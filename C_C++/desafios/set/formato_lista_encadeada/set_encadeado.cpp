#include <iostream>
#include <string>
#include <new>
#include <stdlib.h>

//Agora a set8 é versão a otimizada

using namespace std;

struct carta{
    string numero;
    string figura;
    struct carta *proximo;
};

void deleta(carta *&pointEncadeado, int cont1, int cont2, int *total){
    pointEncadeado = pointEncadeado->proximo;
    carta *p;

    if (cont1 == 1){
        pointEncadeado = pointEncadeado->proximo;
        p = pointEncadeado;
    }
    else{
        p = pointEncadeado;
        for (int i = 1; i < cont1; i++){
            p = p->proximo;
        }
        carta *auxiliar = new carta;
        auxiliar = p->proximo;
        p->proximo = auxiliar->proximo;
        free(auxiliar);
    }

    for(int j = cont1 + 1; j < cont2; j++){
        p = p->proximo;
    }
    if (p->proximo == NULL)
        p = NULL;
    else{
        carta *auxiliar2 = new carta;
        auxiliar2 = p->proximo;
        p->proximo = auxiliar2->proximo;
        free(auxiliar2);
    }

    free(p);
    *total = *total - 3;

}

void avalia (carta *pointEncadeado, int *total, int *totalSet){
    string fig_1, fig_2, num_1, num_2;
    int cont1 = 0, cont2;
    carta *p = pointEncadeado;
    
    fig_1 = p->figura;
    num_1 = p->numero;
    p = p->proximo;
    cont1++;

    while (p != NULL){
        if (fig_1 == p->figura){
            if(num_1 == p->numero){
                cont2 = cont1 + 1;
                fig_2 = p->figura;
                num_2 = p->numero;
                p = p->proximo;
                
                while(p != NULL){
                    if((fig_1 == p->figura) && (num_1 == p->numero)){
                        *totalSet = *totalSet + 1;
                        deleta(pointEncadeado, cont1, cont2, total);
                    }
                    p = p->proximo;
                    cont2++;
                }
            }
            
            else if(num_1 != p->numero){
                cont2 = cont1 + 1;
                fig_2 = p->figura;
                num_2 = p->numero;
                p = p->proximo;

                while(p != NULL){
                    if((fig_1 == p->figura) && (num_2 != p->numero) && (num_1 != p->numero)){
                        *totalSet = *totalSet + 1;
                        deleta(pointEncadeado, cont1, cont2, total);
                    }
                    p = p->proximo;
                    cont2++;
                }
            }
        }
        
        else if((fig_1 != p->figura) && (num_1 != p->numero)){
            cont2 = cont1 + 1;
            fig_2 = p->figura;
            num_2 = p->numero;
            p = p->proximo;

            while (p != NULL){
                if ((fig_1 != p->figura) && (fig_2 != p->figura) && (num_1 != p->numero) && (num_2 != p->numero)){
                    *totalSet = *totalSet + 1;
                    deleta(pointEncadeado, cont1, cont2, total);
                }
                p = p->proximo;
                cont2++;
            }
        }
        if(p == NULL)
            break;
        else{
            p = p->proximo;
            cont1++;
        }
    }   
}

void adiciona(carta *&pointEncadeado, string numero, string figura, int *cont, int *totalSet){
    
    carta *ultimoTermo = new carta;
    ultimoTermo->numero = numero;
    ultimoTermo->figura = figura;
    ultimoTermo->proximo = NULL;

    *cont = *cont + 1;
    carta *auxPoint = pointEncadeado;

    while (auxPoint != NULL){
        if (auxPoint->proximo == NULL){
           auxPoint->proximo = ultimoTermo;
           break; 
        }
        auxPoint = auxPoint->proximo;
    }

    if (*cont >= 3)
        avalia(pointEncadeado, cont, totalSet);
    
}

void adiciona_primeiro(carta *&pointEncadeado, string numero, string figura, int *cont){

    carta *primCarta = new carta;
    *cont = *cont + 1;
    primCarta->numero = numero;
    primCarta->figura = figura;
    pointEncadeado = primCarta;
    
}

int main(){
    int n;
    string usuario, num_u;
    
    cin >> n;
    while (n != 0){
        int cont = 0, total_set=0;
        carta *pointEncadeado;
        carta *primeiraCarta = new carta;
        pointEncadeado = primeiraCarta;
        
        for(int i = 0; i < n+1; i++){
            cout << "";
            getline (cin,usuario);
            cout << "";            

            switch (usuario[0]){
            case 'u':
                num_u = usuario.substr(0,3);
                usuario = usuario.replace(0,3,"");
                if(cont == 0)
                    adiciona_primeiro(pointEncadeado, num_u, usuario, &cont);
                else 
                    adiciona(pointEncadeado, num_u, usuario, &cont, &total_set);
                break;

            case 'd':
                num_u = usuario.substr(0,5);
                usuario = usuario.replace(0,5,"");
                usuario.pop_back();
                if(cont == 0)
                    adiciona_primeiro(pointEncadeado, num_u, usuario, &cont);
                else 
                    adiciona(pointEncadeado, num_u, usuario, &cont, &total_set);
                break;

            case 't':
                num_u = usuario.substr(0,5);
                usuario = usuario.replace(0,5,"");
                usuario.pop_back();
                if(cont == 0)
                    adiciona_primeiro(pointEncadeado, num_u, usuario, &cont);
                else 
                    adiciona(pointEncadeado, num_u, usuario, &cont, &total_set);
                break;
            }
        }
        cout << total_set <<endl;
        cin >> n;
    }
    
    return 0;
}
