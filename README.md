# CodeCraftHub

CodeCraftHub es una API REST sencilla para administrar cursos. El proyecto está desarrollado con Python, Flask y almacenamiento local en un archivo JSON.

Está pensado para principiantes que desean aprender:

- Qué es una API REST.
- Cómo crear, consultar, actualizar y eliminar recursos.
- Cómo utilizar métodos HTTP como `GET`, `POST`, `PUT` y `DELETE`.
- Cómo enviar y recibir información en formato JSON.
- Cómo probar una API utilizando `curl`.
- Cómo conectar un frontend con una API gracias a CORS.

---

## 1. Visión general del proyecto

CodeCraftHub permite gestionar cursos mediante una API REST.

Cada curso contiene los siguientes datos:

|
 Campo 
|
 Descripción 
|
 Requerido 
|
|
---
|
---
|
---
|
|
`id`
|
 Identificador numérico autogenerado 
|
 No 
|
|
`name`
|
 Nombre del curso 
|
 Sí 
|
|
`description`
|
 Descripción del curso 
|
 Sí 
|
|
`target_date`
|
 Fecha objetivo con formato 
`YYYY-MM-DD`
|
 Sí 
|
|
`status`
|
 Estado actual del curso 
|
 Sí 
|
|
`created_at`
|
 Fecha y hora de creación 
|
 No 
|

Los estados permitidos son exactamente:

- `Not Started`
- `In Progress`
- `Completed`

Los cursos se almacenan en el archivo local:

```text
courses.json
Si el archivo no existe, la aplicación lo crea automáticamente al iniciarse.

2. Características principales
CodeCraftHub incluye:

API REST construida con Flask.
CRUD completo para cursos:
Crear cursos.
Consultar todos los cursos.
Consultar un curso por ID.
Actualizar cursos.
Eliminar cursos.
IDs autogenerados comenzando desde
1
.
Almacenamiento persistente en
courses.json
.
Fecha de creación automática mediante
created_at
.
Validación de campos obligatorios.
Validación del formato de fecha.
Validación de estados permitidos.
Respuestas en formato JSON.
Manejo de errores HTTP:
400 Bad Request
404 Not Found
500 Internal Server Error
Endpoint de estadísticas.
CORS habilitado para permitir llamadas desde un frontend en el navegador.
Creación automática del archivo
courses.json
.
3. Tecnologías utilizadas
Python 3
Flask
Flask-CORS
JSON
cURL para realizar pruebas
4. Requisitos previos
Antes de instalar el proyecto, necesitas tener instalado:

Python 3.8 o una versión posterior.
pip
, el instalador de paquetes de Python.
Una terminal:
CMD de Windows.
PowerShell.
Terminal de macOS o Linux.
Para comprobar que Python está instalado, ejecuta:

python --version
En algunos sistemas puede ser necesario utilizar:

python3 --version
También puedes comprobar
pip
con:

pip --version
5. Estructura del proyecto
La estructura mínima del proyecto es:

CodeCraftHub/
│
├── app.py
├── requirements.txt
├── README.md
└── courses.json
Descripción de los archivos
app.py
Contiene:

La aplicación Flask.
Las rutas de la API.
La validación de los datos.
La lectura y escritura de
courses.json
.
El manejo de errores.
La configuración de CORS.
requirements.txt
Contiene las dependencias necesarias para ejecutar el proyecto:

Flask==3.1.0
flask-cors==5.0.0
courses.json
Contiene los cursos almacenados.

Este archivo se crea automáticamente si no existe. Inicialmente tendrá este contenido:

[]
README.md
Contiene la documentación del proyecto y las instrucciones de uso.

6. Instalación paso a paso
Paso 1: Descargar o crear el proyecto
Crea una carpeta llamada
CodeCraftHub
:

mkdir CodeCraftHub
cd CodeCraftHub
Copia dentro de esta carpeta los archivos:

app.py
requirements.txt
README.md
No es necesario crear manualmente
courses.json
, porque la aplicación lo generará automáticamente.

Paso 2: Crear un entorno virtual
Es recomendable utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

En Windows:

python -m venv venv
En macOS o Linux:

python3 -m venv venv
Paso 3: Activar el entorno virtual
Windows CMD
venv\Scripts\activate
Windows PowerShell
venv\Scripts\Activate.ps1
macOS o Linux
source venv/bin/activate
Cuando el entorno virtual está activo, normalmente aparece
(venv)
al inicio de la línea de comandos.

Paso 4: Instalar las dependencias
Ejecuta:

pip install -r requirements.txt
Si tu sistema utiliza
pip3
, ejecuta:

pip3 install -r requirements.txt
7. Cómo ejecutar la aplicación
Con el entorno virtual activado, ejecuta:

python app.py
En macOS o Linux puede ser necesario:

python3 app.py
La aplicación se ejecutará en:

http://localhost:5000
La API estará disponible en:

http://localhost:5000/api/courses
Para detener la aplicación, presiona:

Ctrl + C
8. Formato general de las solicitudes
Para enviar datos a la API se utiliza JSON.

Las solicitudes
POST
y
PUT
deben incluir esta cabecera:

Content-Type: application/json
Ejemplo de una carga útil JSON:

{
  "name": "Python para principiantes",
  "description": "Curso introductorio de programación con Python",
  "target_date": "2026-12-31",
  "status": "Not Started"
}
Los cuatro campos siguientes son obligatorios:

name
description
target_date
status
El campo
target_date
debe utilizar exactamente el formato:

YYYY-MM-DD
Ejemplo válido:

2026-12-31
Ejemplos no válidos:

31-12-2026
2026/12/31
2026-1-5
9. Documentación de la API
9.1 Crear un curso
POST /api/courses
Descripción
Crea un curso nuevo.

El
id
y el
created_at
son generados automáticamente por la aplicación.

Ejemplo con cURL para CMD de Windows
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Python para principiantes\",\"description\":\"Curso introductorio de programación con Python\",\"target_date\":\"2026-12-31\",\"status\":\"Not Started\"}"
Carga útil JSON
{
  "name": "Python para principiantes",
  "description": "Curso introductorio de programación con Python",
  "target_date": "2026-12-31",
  "status": "Not Started"
}
Respuesta exitosa
Código HTTP:

201 Created
Respuesta:

{
  "message": "Curso creado correctamente.",
  "course": {
    "id": 1,
    "name": "Python para principiantes",
    "description": "Curso introductorio de programación con Python",
    "target_date": "2026-12-31",
    "status": "Not Started",
    "created_at": "2026-11-22T10:30:00.000000Z"
  }
}
El valor de
created_at
dependerá del momento en que se cree el curso.

9.2 Obtener todos los cursos
GET /api/courses
Descripción
Devuelve todos los cursos almacenados.

Ejemplo con cURL
curl -X GET http://localhost:5000/api/courses
Respuesta exitosa
Código HTTP:

200 OK
Respuesta:

{
  "courses": [
    {
      "id": 1,
      "name": "Python para principiantes",
      "description": "Curso introductorio de programación con Python",
      "target_date": "2026-12-31",
      "status": "Not Started",
      "created_at": "2026-11-22T10:30:00.000000Z"
    }
  ],
  "total": 1
}
La propiedad
courses
contiene una lista de cursos y
total
indica cuántos cursos existen.

Si no hay cursos, la respuesta será similar a:

{
  "courses": [],
  "total": 0
}
9.3 Obtener un curso por ID
GET /api/courses/<id>
Reemplaza
<id>
por el identificador del curso.

Ejemplo
curl -X GET http://localhost:5000/api/courses/1
Respuesta exitosa
Código HTTP:

200 OK
Respuesta:

{
  "course": {
    "id": 1,
    "name": "Python para principiantes",
    "description": "Curso introductorio de programación con Python",
    "target_date": "2026-12-31",
    "status": "Not Started",
    "created_at": "2026-11-22T10:30:00.000000Z"
  }
}
9.4 Actualizar un curso
PUT /api/courses/<id>
Descripción
Actualiza un curso existente.

El método
PUT
requiere enviar los cuatro campos obligatorios:

name
description
target_date
status
El campo
created_at
no se envía. La aplicación conserva automáticamente la fecha original de creación.

Carga útil JSON
{
  "name": "Python avanzado",
  "description": "Curso avanzado de desarrollo con Python y Flask",
  "target_date": "2027-02-28",
  "status": "In Progress"
}
Ejemplo con cURL
curl -X PUT http://localhost:5000/api/courses/1 -H "Content-Type: application/json" -d "{\"name\":\"Python avanzado\",\"description\":\"Curso avanzado de desarrollo con Python y Flask\",\"target_date\":\"2027-02-28\",\"status\":\"In Progress\"}"
Respuesta exitosa
Código HTTP:

200 OK
Respuesta:

{
  "message": "Curso actualizado correctamente.",
  "course": {
    "id": 1,
    "name": "Python avanzado",
    "description": "Curso avanzado de desarrollo con Python y Flask",
    "target_date": "2027-02-28",
    "status": "In Progress",
    "created_at": "2026-11-22T10:30:00.000000Z"
  }
}
9.5 Eliminar un curso
DELETE /api/courses/<id>
Descripción
Elimina un curso por su identificador.

Ejemplo con cURL
curl -X DELETE http://localhost:5000/api/courses/1
Respuesta exitosa
Código HTTP:

200 OK
Respuesta:

{
  "message": "Curso eliminado correctamente.",
  "course": {
    "id": 1,
    "name": "Python avanzado",
    "description": "Curso avanzado de desarrollo con Python y Flask",
    "target_date": "2027-02-28",
    "status": "In Progress",
    "created_at": "2026-11-22T10:30:00.000000Z"
  }
}
9.6 Obtener estadísticas
GET /api/courses/stats
Descripción
Devuelve:

El total de cursos.
La cantidad de cursos agrupada por estado.
Ejemplo con cURL
curl -X GET http://localhost:5000/api/courses/stats
Respuesta exitosa
Código HTTP:

200 OK
Respuesta:

{
  "total": 3,
  "by_status": {
    "Not Started": 1,
    "In Progress": 1,
    "Completed": 1
  }
}
La propiedad
by_status
siempre incluye los tres estados permitidos:

Not Started
In Progress
Completed
10. Estados permitidos
Cada curso debe utilizar uno de estos estados:

Not Started
El curso todavía no ha comenzado.

{
  "status": "Not Started"
}
In Progress
El curso se encuentra en progreso.

{
  "status": "In Progress"
}
Completed
El curso ha sido completado.

{
  "status": "Completed"
}
No se permiten valores como:

Pending
Finished
Started
completed
in progress
Los estados distinguen entre mayúsculas y minúsculas.

11. Respuestas de error
Los errores se devuelven en formato JSON utilizando la propiedad
error
.

Ejemplo:

{
  "error": "Curso no encontrado."
}
Error
400 Bad Request
Se utiliza cuando los datos enviados son incorrectos.

Campos faltantes
{
  "error": "Faltan campos obligatorios: description"
}
Estado inválido
{
  "error": "Estado inválido. Los estados permitidos son: 'Not Started', 'In Progress' y 'Completed'."
}
Fecha inválida
{
  "error": "El campo 'target_date' debe tener el formato YYYY-MM-DD."
}
Solicitud sin JSON
{
  "error": "La solicitud debe tener Content-Type: application/json"
}
Error
404 Not Found
Se utiliza cuando el curso no existe o la ruta no está disponible.

{
  "error": "Curso no encontrado."
}
Error
500 Internal Server Error
Se utiliza cuando ocurre un problema leyendo o escribiendo
courses.json
, o cuando ocurre otro error interno.

Ejemplo:

{
  "error": "No se pudo leer el archivo de datos."
}
12. Instrucciones de prueba
12.1 Crear el primer curso
Ejecuta:

curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Python para principiantes\",\"description\":\"Curso introductorio de programación con Python\",\"target_date\":\"2026-12-31\",\"status\":\"Not Started\"}"
Deberías recibir una respuesta con código
201
.

12.2 Crear un segundo curso
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Desarrollo de APIs REST\",\"description\":\"Creación de APIs con Flask y Python\",\"target_date\":\"2027-01-15\",\"status\":\"In Progress\"}"
12.3 Crear un tercer curso
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Bases de datos SQL\",\"description\":\"Fundamentos de SQL y bases de datos relacionales\",\"target_date\":\"2026-10-30\",\"status\":\"Completed\"}"
12.4 Consultar todos los cursos
curl -X GET http://localhost:5000/api/courses
Comprueba que la respuesta contenga:

{
  "courses": [],
  "total": 3
}
La lista no estará vacía y
total
debería indicar la cantidad de cursos creados.

12.5 Consultar las estadísticas
curl -X GET http://localhost:5000/api/courses/stats
Si creaste un curso con cada estado, la respuesta esperada será:

{
  "total": 3,
  "by_status": {
    "Not Started": 1,
    "In Progress": 1,
    "Completed": 1
  }
}
12.6 Consultar un curso específico
curl -X GET http://localhost:5000/api/courses/1
La respuesta debe contener una propiedad llamada
course
.

12.7 Actualizar un curso
curl -X PUT http://localhost:5000/api/courses/1 -H "Content-Type: application/json" -d "{\"name\":\"Python avanzado\",\"description\":\"Curso avanzado de desarrollo con Python y Flask\",\"target_date\":\"2027-02-28\",\"status\":\"Completed\"}"
La respuesta debe tener:

{
  "message": "Curso actualizado correctamente.",
  "course": {}
}
12.8 Eliminar un curso
curl -X DELETE http://localhost:5000/api/courses/3
La respuesta debe tener:

{
  "message": "Curso eliminado correctamente.",
  "course": {}
}
12.9 Probar un curso inexistente
curl -X GET http://localhost:5000/api/courses/9999
Respuesta esperada:

{
  "error": "Curso no encontrado."
}
Código HTTP esperado:

404
12.10 Probar un estado inválido
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso de prueba\",\"description\":\"Descripción de prueba\",\"target_date\":\"2027-03-10\",\"status\":\"Pending\"}"
La API debe devolver un error
400
.

12.11 Probar campos faltantes
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso incompleto\",\"target_date\":\"2027-03-10\",\"status\":\"Not Started\"}"
Respuesta esperada:

{
  "error": "Faltan campos obligatorios: description"
}
12.12 Probar una fecha inválida
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso con fecha incorrecta\",\"description\":\"Descripción de prueba\",\"target_date\":\"10-03-2027\",\"status\":\"Not Started\"}"
Respuesta esperada:

{
  "error": "El campo 'target_date' debe tener el formato YYYY-MM-DD."
}
13. Solución de problemas comunes
Problema:
python
no se reconoce como comando
Posible solución
Instala Python desde su sitio oficial y asegúrate de activar la opción:

Add Python to PATH
Después, cierra y vuelve a abrir la terminal.

También puedes probar:

py --version
Y ejecutar la aplicación con:

py app.py
Problema:
pip install
falla
Comprueba que el entorno virtual esté activado.

En Windows CMD:

venv\Scripts\activate
Después vuelve a ejecutar:

pip install -r requirements.txt
También puedes actualizar
pip
:

python -m pip install --upgrade pip
Problema: el puerto 5000 ya está siendo utilizado
La aplicación utiliza:

http://localhost:5000
Si otro programa está utilizando ese puerto, cierra el programa correspondiente o cambia el puerto en
app.py
.

Por ejemplo:

app.run(
    host="localhost",
    port=5001,
    debug=False,
)
En ese caso, la API estará disponible en:

http://localhost:5001
Los comandos
curl
también deberán utilizar el nuevo puerto.

Problema: aparece un error
404
Comprueba que:

La aplicación esté ejecutándose.
La URL esté escrita correctamente.
El endpoint tenga el prefijo
/api
.
El ID del curso exista.
Ejemplo correcto:

http://localhost:5000/api/courses
Ejemplo incorrecto:

http://localhost:5000/courses
Problema: aparece un error
400
Comprueba que:

La solicitud incluya la cabecera
Content-Type: application/json
.
El cuerpo tenga JSON válido.
Se incluyan los cuatro campos obligatorios.
El estado sea uno de los permitidos.
La fecha tenga formato
YYYY-MM-DD
.
Ejemplo válido:

{
  "name": "Curso válido",
  "description": "Descripción válida",
  "target_date": "2027-05-20",
  "status": "In Progress"
}
Problema:
courses.json
no aparece
El archivo se crea cuando se inicia
app.py
.

Comprueba que:

La aplicación se haya iniciado correctamente.
Tengas permisos de escritura en la carpeta.
Estés revisando la misma carpeta donde se encuentra
app.py
.
Problema: error al leer
courses.json
Comprueba que
courses.json
contenga una lista JSON válida.

Contenido válido cuando no hay cursos:

[]
Contenido válido con un curso:

[
  {
    "id": 1,
    "name": "Python",
    "description": "Curso de Python",
    "target_date": "2027-01-01",
    "status": "Not Started",
    "created_at": "2026-11-22T10:30:00.000000Z"
  }
]
No escribas texto adicional fuera del JSON.

Problema: el navegador bloquea la solicitud
La aplicación utiliza
flask-cors
para habilitar CORS.

Comprueba que:

flask-cors
esté instalado:

pip install flask-cors
También verifica que la aplicación se haya reiniciado después de instalar la dependencia.

Problema:
curl
no funciona en Windows
Las versiones modernas de Windows incluyen
curl
.

Puedes comprobarlo con:

curl --version
Si no está disponible, puedes utilizar:

PowerShell.
Postman.
Insomnia.
Un frontend JavaScript.
Otra herramienta para realizar solicitudes HTTP.
14. Conceptos básicos de una API REST
GET
Se utiliza para consultar información.

Ejemplo:

GET /api/courses
POST
Se utiliza para crear un recurso nuevo.

Ejemplo:

POST /api/courses
PUT
Se utiliza para actualizar un recurso existente.

Ejemplo:

PUT /api/courses/1
DELETE
Se utiliza para eliminar un recurso.

Ejemplo:

DELETE /api/courses/1
15. Códigos HTTP utilizados
Código	Significado	Uso en CodeCraftHub
200
OK	Consulta, actualización, eliminación y estadísticas exitosas
201
Created	Curso creado correctamente
400
Bad Request	Datos inválidos o campos faltantes
404
Not Found	Curso o ruta no encontrados
500
Internal Server Error	Error interno o problema con el archivo JSON
16. Ejemplo completo de un curso
{
  "id": 1,
  "name": "Desarrollo de APIs REST",
  "description": "Aprende a crear APIs con Python y Flask",
  "target_date": "2027-01-15",
  "status": "In Progress",
  "created_at": "2026-11-22T10:30:00.000000Z"
}
17. Flujo recomendado para utilizar la aplicación
Un flujo normal puede ser:

Iniciar la aplicación.
Crear uno o varios cursos con
POST
.
Consultar los cursos con
GET
.
Consultar las estadísticas.
Actualizar un curso con
PUT
.
Consultar nuevamente el curso para comprobar el cambio.
Eliminar un curso con
DELETE
.
Consultar las estadísticas otra vez.
La API permite que cualquier frontend compatible con CORS se conecte a ella desde el navegador.

18. Licencia
Este proyecto puede utilizarse con fines educativos para aprender Python, Flask, APIs REST, JSON y desarrollo web.

undefined