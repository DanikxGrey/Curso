create table agendamentos(
id int auto_increment primary key,
nome varchar (100) not null,
telefone varchar(20) not null,
aparelho varchar(50) not null,
data date not null,
descricao text not null,
data_envio timestamp default current_timestamp
);