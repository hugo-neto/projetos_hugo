/*Antes de deletar faça um count(*)*/
SELECT COUNT(*) FROM TABELA
WHERE NOME = 'ANA';

/*Fazendo o DELETE. Lemnre-se de usar a condição!*/
DELETE FROM CLIENTE
WHERE NOME='ANA'
AND EMAIL = 'ANA@GMAIL.COM';
