USE PROJETO;

/*Atualizando linhas com cliente = null
Elas já foram identificadas previamente*/
UPDATE CLIENTE
SET EMAIL = 'JORGE@GMAIL.COM'
WHERE NOME = 'JORGE';

/*Lembrando que:
UPDATE TABELA
SET COLUNA = 'VALOR'
Muda a coluna inteira com 
esse valor!!!

SEMPRE USE O WHERE!!
*/

UPDATE CLIENTE
SET EMAIL = 'LILIAN@GMAIL.COM'
WHERE NOME = 'LILIAN';
