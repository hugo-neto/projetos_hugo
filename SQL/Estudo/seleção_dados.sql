/**/
use PROJETO;

SELECT NOME, SEXO FROM CLIENTE
WHERE SEXO = 'M';

SELECT NOME, ENDERECO FROM CLIENTE
WHERE SEXO = 'F';

SELECT NOME, SEXO FROM CLIENTE
WHERE ENDERECO = 'RJ';

/* UTILIZANDO O LIKE */

SELECT NOME, SEXO FROM CLIENTE
WHERE ENDERECO LIKE 'RJ';

/*% é um coringa
%RJ = Começa com qualquer coisa mas
termina com RJ
ou
OSCAR CURI% = Começa OSCAR CURI
termina qualquer coisa
ou
%TEXTO% = Começa e termina qualquer coisa
%___TEXTO___% = Começa com qualquer coisa
limitada a um número de caracter 
( determinado pelo _)
*/

SELECT NOME, SEXO, ENDERECO FROM CLIENTE
WHERE ENDERECO LIKE '%RJ';
