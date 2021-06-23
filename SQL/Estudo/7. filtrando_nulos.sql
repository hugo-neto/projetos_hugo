/*Seleciona o Data Base PROJETO*/
use PROJETO;

/*Seleciona as linhas em que o EMAIL seja nulo.
Veja que o comando é: 
EMAIL IS NULL
*/
SELECT * FROM CLIENTE WHERE EMAIL IS NULL;

/*Seleciona as linhas em que o EMAIL não seja nulo.
Veja que o comando é: 
EMAIL IS NOT NULL
*/
SELECT * FROM CLIENTE WHERE EMAIL IS NOT NULL;

