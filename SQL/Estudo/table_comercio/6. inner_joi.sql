/*Função IFNULL() escolhe item null no campo C.EMAIL e 
retorna ********** se for nulo*/

SELECT C.NOME,
        IFNULL(C.EMAIL, '************') AS 'E-MAIL',
        E.ESTADO,
        T.NUMERO
FROM CLIENTE C
INNER JOIN ENDERECO E
ON C.IDCLIENTE = E.ID_CLIENTE
INNER JOIN TELEFONE T
ON C.IDCLIENTE = T.ID_CLIENTE;
