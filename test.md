Casos de prueba para la API de CodeCraftHub
La API debe estar ejecutándose en:

http://localhost:5000
Antes de comenzar:

python app.py
Los siguientes comandos están preparados para CMD de Windows y cada uno ocupa una sola línea.

1. Crear cursos con
POST /api/courses
Caso exitoso: curso
Not Started
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Python para principiantes\",\"description\":\"Curso introductorio de programación con Python\",\"target_date\":\"2026-12-31\",\"status\":\"Not Started\"}"
Respuesta esperada:

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
Código HTTP esperado:

201 Created
El valor de
created_at
será diferente en cada ejecución.

Caso exitoso: curso
In Progress
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Desarrollo de APIs REST\",\"description\":\"Creación de APIs con Flask y Python\",\"target_date\":\"2027-01-15\",\"status\":\"In Progress\"}"
Respuesta esperada:

{
  "message": "Curso creado correctamente.",
  "course": {
    "id": 2,
    "name": "Desarrollo de APIs REST",
    "description": "Creación de APIs con Flask y Python",
    "target_date": "2027-01-15",
    "status": "In Progress",
    "created_at": "2026-11-22T10:35:00.000000Z"
  }
}
Código HTTP esperado:

201 Created
Caso exitoso: curso
Completed
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Bases de datos SQL\",\"description\":\"Fundamentos de SQL y bases de datos relacionales\",\"target_date\":\"2026-10-30\",\"status\":\"Completed\"}"
Respuesta esperada:

{
  "message": "Curso creado correctamente.",
  "course": {
    "id": 3,
    "name": "Bases de datos SQL",
    "description": "Fundamentos de SQL y bases de datos relacionales",
    "target_date": "2026-10-30",
    "status": "Completed",
    "created_at": "2026-11-22T10:40:00.000000Z"
  }
}
Código HTTP esperado:

201 Created
2. Consultar todos los cursos
GET /api/courses
curl -X GET http://localhost:5000/api/courses
Respuesta esperada:

{
  "courses": [
    {
      "id": 1,
      "name": "Python para principiantes",
      "description": "Curso introductorio de programación con Python",
      "target_date": "2026-12-31",
      "status": "Not Started",
      "created_at": "2026-11-22T10:30:00.000000Z"
    },
    {
      "id": 2,
      "name": "Desarrollo de APIs REST",
      "description": "Creación de APIs con Flask y Python",
      "target_date": "2027-01-15",
      "status": "In Progress",
      "created_at": "2026-11-22T10:35:00.000000Z"
    },
    {
      "id": 3,
      "name": "Bases de datos SQL",
      "description": "Fundamentos de SQL y bases de datos relacionales",
      "target_date": "2026-10-30",
      "status": "Completed",
      "created_at": "2026-11-22T10:40:00.000000Z"
    }
  ],
  "total": 3
}
Código HTTP esperado:

200 OK
3. Consultar un curso por ID
GET /api/courses/1
curl -X GET http://localhost:5000/api/courses/1
Respuesta esperada:

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
Código HTTP esperado:

200 OK
4. Consultar estadísticas
GET /api/courses/stats
curl -X GET http://localhost:5000/api/courses/stats
Respuesta esperada con los tres cursos creados anteriormente:

{
  "total": 3,
  "by_status": {
    "Not Started": 1,
    "In Progress": 1,
    "Completed": 1
  }
}
Código HTTP esperado:

200 OK
5. Actualizar un curso
Para
PUT
, la API requiere enviar todos los campos obligatorios:

name
description
target_date
status
Carga útil JSON para PUT
{
  "name": "Python avanzado",
  "description": "Curso avanzado de desarrollo con Python y Flask",
  "target_date": "2027-02-28",
  "status": "In Progress"
}
Comando
PUT /api/courses/1
curl -X PUT http://localhost:5000/api/courses/1 -H "Content-Type: application/json" -d "{\"name\":\"Python avanzado\",\"description\":\"Curso avanzado de desarrollo con Python y Flask\",\"target_date\":\"2027-02-28\",\"status\":\"In Progress\"}"
Respuesta esperada:

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
Código HTTP esperado:

200 OK
La propiedad
created_at
debe conservar su valor original.

6. Eliminar un curso
DELETE /api/courses/3
curl -X DELETE http://localhost:5000/api/courses/3
Respuesta esperada:

{
  "message": "Curso eliminado correctamente.",
  "course": {
    "id": 3,
    "name": "Bases de datos SQL",
    "description": "Fundamentos de SQL y bases de datos relacionales",
    "target_date": "2026-10-30",
    "status": "Completed",
    "created_at": "2026-11-22T10:40:00.000000Z"
  }
}
Código HTTP esperado:

200 OK
Casos de error
7. POST con campos faltantes
Falta
description
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso incompleto\",\"target_date\":\"2027-03-10\",\"status\":\"Not Started\"}"
Respuesta esperada:

{
  "error": "Faltan campos obligatorios: description"
}
Código HTTP esperado:

400 Bad Request
Faltan varios campos
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso incompleto\"}"
Respuesta esperada:

{
  "error": "Faltan campos obligatorios: description, target_date, status"
}
Código HTTP esperado:

400 Bad Request
Campo vacío
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"\",\"description\":\"Descripción válida\",\"target_date\":\"2027-03-10\",\"status\":\"Not Started\"}"
Respuesta esperada:

{
  "error": "Faltan campos obligatorios: name"
}
Código HTTP esperado:

400 Bad Request
8. POST con estado inválido
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso con estado incorrecto\",\"description\":\"Descripción del curso\",\"target_date\":\"2027-03-10\",\"status\":\"Pending\"}"
Respuesta esperada:

{
  "error": "Estado inválido. Los estados permitidos son: 'Not Started', 'In Progress' y 'Completed'."
}
Código HTTP esperado:

400 Bad Request
Los únicos estados válidos son:

Not Started
In Progress
Completed
9. POST con fecha inválida
Formato incorrecto
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso con fecha incorrecta\",\"description\":\"Descripción del curso\",\"target_date\":\"10-03-2027\",\"status\":\"Not Started\"}"
Respuesta esperada:

{
  "error": "El campo 'target_date' debe tener el formato YYYY-MM-DD."
}
Código HTTP esperado:

400 Bad Request
Fecha inexistente
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso con fecha inexistente\",\"description\":\"Descripción del curso\",\"target_date\":\"2027-02-30\",\"status\":\"Not Started\"}"
Respuesta esperada:

{
  "error": "El campo 'target_date' debe tener el formato YYYY-MM-DD."
}
Código HTTP esperado:

400 Bad Request
Fecha sin ceros iniciales
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso con formato incorrecto\",\"description\":\"Descripción del curso\",\"target_date\":\"2027-1-5\",\"status\":\"Not Started\"}"
Respuesta esperada:

{
  "error": "El campo 'target_date' debe tener el formato YYYY-MM-DD."
}
Código HTTP esperado:

400 Bad Request
10. POST con tipos de datos incorrectos
name
no es texto
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":123,\"description\":\"Descripción válida\",\"target_date\":\"2027-03-10\",\"status\":\"Not Started\"}"
Respuesta esperada:

{
  "error": "El campo 'name' debe ser texto."
}
Código HTTP esperado:

400 Bad Request
status
no es texto
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso válido\",\"description\":\"Descripción válida\",\"target_date\":\"2027-03-10\",\"status\":1}"
Respuesta esperada:

{
  "error": "El campo 'status' debe ser texto."
}
Código HTTP esperado:

400 Bad Request
11. Solicitud sin JSON
curl -X POST http://localhost:5000/api/courses -d "name=Curso&description=Descripcion"
Respuesta esperada:

{
  "error": "La solicitud debe tener Content-Type: application/json"
}
Código HTTP esperado:

400 Bad Request
12. JSON inválido
curl -X POST http://localhost:5000/api/courses -H "Content-Type: application/json" -d "{\"name\":\"Curso inválido\",\"description\":}"
Respuesta esperada:

{
  "error": "El cuerpo de la solicitud debe contener JSON válido."
}
Código HTTP esperado:

400 Bad Request
13. Consultar un curso inexistente
GET /api/courses/9999
curl -X GET http://localhost:5000/api/courses/9999
Respuesta esperada:

{
  "error": "Curso no encontrado."
}
Código HTTP esperado:

404 Not Found
14. Actualizar un curso inexistente
PUT /api/courses/9999
curl -X PUT http://localhost:5000/api/courses/9999 -H "Content-Type: application/json" -d "{\"name\":\"Curso inexistente\",\"description\":\"Descripción del curso\",\"target_date\":\"2027-04-01\",\"status\":\"In Progress\"}"
Respuesta esperada:

{
  "error": "Curso no encontrado."
}
Código HTTP esperado:

404 Not Found
15. Eliminar un curso inexistente
DELETE /api/courses/9999
curl -X DELETE http://localhost:5000/api/courses/9999
Respuesta esperada:

{
  "error": "Curso no encontrado."
}
Código HTTP esperado:

404 Not Found
16. PUT con campos faltantes
curl -X PUT http://localhost:5000/api/courses/1 -H "Content-Type: application/json" -d "{\"name\":\"Nombre actualizado\",\"status\":\"Completed\"}"
Respuesta esperada:

{
  "error": "Faltan campos obligatorios: description, target_date"
}
Código HTTP esperado:

400 Bad Request
17. PUT con estado inválido
curl -X PUT http://localhost:5000/api/courses/1 -H "Content-Type: application/json" -d "{\"name\":\"Python actualizado\",\"description\":\"Nueva descripción\",\"target_date\":\"2027-05-20\",\"status\":\"Finished\"}"
Respuesta esperada:

{
  "error": "Estado inválido. Los estados permitidos son: 'Not Started', 'In Progress' y 'Completed'."
}
Código HTTP esperado:

400 Bad Request
18. PUT con fecha inválida
curl -X PUT http://localhost:5000/api/courses/1 -H "Content-Type: application/json" -d "{\"name\":\"Python actualizado\",\"description\":\"Nueva descripción\",\"target_date\":\"2027/05/20\",\"status\":\"Completed\"}"
Respuesta esperada:

{
  "error": "El campo 'target_date' debe tener el formato YYYY-MM-DD."
}
Código HTTP esperado:

400 Bad Request
19. Ruta inexistente
curl -X GET http://localhost:5000/api/unknown
Respuesta esperada:

{
  "error": "La ruta solicitada no existe."
}
Código HTTP esperado:

404 Not Found
20. Método HTTP no permitido
Por ejemplo, intentar usar
DELETE
sobre la colección completa:

curl -X DELETE http://localhost:5000/api/courses
Respuesta esperada:

{
  "error": "Método HTTP no permitido para esta ruta."
}
Código HTTP esperado:

405 Method Not Allowed
Secuencia recomendada para principiantes
Ejecuta las pruebas principales en este orden:

1. POST /api/courses       Crear el primer curso
2. POST /api/courses       Crear el segundo curso
3. POST /api/courses       Crear el tercer curso
4. GET /api/courses        Ver todos los cursos
5. GET /api/courses/1      Ver un curso concreto
6. GET /api/courses/stats  Ver estadísticas
7. PUT /api/courses/1      Actualizar un curso
8. DELETE /api/courses/3   Eliminar un curso
9. GET /api/courses/9999   Probar curso inexistente
10. POST /api/courses      Probar datos inválidos
La respuesta de error siempre debe incluir una propiedad
error
y utilizar estos códigos:

400 - Datos enviados incorrectamente
404 - Curso o ruta no encontrados
500 - Error interno o de lectura/escritura