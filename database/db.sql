drop database db_chaka;

create database db_chaka;

use db_chaka;

drop TABLE usuario;
CREATE TABLE usuario (
  codigo int(5) NOT NULL primary key auto_increment,
  nombre varchar(50) NOT NULL,
  usuario varchar(50) NOT NULL UNIQUE KEY,
  correo varchar(50) NOT NULL,
  clave varchar(50) NOT NULL,
  tipo varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

insert into usuario(nombre,usuario,correo,clave,tipo)
values ('Noe','noeSalva','noe.salvatierra@utec.edu.pe','123','cliente');
insert into usuario(nombre,usuario,correo,clave,tipo)
values ('Maria','mariaGracias','maria.neira@upc.edu.pe','123','productora');

drop TABLE producto;
CREATE TABLE producto (
  idproducto int(5) NOT NULL primary key auto_increment,
  idproductor int(5) NOT NULL,
  categoria varchar(45) NOT NULL,
  precio double(6,2) NOT NULL,
  stock int(5) NOT NULL,
  descripcion varchar(500) NOT NULL,
  valoracion varchar(45) NOT NULL,
  imagen varchar(45) NOT NULL,
  titulo varchar(45) NOT NULL
);

insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'organico',3.0, 10 ,'Maiz frito con bajas calorias. Proveniente de Huancayo','4','cancha_serrana.png','Cancha Warmi 100% organico');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'textil',45.0, 45,'Esta chompa ha sido tejida con lana finamente seleccionada por personas intruidas en el area de textileria. Manos artesanas perfectamente cuidadas han hecho estas prendas','4','chompa_tejida.png','Chompa tejida a mano marca Sol Alpaca ');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'textil',52.0, 77,'El poncho de alpaca se caracteriza por su suavidad y ligereza. De esta forma, ya no te preocuparas por el frio','4','poncho_alpaca.png','Poncho de Alpaca');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'textil',12.0, 43,'Este chullo viene desde el lugar mas recondito de huancayo, elaborado con lana de cuy','4','chullo_huancayo.png','Chullo Huancaino');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'textil',96.0, 14,'Chalina tejida a mano y elaborada es Ayacucho. Por la compra de un producto damos trabajo a muchos artesanos','4','chalina_alpaca.png','Chalina Alpaca');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'textil',20.0, 18,'Bello conjunto de lana con hermosos bordados piuranos','4','conjunto1_alpaca.png','Conjunto de lana');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'textil',96.0, 35,'Suave chalina con acabados de lujo, directo de Cuzco a tu casa.','4','chalina_guanaco.png','Chalina de baby alpaca');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'textil',47.0, 12,'Suaves y deliciosos brownies con cacao de Chanchamayo.','4','happy_brownies.png','Brownies hechos de cacao y menta organica');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'textil',54.0, 5,'Chompa con patrones incaicos, fabricada con lana de alpaca de alta calidad.','4','chompa_inca.png','Chompa inspirado en patrones Incaicos');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'textil',35.0, 1,'Sopa con sabor a cuy y pequenos trozos de carne. Muy deliciosa para que la disfrutes en tu hogar.','4','maruchan.png','Sopa Instantanea sabor a cuy');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'textil',45.0, 4,'Chifles piuranos con un muy rico sabor, de Piura a tu casa','4','chifles_piurano.png','Chifles Piuranos');
insert into producto(idproductor,categoria,precio,stock,descripcion,valoracion,imagen,titulo)
values ( 2 ,'artesania',32.0, 1,'Este torito tiene una gran leyenda detrás de su arte, esperamos que te proteja y te de buena fortuna.','5','torito.png','Torito de Pucara');




CREATE TABLE  lista(
  idlista int(5) NOT NULL primary key auto_increment,
  idproducto int(5) NOT NULL,
  idusuario int(5) NOT NULL
);




insert into lista(idproducto,idusuario)
values (3,5)


