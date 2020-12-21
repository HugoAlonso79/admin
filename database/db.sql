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
