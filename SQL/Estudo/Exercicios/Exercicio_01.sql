/* Acesso aos documentos:
https://drive.google.com/drive/folders/1dMd4WcS3TRD2GDpXGiSa9ZqgDPwxa9sl?usp=sharing
Seleciona o Banco de Dados treino */

/* Acesso aos documentos:
https://drive.google.com/drive/folders/1dMd4WcS3TRD2GDpXGiSa9ZqgDPwxa9sl?usp=sharing
Seleciona o Banco de Dados treino */

/*Cria uma database treino*/
CREATE DATABASE livraria;

/*Conecta o Banco de Dados*/
USE livraria;

/* Cria uma tabela clientes */
CREATE TABLE LIVROS(
	ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    NOME_DO_LIVRO VARCHAR(45),
    NOME_DO_AUTOR VARCHAR(45),
    /*
    M = Masculino
    F = Feminino
    */
    SEXO ENUM('Masculino', 'Feminino') NOT NULL,
    NUMERO_PAGINAS INT,
    NOME_EDITORA VARCHAR(25),
    VALOR_LIVRO FLOAT,
    UF CHAR(2),
    ANO_PUBLICACAO CHAR(4),
    primary key(ID)
);

/*Inserindo Valores na Base de Dados Criada*/
INSERT INTO LIVROS(NOME_DO_LIVRO, NOME_DO_AUTOR, SEXO, NUMERO_PAGINAS, NOME_EDITORA, VALOR_LIVRO, UF, ANO_PUBLICACAO) VALUES
('Cavaleiro Real',	'Ana Claudia',	'Feminino',	465,	'Atlas',	49.90,	'RJ',	'2009'),
('SQL para leigos',	'João Nunes',	'Masculino',	450,	'Addison',	98.00,	'SP',	'2018'),
('Receitas Caseiras',	'Celia Tavares',	'Feminino',	210,	'Atlas',	45.00,	'RJ',	'2008'),
('Pessoas Efetivas',	'Eduardo Santos',	'Masculino',	390,	'Beta',	78.99,	'RJ',	'2018'),
('Habitos Saudáveis',	'Eduardo Santos',	'Masculino',	630,	'Beta	',150.98,	'RJ',	'2019'),
('A Casa Marrom',	'Hermes Macedo',	'Masculino',	250,	'Bubba',	60.00,	'MG',	'2016'),
('Estacio Querido',	'Geraldo Francisco',	'Masculino',	310,	'Insignia	',100.00,	'ES',	'2015'),
('Pra sempre amigas',	'Leda Silva',	'Feminino',	510,	'Insignia',	78.98,	'ES',	'2011'),
('Copas Inesqueciveis',	'Marco Alcantara',	'Masculino',	200,	'Larson	',130.98,	'RS',	'2018'),
('O poder da mente',	'Clara Mafra',	'Feminino',	120,	'Continental',	56.58,	'SP',	'2017');                                            


/*SOMENTE PARA FINS ACADÊMICOS
MOSTRA TUDO!!*/
SELECT * FROM LIVROS;

/*Exitem as colunas selecionadas na formatação desejada*/
SELECT NOME_DO_LIVRO as 'Nome do livro', NOME_EDITORA as Editora FROM LIVROS;

/*Exitem as colunas selecionadas na formatação desejada de somente Masculino*/
SELECT NOME_DO_LIVRO as 'Nome do livro', UF as 'Unidade da Federação' FROM LIVROS
WHERE SEXO = 'Masculino';

/*Exitem as colunas selecionadas na formatação desejada de somente Feminino*/
SELECT NOME_DO_LIVRO as 'Nome do livro', NUMERO_PAGINAS as 'Número de Páginas' FROM LIVROS
WHERE SEXO = 'Feminino';

/*Exitem as colunas selecionadas na formatação e condição desejada*/
SELECT NOME_DO_LIVRO as 'Nome do livro', NUMERO_PAGINAS as 'Número de Páginas' FROM LIVROS
WHERE NUMERO_PAGINAS <= 465;

/*Exitem as colunas selecionadas na formatação desejada de somente Feminino*/
SELECT NOME_DO_LIVRO as 'Nome do livro', VALOR_LIVRO as 'Valor do Livro' FROM LIVROS
WHERE UF = 'SP';
