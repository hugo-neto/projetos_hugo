/*Lembrar que:
Caso haja um banco de dados com 70% F e 30% RJ num condicional OR
Colocar primeiro S = ‘F’ OR UF = ‘RJ’ para economizar performance.
Ele busca o maior que fica Verdade e depois vai para o menor e isso 
evita um processo duplo.
Para o AND a lógica é inversa
*/

/*
create table funcionarios
  (
      idFuncionario integer,
      nome varchar(100),
      email varchar(200),
      sexo varchar(10),
      departamento varchar(100),
      admissao varchar(10),
      salario integer,
      cargo varchar(100),
      idRegiao int
  );
*/
use exercicio;
/*Trazer todos os funcionários 
do departamento de filmes ou roupas*/

SELECT * FROM funcionarios;

/*Contando itens do departamento (975)*/
SELECT COUNT(*) as 'TOTAL' 
FROM funcionarios; 

/*Contando número departamento Filmes (21) 2,15%*/
SELECT departamento, COUNT(*) AS 'Nº departamento filmes'
FROM funcionarios WHERE departamento = 'Filmes'
GROUP BY departamento;

/*Contando número departamento rouas (53) 5,44%*/
SELECT departamento, COUNT(*) AS 'Nº departamento roupas'
FROM funcionarios WHERE departamento = 'Roupas'
GROUP BY departamento;

/*Contando número departamento lar (52) 5,33%*/
SELECT departamento, COUNT(*) AS 'Nº departamento Lar'
FROM funcionarios WHERE departamento = 'Lar'
GROUP BY departamento;

/*Forma otimizada*/
SELECT nome FROM funcionarios
WHERE departamento = 'Roupas' OR departamento = 'Filmes';

/*Forma não otimizada*/
SELECT nome FROM funcionarios
WHERE departamento = 'Filmes' OR departamento = 'Roupas';

/*
Lista funcionários departamento filme ou lar.
Ele necessita enviar um e-mail para esses dois setores
*/

/*Forma otimizada*/
SELECT nome FROM funcionarios
WHERE departamento = 'Lar' OR departamento = 'Filmes';

/*Traga os funcionários do sexo feminino ou aqueles 
que trabalham no setor jardim*/

/*Contando itens do departamento (975)*/
SELECT COUNT(*) as 'TOTAL' 
FROM funcionarios; 

/*Contando número departamento Jardim (47) 4,82%*/
SELECT departamento, COUNT(*) AS 'Nº departamento Jardim'
FROM funcionarios WHERE departamento = 'Jardim'
GROUP BY departamento;

/*Contando número de mulheres (491) 50,36%*/
SELECT sexo, COUNT(*) AS 'Nº mulheres'
FROM funcionarios WHERE sexo = 'Feminino'
GROUP BY sexo;

/*Forma otimizada*/
SELECT nome FROM funcionarios
WHERE sexo = 'Feminino' OR departamento = 'Jardim' ;
