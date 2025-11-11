create database danikx; 

use danikx;
create table agendamento(
id int auto_increment primary key,
nome varchar (100) not null,
cpf varchar (30) not null,
idade int (99) not null,
data date not null
);