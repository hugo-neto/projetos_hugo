/* Projeção de colunas que não existem em CLIENTE*/
SELECT NOW() as DATA_HORA, 'HUGO' as Professor;

SELECT NOME, SEXO, EMAIL, ENDERECO FROM CLIENTE;

/*Projeta a coluna NOME como CLIENTE
usando sintaxe COLUNA AS NOME_DESEJADO*/
SELECT NOME AS CLIENTE, SEXO, EMAIL FROM CLIENTE;

/*SOMENTE PARA FINS ACADÊMICOS
MOSTRA TUDO!!*/
SELECT * FROM CLIENTE

/*Projeta tabelas que existem e não existem no banco*/
SELECT EMAIL, SEXO, ENDERECO, NOME, NOW() AS DATA_HORA FROM CLIENTE;

