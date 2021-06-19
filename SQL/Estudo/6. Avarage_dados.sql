/*Seleciona a base de dados*/
use exercicio;

/*Escolhe a coluna comparativa
e a coluna com o valor médio
a ser calculado*/
SELECT sexo, AVG(salario)
FROM funcionarios
GROUP BY sexo
ORDER BY sexo;
