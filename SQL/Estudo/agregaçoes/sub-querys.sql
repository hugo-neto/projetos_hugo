/*Caso não haja esse where com sub-query dá ruim*/
SELECT NOME, MARCO FROM VENDEDORES
WHERE MARCO = (SELECT MIN(MARCO) FROM VENDEDORES);

SELECT NOME, MARCO FROM VENDEDORES
WHERE MARCO = (SELECT MAX(FEVEREIRO) FROM VENDEDORES);
