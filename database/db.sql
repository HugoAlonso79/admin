drop database db_chaka;

create database db_chaka;

use db_chaka;

CREATE TABLE usuario (
  codigo int(5) NOT NULL primary key auto_increment,
  nombre varchar(50) NOT NULL,
  usuario varchar(50) NOT NULL UNIQUE KEY,
  correo varchar(50) NOT NULL,
  clave varchar(50) NOT NULL,
  tipo varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

insert into usuario(nombre,usuario,correo,clave,tipo)
values ('chaka','chaka','chaka@chaka.com','123456','productor');


CREATE TABLE producto (
  idproducto int(5) NOT NULL primary key auto_increment,
  idproductor int(5) NOT NULL,
  categoria varchar(45) NOT NULL,
  precio varchar(45) NOT NULL,
  stock int(5) NOT NULL,
  descripcion varchar(500) NOT NULL,
  valoracion varchar(45) NOT NULL,
  imagen varchar(45) NOT NULL,
  titulo varchar(45) NOT NULL
);
