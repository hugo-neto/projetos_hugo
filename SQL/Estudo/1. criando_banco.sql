/* Acesso aos documentos:
https://drive.google.com/drive/folders/1dMd4WcS3TRD2GDpXGiSa9ZqgDPwxa9sl?usp=sharing

Seleciona o Banco de Dados treino */

/*Cria uma database treino*/
CREATE DATABASE treino;

/*Conecta o Banco de Dados*/
USE treino;

/* Cria uma tabela clientes */
CREATE TABLE CLIENTE (
	NOME VARCHAR(45),
    SEXO CHAR(1),
    EMAIL VARCHAR(45),
    CPF INT(11),
    TELEFONE VARCHAR(30)
);

/*Mostra todas tabelas*/
SHOW TABLES;

/*Mostra a descrição/campos da tabelas
DESC = Describe
*/
DESC CLIENTE;
