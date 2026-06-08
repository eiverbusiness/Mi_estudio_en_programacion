CREATE DATABASE ejercicio;

USE ejercicio;

CREATE TABLE estudiantes(
    cedula INT,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    numero_celular INT
);

ALTER TABLE estudiantes
ADD COLUMN edad;

INSERT INTO estudiantes(cedula, nombre, apellido, numero_celular, edad)

VALUES
(30268661,'Eiver Renier','Valencia Torres',04128646405,25),
(30064722,'Eliana Cristina','Salazar Carrillo',0424-6196021,23),
(31134280,'Moises David','Muñoz Ferrer',0412-0500345,22),
(32554190,'Andres Felipe', 'Barros Riascos',0414-9680127,20),
(32964420,'Jean Paul', 'Godoy Colina', 0412-7232529,18),
(33127878,'Oscar Enrique','Palmar Fonseca',0424-6576978,19);


SELECT * FROM estudiantes
WHERE edad > 20

SELECT * FROM estudiantes
WHERE cedula = 30268661 AND edad = 23;