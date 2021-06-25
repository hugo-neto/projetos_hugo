/*Há uma espécie de intersecção entre
dois conjuntos (ou tbm chamado tabela)*/

SELECT NOME, SEXO, BAIRRO, CIDADE
FROM CLIENTE
INNER JOIN ENDERECO
ON IDCLIENTE = ID_CLIENTE
WHERE SEXO = 'F';
