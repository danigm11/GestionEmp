# GestionEmp

Empresa: TwoGs

Participantes:

Daniel Martín Sáiz --> Equipos

TODAS LAS PETICIONES TIENEN UN EJEMPLO PARA FACILITAR SU USO EN POSTMAN EN EL ARCHIVO equipos.py, LAS PETICIONES ESTÁN COMENTADAS ENCIMA DE CADA FUNCIÓN

GET - /equipos : Muestra la lista de todos los equipos.

GET - /equipos/int:id : Muestra los datos del equipo con esa id.

GET - /equipos/filtrar_por_nombre :  Muestra los equipos con el nombre parado por parámetro, para configurar el parámetro desde porstman debemos presionar Params y añadir uno nuevo, key: nombre value: T1 por ejemplo.

GET - equipos/filtrar_por_titulos_mundiales?num_titulos=2  : Muestra los equipos con más titulos internacionales que el parámetro pasado, la configuración se hace igual que para filtrar por nombre, en Params  key:titulos_mundiales value: 2.

POST - /equipos : Sirve para añadir un equipo nuevo pasandol en el body los campos, ejemplo comentado en el archivo equipos.py.

PUT - /equipos/int:id  : Sirve para modificar equipos ya creados, pasandole por el body los campos que queremos modificar y especificando ID.

DELETE - /equipos/int:id  : Sirve para borrar equipos pasandole la Id en la url.

POST - /jugadoresD : Sirve para añadir un jugador a un equipo, pasandole en el body los campos requeridos.

GET - equipos/int:id/jugadores : Sirve para comprobar los jugadores que pertenecen a los equipos y así realizar una petición entre tablas, hay que pasarle la id del equipo en la petición.

Adolfo Burgos Belgrano

Gonzalo Ruíz Azuar

Daniel García Mesa --> Torneos

/torneos : Devuelve una lista que contiene los torneos creados con todos sus datos

/torneos/string:sede : Devuelve la lista anterior pero solo los torneos que contengan la sede especificada, Ej: Madrid

/torneos/nuevo : Nos permite crear un nuevo torneo

/torneos/borrar/int:id : Nos permite eliminar un torneo indicando su ID, se pueden ver las IDs de los torneos en el primer endpoint

/torneos/editar/int:id : Nos permite editar la información de un torneo indicando su ID y los campos que vamos a modificar en el body

/torneos/mostrar/int:id : Nos permite ver toda la información de un torneo indicando su ID