/*Comandos do tipo DDL Data Definition Language
nome_da_coluna novo_nome 
*/

ALTER TABLE CLIENTE
CHANGE PRECO VALOR_UNITARIO INT NOT NULL

/*Não necessita indicar o que vai ser alterado
Só muda o tipo dos dados de certa coluna*/
ALTER TABLE CLIENTE
MODIFY VALOR_UNITARIO INT NOT NULL

/*Adiciona uma coluna*/
ALTER TABLE CLIENTE
ADD PESO FLOAT(10,2) NOT NULL

/*Deleta uma coluna inteira*/
ALTER TABLE PRODUTO
DROP COLUMN PESO

/*Adiciona em local específico (depois da coluna nome)*/
ALTER TABLE PRODUTO
ADD COLUMN PESO FLOAT(10,2) NOT NULL
AFTER NOME_PRODUTO

/*Adiciona em local específico (início!)*/
ALTER TABLE PRODUTO
ADD COLUMN PESO FLOAT(10,2) NOT NULL
FIRST
