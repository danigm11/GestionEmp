CREATE DATABASE IF NOT EXISTS TwoGs;

USE TwoGs;

CREATE TABLE IF NOT EXISTS Torneos (
    ID INTEGER NOT NULL UNIQUE,
    Nombre TEXT,
    Sede TEXT,
    Fecha TEXT,
    Premio NUMERIC,
    Categoria TEXT,
    PRIMARY KEY(ID)
);
CREATE DATABASE IF NOT EXISTS TwoGs;

USE TwoGs;

CREATE TABLE IF NOT EXISTS Torneos (
    ID INTEGER NOT NULL UNIQUE,
    Nombre TEXT,
    Sede TEXT,
    Fecha TEXT,
    Premio NUMERIC,
    Categoria TEXT,
    PRIMARY KEY(ID)
);

CREATE TABLE IF NOT EXISTS Equipos (
    ID INTEGER NOT NULL UNIQUE,
    Nombre TEXT,
    Región TEXT,
    Titulos_Mundiales INTEGER,
    Titulos_Regionales INTEGER,
    Categoría INTEGER,
    PRIMARY KEY(ID)
);

CREATE TABLE Jugadores (
	ID	INTEGER UNIQUE,
	Nombre	TEXT,
	Nacionalidad	BLOB,
	Edad	INTEGER,
	Rol	TEXT,
	IDEquipo	INTEGER,
	PRIMARY KEY(ID AUTOINCREMENT),
	FOREIGN KEY(IDEquipo) REFERENCES Equipos(ID)
)