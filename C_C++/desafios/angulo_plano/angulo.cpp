#include <stdlib.h>
#include <stdio.h>
#include <math.h>

/*Função que calcula o ângulo entre uma reta
e o eixo x no primeiro quadrante de um plano
cartesino
LINK REFERÊNCIA:
https://www.ime.usp.br/~macmulti/exercicios/funcoes1/index.html 

Questão 4-c do link (POLI 97)

PS: Por algum motivo que eu não sei
só funcionou em .cpp :(

*/

float arctan(float valor){
    int k, n = 0;
    k = k * 2 + 1;
    float total = 0, termo = pow(valor,k)/k;
    
    while(termo > 0.0001){
        total = total + ((pow(-1,n))*termo);
        n++;
        k = 2*n + 1;
        termo = pow(valor,k)/k;
    }
    
    return total;
}


int main(){

    float x, y;

    printf("\nDigite o valor de x:");
    scanf("%f", &x);
    printf("\nDigite o valor de y:");
    scanf("%f", &y);

    while((x < 0)||(y < 0)){
        printf("\nValor de x ou y digitados errôneamente. \nSó aceitamos >= 0...");
        
        printf("\nDigite o valor de x:");
        scanf("%f", &x);
        printf("\nDigite o valor de y:");
        scanf("%f", &y);
    }

    if (y < x){
        float termo =  y / x;
        printf("O ângulo é: %.4f radianos", arctan(termo));
    }
    else {
        float termo =  x / y;
        printf("O ângulo é: %.4f radianos", 3.14/2 - arctan(termo));
    }

    return 0;
}
