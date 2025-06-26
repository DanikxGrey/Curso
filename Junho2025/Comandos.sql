create database cadastro
default character set utf8mb4
collate utf8mb4_general_ci;

use cadastro;

create table pessoas(
id int primary key not null auto_increment,
nome varchar(30) not null,
nascimento date,
sexo enum ('M', 'F'),
peso decimal (5,2),
altura decimal (3,2),
nacionalidade varchar(20)
)
engine=innodb default charset=utf8mb4;

insert into pessoas values
(default, 'Ana', '1975-12-22', 'F', '52.3', '1.45', 'EUA'),
(default, 'Maria', '1999-05-30', 'F', '75.8', '1.70', 'Portugal'),
(default, 'Wanderly', '1968-02-04', 'M', '73.2', '1.72', 'Brasil');

select * from pessoas;

alter table pessoas
add column profissao varchar (10);

-- abaixo o describe simplificado para descrever 

desc pessoas;

alter table pessoas 
drop column profissao;

desc pessoas;

alter table pessoas
change column profissao prof varchar(20);
-- Pra renomear o nome primeiro se refere ao nome atual (profissao) e o nome que vai substituir ele (prof)
