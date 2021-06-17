/* Comentário */
/* Seleciona o Banco de Dados treino */
use treino;

/* Cria uma tabela clientes */

CREATE TABLE CLIENTE (
	NOME VARCHAR(45),
    SEXO CHAR(1),
    EMAIL VARCHAR(45),
    CPF INT(11),
    TELEFONE VARCHAR(30)
);

DESC CLIENTE;
