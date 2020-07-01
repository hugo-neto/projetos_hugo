LINK: https://www.urionlinejudge.com.br/judge/pt/problems/view/1090

Set é um jogo jogado com um baralho no qual cada carta pode ter uma, duas ou três figuras. Todas as figuras em uma carta são iguais, e podem ser círculos, quadrados ou triângulos. Um set é um conjunto de três cartas em que, para cada característica (número e figura), ou as três cartas são iguais, ou as três cartas são diferentes.

Por exemplo, na figura abaixo, (a) é um set válido, já que todas as cartas têm o mesmo tipo de figura e todas elas têm números diferentes de figuras. Em (b), tanto as figuras quanto os números são diferentes para cada carta. Por outro lado, (c) não é um set, já que as duas últimas cartas têm a mesma figura, mas esta é diferente da figura da primeira carta.


O objetivo do jogo é formar o maior número de sets com as cartas que estão na mesa; cada vez que um set é formado, as três cartas correspondentes são  removidas de jogo. Quando há poucas cartas na mesa, é fácil determinar o maior número de sets que podem ser formados; no entanto, quando há muitas cartas há muitas  combinações possíveis. Seu colega quer treinar para o campeonato mundial de Set, e por isso pediu que você fizesse um programa que calcula o maior número de sets que podem ser formados com um determinado conjunto de cartas.
Entrada

A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (3 ≤ N ≤ 3 x 104), indicando o número de cartas na mesa; cada uma das N linhas seguintes contém a descrição de uma carta.

A descrição de uma carta é dada por duas palavras separadas por um espaço; a primeira palavra é "um" ou "dois"   ou "tres" e indica quantas figuras aquela carta possui. A segunda palavra é, “circulo” (ou “circulos”), “quadrado” (ou “quadrados”) ou “triangulo” (ou “triangulos”) indica qual tipo de figura está naquela carta.

O final da entrada é indicado por uma linha contendo um zero.
Saída

Para cada caso de teste da entrada seu programa deve imprimir uma única linha na saída, contendo um número inteiro, indicando o maior número de sets que podem ser formados com as cartas dadas.
Exemplo de Entrada 	Exemplo de Saída

3
um circulo
dois circulos
tres circulos
Saída = 1

3
um triangulo
tres quadrados
dois circulos
Saída = 1

6
dois quadrados
dois quadrados
dois quadrados
dois quadrados
dois quadrados
dois quadrados
Saída = 2

4
um quadrado
tres triangulos
um quadrado
dois triangulos
Saída = 0
