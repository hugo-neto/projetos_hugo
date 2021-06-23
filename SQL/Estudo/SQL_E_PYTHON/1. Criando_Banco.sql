/*PK auto incrementada e não nula
Até 5 dígitos com 2 sendo da vírgula
Chave primária é o id
nome, sigla não precisam se relacionar
*/

CREATE DATABASE estados(

id INT UNSIGNED NOT NULL AUTO_INCREMENT,

nome VARCHAR(45) NOT NULL,

sigla CHAR(2) NOT NULL,

regiao ENUM('RJ', 'SP', 'MG', 'ES', 'RS') NOT NULL,

populacao DECIMAL(5,2) NOT NULL,

primary key (id),

unique key (nome)
unique key (sigla)
);

-- Consultando em tabela com ordem crescente
SELECT *
FROM estados
WHERE regiao = 'RJ'
ORDER BY nome;

-- Consultando em tabela com ordem decrescente
SELECT *
FROM estados
WHERE regiao = 'RJ'
ORDER BY nome DESC;
