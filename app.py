import json
import os
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS


# -----------------------------------------------------------------------------
# Configuración inicial
# -----------------------------------------------------------------------------

app = Flask(__name__)

# Permite que un frontend en el navegador consuma esta API.
CORS(app)

# El archivo courses.json se guardará en la misma carpeta que app.py.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "courses.json")

# Estados permitidos para los cursos.
VALID_STATUSES = {
    "Not Started",
    "In Progress",
    "Completed",
}


class StorageError(Exception):
    """Error personalizado para problemas leyendo o escribiendo el archivo JSON."""


# -----------------------------------------------------------------------------
# Funciones auxiliares para trabajar con courses.json
# -----------------------------------------------------------------------------

def ensure_data_file():
    """
    Crea courses.json automáticamente si todavía no existe.
    """
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4, ensure_ascii=False)
        except OSError as error:
            raise StorageError(
                f"No se pudo crear el archivo de datos: {error}"
            ) from error


def read_courses():
    """
    Lee todos los cursos desde courses.json.

    Retorna:
        list: Lista de cursos.
    """
    ensure_data_file()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        # El archivo debe contener una lista.
        if not isinstance(data, list):
            raise StorageError(
                "El archivo courses.json debe contener una lista de cursos."
            )

        return data

    except json.JSONDecodeError as error:
        raise StorageError(
            "El archivo courses.json contiene JSON inválido."
        ) from error

    except OSError as error:
        raise StorageError(
            f"No se pudo leer el archivo de datos: {error}"
        ) from error


def write_courses(courses):
    """
    Guarda la lista de cursos en courses.json.
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(courses, file, indent=4, ensure_ascii=False)

    except (OSError, TypeError, ValueError) as error:
        raise StorageError(
            f"No se pudo escribir el archivo de datos: {error}"
        ) from error


def get_next_id(courses):
    """
    Genera el siguiente ID disponible.

    Si no existen cursos, empieza desde 1.
    Después utiliza el ID más alto existente + 1.
    """
    if not courses:
        return 1

    ids = [
        course.get("id", 0)
        for course in courses
        if isinstance(course.get("id", 0), int)
    ]

    return max(ids, default=0) + 1


def validate_course_data(data):
    """
    Valida los campos enviados para crear o actualizar un curso.

    Retorna:
        tuple:
            - error: mensaje de error o None
            - cleaned_data: datos preparados o None
    """
    if not isinstance(data, dict):
        return "El cuerpo de la solicitud debe ser un objeto JSON.", None

    required_fields = [
        "name",
        "description",
        "target_date",
        "status",
    ]

    # Verificamos que todos los campos obligatorios existan.
    missing_fields = [
        field
        for field in required_fields
        if field not in data
        or data[field] is None
        or (
            isinstance(data[field], str)
            and not data[field].strip()
        )
    ]

    if missing_fields:
        return (
            "Faltan campos obligatorios: "
            + ", ".join(missing_fields),
            None,
        )

    # Todos estos campos deben ser texto.
    for field in required_fields:
        if not isinstance(data[field], str):
            return f"El campo '{field}' debe ser texto.", None

    name = data["name"].strip()
    description = data["description"].strip()
    target_date = data["target_date"].strip()
    status = data["status"].strip()

    # Validamos el estado.
    if status not in VALID_STATUSES:
        return (
            "Estado inválido. Los estados permitidos son: "
            "'Not Started', 'In Progress' y 'Completed'.",
            None,
        )

    # Validamos que la fecha tenga formato YYYY-MM-DD
    # y que además sea una fecha real.
    try:
        parsed_date = datetime.strptime(target_date, "%Y-%m-%d")

        # Esto evita aceptar formatos como 2025-1-1.
        if parsed_date.strftime("%Y-%m-%d") != target_date:
            return (
                "El campo 'target_date' debe tener el formato YYYY-MM-DD.",
                None,
            )

    except ValueError:
        return (
            "El campo 'target_date' debe tener el formato YYYY-MM-DD.",
            None,
        )

    cleaned_data = {
        "name": name,
        "description": description,
        "target_date": target_date,
        "status": status,
    }

    return None, cleaned_data


def get_json_body():
    """
    Obtiene y valida el cuerpo JSON de la solicitud.
    """
    if not request.is_json:
        return None, (
            jsonify({
                "error": "La solicitud debe tener Content-Type: application/json"
            }),
            400,
        )

    data = request.get_json(silent=True)

    if data is None:
        return None, (
            jsonify({
                "error": "El cuerpo de la solicitud debe contener JSON válido."
            }),
            400,
        )

    return data, None


# -----------------------------------------------------------------------------
# Endpoints de cursos
# -----------------------------------------------------------------------------

@app.route("/api/courses", methods=["POST"])
def create_course():
    """
    Crea un nuevo curso.
    """
    data, error_response = get_json_body()

    if error_response:
        return error_response

    validation_error, cleaned_data = validate_course_data(data)

    if validation_error:
        return jsonify({"error": validation_error}), 400

    try:
        courses = read_courses()

        new_course = {
            "id": get_next_id(courses),
            "name": cleaned_data["name"],
            "description": cleaned_data["description"],
            "target_date": cleaned_data["target_date"],
            "status": cleaned_data["status"],
            "created_at": datetime.utcnow().isoformat() + "Z",
        }

        courses.append(new_course)
        write_courses(courses)

        return jsonify({
            "message": "Curso creado correctamente.",
            "course": new_course,
        }), 201

    except StorageError as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses", methods=["GET"])
def get_courses():
    """
    Retorna todos los cursos.
    """
    try:
        courses = read_courses()

        return jsonify({
            "courses": courses,
            "total": len(courses),
        }), 200

    except StorageError as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses/stats", methods=["GET"])
def get_course_stats():
    """
    Retorna el total de cursos y la cantidad por estado.
    """
    try:
        courses = read_courses()

        courses_by_status = {
            "Not Started": 0,
            "In Progress": 0,
            "Completed": 0,
        }

        for course in courses:
            status = course.get("status")

            if status in courses_by_status:
                courses_by_status[status] += 1

        return jsonify({
            "total": len(courses),
            "by_status": courses_by_status,
        }), 200

    except StorageError as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    """
    Retorna un curso específico por su ID.
    """
    try:
        courses = read_courses()

        course = next(
            (course for course in courses if course.get("id") == course_id),
            None,
        )

        if course is None:
            return jsonify({
                "error": "Curso no encontrado."
            }), 404

        return jsonify({"course": course}), 200

    except StorageError as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    """
    Actualiza completamente un curso existente.

    Para PUT se deben enviar todos los campos obligatorios:
    name, description, target_date y status.
    """
    data, error_response = get_json_body()

    if error_response:
        return error_response

    validation_error, cleaned_data = validate_course_data(data)

    if validation_error:
        return jsonify({"error": validation_error}), 400

    try:
        courses = read_courses()

        course_index = next(
            (
                index
                for index, course in enumerate(courses)
                if course.get("id") == course_id
            ),
            None,
        )

        if course_index is None:
            return jsonify({
                "error": "Curso no encontrado."
            }), 404

        old_course = courses[course_index]

        updated_course = {
            "id": course_id,
            "name": cleaned_data["name"],
            "description": cleaned_data["description"],
            "target_date": cleaned_data["target_date"],
            "status": cleaned_data["status"],
            # Se conserva la fecha original de creación.
            "created_at": old_course.get(
                "created_at",
                datetime.utcnow().isoformat() + "Z",
            ),
        }

        courses[course_index] = updated_course
        write_courses(courses)

        return jsonify({
            "message": "Curso actualizado correctamente.",
            "course": updated_course,
        }), 200

    except StorageError as error:
        return jsonify({"error": str(error)}), 500


@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    """
    Elimina un curso por su ID.
    """
    try:
        courses = read_courses()

        course_index = next(
            (
                index
                for index, course in enumerate(courses)
                if course.get("id") == course_id
            ),
            None,
        )

        if course_index is None:
            return jsonify({
                "error": "Curso no encontrado."
            }), 404

        deleted_course = courses.pop(course_index)
        write_courses(courses)

        return jsonify({
            "message": "Curso eliminado correctamente.",
            "course": deleted_course,
        }), 200

    except StorageError as error:
        return jsonify({"error": str(error)}), 500


# -----------------------------------------------------------------------------
# Manejo global de errores
# -----------------------------------------------------------------------------

@app.errorhandler(404)
def handle_404(error):
    """
    Devuelve errores 404 en formato JSON.
    """
    return jsonify({
        "error": "La ruta solicitada no existe."
    }), 404


@app.errorhandler(405)
def handle_405(error):
    """
    Devuelve errores de método HTTP no permitido en formato JSON.
    """
    return jsonify({
        "error": "Método HTTP no permitido para esta ruta."
    }), 405


@app.errorhandler(500)
def handle_500(error):
    """
    Devuelve errores internos en formato JSON.
    """
    return jsonify({
        "error": "Ocurrió un error interno en el servidor."
    }), 500


# -----------------------------------------------------------------------------
# Inicio de la aplicación
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Se crea el archivo automáticamente al iniciar la aplicación.
    try:
        ensure_data_file()
    except StorageError as error:
        print(f"Advertencia: {error}")

    # La API estará disponible en http://localhost:5000
    app.run(
        host="localhost",
        port=5000,
        debug=False,
    )