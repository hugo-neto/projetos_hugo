/*use livraria;*/

/*Contando o número de registro de uma tabela*/
SELECT COUNT(*) AS "Registros Livraria" FROM LIVROS;

/*Contando o número de registro de uma tabela
em outra base de dados*/
SELECT COUNT(*) AS "Registros Treino" FROM treino.CLIENTE;

/*Sem a ação group by ele entrega o número de registros
da função count e a primeira linha da coluna SEXO*/
SELECT SEXO, COUNT(*) 
FROM LIVROS 
GROUP BY SEXO;
