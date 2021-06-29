
use teste;

/*Muda o delimitador*/
DELIMITER GO

/*Cria uma nova procedure
procedure = funcao*/
CREATE PROCEDURE FUNCOES()
BEGIN

	SELECT * FROM funcionarios;

END
GO

DELIMITER ;

DELIMITER GO

/*Cria uma nova procedure*/
CREATE PROCEDURE SOMA(NUMERO1 INT, NUMERO2 INT)
BEGIN

	SELECT NUMERO1 + NUMERO2 AS 'RESULTADO_SOMA';

END
GO

DELIMITER ;

/*CHAMANDO
*/

/*Para apagar uma procedure não é necessário colocar entre parênteses*/
DROP PROCEDURE SOMA;
DROP PROCEDURE FUNCOES;

CALL FUNCOES();
CALL SOMA(1,2);
