CREATE DATABASE COMERCIO;

USE COMERCIO;

/*Tabela que será a referenciada*/
CREATE TABLE CLIENTE (
	IDCLIENTE INT PRIMARY KEY AUTO_INCREMENT,
    NOME VARCHAR(45) NOT NULL,
    SEXO ENUM('M', 'F') NOT NULL,
    EMAIL VARCHAR(45) UNIQUE,
    CPF CHAR(11) UNIQUE
);

/*1 - 1 com CLIENTE*/
CREATE TABLE ENDERECO (
	IDENDERECO INT PRIMARY KEY AUTO_INCREMENT,
    RUA VARCHAR(45) NOT NULL,
    BAIRRO VARCHAR(45) NOT NULL,
    CIDADE VARCHAR(45) NOT NULL,
    ESTADO CHAR(2) NOT NULL,
    /*UNIQUE porque é relação 1 -1*/
    ID_CLIENTE INT UNIQUE,
    FOREIGN KEY (ID_CLIENTE)
    /*TABELA(CAMPO/COLUNA)*/
    REFERENCES CLIENTE(IDCLIENTE)
);

/*1 - N com CLIENTE*/
CREATE TABLE TELEFONE (
	IDTELEFONE INT PRIMARY KEY AUTO_INCREMENT,
    TIPO ENUM('CEL', 'RES', 'COM'),
    NUMERO VARCHAR(12) NOT NULL,
    /*sem UNIQUE porque é relação 1 -N*/
    ID_CLIENTE INT,
    FOREIGN KEY (ID_CLIENTE)
    REFERENCES CLIENTE(IDCLIENTE)
);
