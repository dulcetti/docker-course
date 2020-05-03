create database email_sender;

\c email_sender

CREATE TABLE emails (
  id serial not null,
  data TIMESTAMP not null default current_timestamp,
  assunto VARCHAR(100) not null,
  mensagem VARCHAR(250) not null
);