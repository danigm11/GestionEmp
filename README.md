# GestionEmp

Empresa: TwoGs

Participantes: 

Daniel Martín Sáiz --> Equipos

Adolfo Burgos Belgrano 

Gonzalo Ruíz Azuar

Daniel García Mesa --> Torneos


/torneos : Devuelve una lista que contiene los torneos creados con todos sus datos

/torneos/<string:sede> : Devuelve la lista anterior pero solo los torneos que contengan la sede especificada, Ej: Madrid


/torneos/nuevo : Nos permite crear un nuevo torneo


/torneos/borrar/<int:id> : Nos permite eliminar un torneo indicando su ID, se pueden ver las IDs de los torneos en el primer endpoint

/torneos/editar/<int:id> : Nos permite editar la información de un torneo indicando su ID y los campos que vamos a modificar en el body

/torneos/mostrar/<int:id> : Nos permite ver toda la información de un torneo indicando su ID

