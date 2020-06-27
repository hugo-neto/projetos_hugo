#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sobe_desce(int *ponteiro_z, int condicao){
    if (condicao == 1){
        *ponteiro_z = *ponteiro_z + 1;
    }
    
    else{
        *ponteiro_z = *ponteiro_z - 1;
    }
}

void direciona_r(int *dirPtr){
    if (*dirPtr == 3)
        *dirPtr = 0;
    else
        *dirPtr = *dirPtr + 1;
}

void direciona_l(int *dirPtr){
    if (*dirPtr == 0)
        *dirPtr = 3;
    else
        *dirPtr = *dirPtr - 1;
}

void move(int direcao[4]){
    switch (direcao[3])
    {
    case 0:
        direcao[1] = direcao[1] + 1;
        break;
    
    case 1:
        direcao[0] = direcao[0] + 1;
        break;
    
    case 2:
        direcao[1] = direcao[1] - 1;
        break;
    
    case 3:
        direcao[0] = direcao[0] - 1;
        break;
    
    default:
        break;
    }
}

void printa_vetor(int posicao[4]){
    char *direcao[4] = {"NORTE", "LESTE", "SUL", "OESTE"};
    int k;

    switch (posicao[3]){
    case 0:
        //direcao[0] = "NORTE";
        k = 0;
        break;
    
    case 1:
        //direcao[0] = "LESTE";
        k = 1;
        break;
    
    case 2:
        //direcao[0] = "SUL";
        k = 2;
        break;
    
    case 3:
        //direcao[0] = "OESTE";
        k = 3;
        break;
    
    default:
        break;
    }
    printf("\n");
    printf("Posicao x: %d\nPosicao y: %d\nPosicao z: %d\nDireção: %s\n", posicao[0], posicao[1], posicao[2], direcao[k]);
    printf("\n");

}

int main(){
    int j = 1, i = 0;
    int posicao[4] = {0,0,0,0};
    char n, c, comandos[255];

    puts("Digite os comandos abaixo: ");

    while((c = getchar()) != '\n'){
        comandos[++i] = c;
    }
    comandos[i+1] = '\0';
    
    while(comandos[j] != '\0'){
        n = tolower(comandos[j]);
        j++;
        switch (n){
        case 'u':
            sobe_desce(&posicao[2], 1);
            break;
        
        case 'd':
            sobe_desce(&posicao[2], 0);
            break;

        case 'r':
            direciona_r(&posicao[3]);
            break;

        case 'l':
            direciona_l(&posicao[3]);
            break;

        case 'm':
            move(posicao);
            break;

        default:
            printf("\nEntrou no dedault");
            break;
        }
    }

    printa_vetor(posicao);

    return 0;
}
