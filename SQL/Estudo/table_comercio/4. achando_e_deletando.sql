/*Inserindo dado
INSERT INTO CLIENTE VALUES(NULL, 'HUGO NETO', 'M', 'HUGO2@GMAIL.COM', 12345678901);
*/

/*Confirmando o dado a ser deletado*/
SELECT * FROM CLIENTE;

/*Deletando com base no IDCLIENTE identificado acima*/
DELETE FROM CLIENTE WHERE IDCLIENTE = 12;
