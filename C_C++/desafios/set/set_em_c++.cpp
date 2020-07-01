#include <iostream>
#include <string>
#include <new>

using namespace std;

struct carta{
    string numero;
    string figura;
};

void deleta(carta *&pointEncadeado, int cont1, int cont2, int *total, int *totalSet){
    int indice = 0;
    carta *novoPoint = new carta [*total-3];
    
    for (int i = 0; i < cont1-1; i++){
        novoPoint[indice].numero = pointEncadeado[i+1].numero;
        novoPoint[indice].figura = pointEncadeado[i+1].figura;
        indice++;
    }
    
    for (int j = cont1; j < cont2-1; j++){
        novoPoint[indice].numero = pointEncadeado[j+1].numero;
        novoPoint[indice].figura = pointEncadeado[j+1].figura;
        indice++;
    }
    
    pointEncadeado = novoPoint;
    *total = *total - 3;
    *totalSet = *totalSet + 1;
    
}

void avalia (carta *&pointEncadeado, int *total, int *totalSet){
    for (int i = 1; i < *total; i++){
        if (pointEncadeado[0].figura == pointEncadeado[i].figura){
            if (pointEncadeado[0].numero == pointEncadeado[i].numero){
                for (int j = i + 1; j < *total; j++){
                    if((pointEncadeado[0].figura == pointEncadeado[j].figura) && (pointEncadeado[0].numero == pointEncadeado[j].numero)){
                        deleta(pointEncadeado, i, j, total, totalSet);
                    }
                }
            }
            
            else if (pointEncadeado[0].numero != pointEncadeado[i].numero){
                for (int j = i + 1; j < *total; j++){
                   if((pointEncadeado[0].figura == pointEncadeado[j].figura) && (pointEncadeado[0].numero != pointEncadeado[j].numero) && (pointEncadeado[0].numero != pointEncadeado[i].numero)){
                       deleta(pointEncadeado, i, j, total, totalSet);
                   }
                }
            }
        }

        else if ((pointEncadeado[0].figura != pointEncadeado[i].figura) && (pointEncadeado[0].numero != pointEncadeado[i].numero)){
            for (int j = i + 1; j < *total; j++){
                if((pointEncadeado[0].figura != pointEncadeado[i].figura) && (pointEncadeado[0].figura != pointEncadeado[j].figura) && (pointEncadeado[0].numero != pointEncadeado[i].numero) && ((pointEncadeado[0].numero != pointEncadeado[j].numero))){
                    deleta(pointEncadeado, i, j, total, totalSet);
                }
            }
        }
    }
    
}

void adiciona(carta *&pointEncadeado, string numero, string figura, int *cont, int *totalSet){
    
    *cont = *cont + 1;
    carta *outraLista = new carta [*cont];
    outraLista[*cont-1].numero = numero;
    outraLista[*cont-1].figura = figura;
    
    for (int i = 0; i < *cont-1; i++){
        outraLista[i].numero = pointEncadeado[i].numero;
        outraLista[i].figura = pointEncadeado[i].figura;
    }
    
    pointEncadeado = outraLista;
    
    if (*cont >= 3){
        avalia(pointEncadeado, cont, totalSet);
    }
}

void adiciona_primeiro(carta *&pointEncadeado, string numero, string figura, int *cont){

    carta *primCarta = new carta[1];
    *cont = *cont + 1;
    primCarta[0].numero = numero;
    primCarta[0].figura = figura;
    pointEncadeado = primCarta;
    
}

int main(){
    int n;
    string usuario, num_u;
    
    cin >> n;
    while (n != 0){
        int cont = 0, total_set=0;
        carta *pointEncadeado;
        carta *primeiraCarta = new carta[1];
        pointEncadeado = primeiraCarta;
        
        for(int i = 0; i < n+1; i++){
            cout << "";
            getline (cin,usuario);
            cout << "";

            switch (usuario[0]){
            case 'u':
                num_u = usuario.substr(0,3);
                usuario = usuario.replace(0,3,"");
                if(cont == 0){
                    adiciona_primeiro(pointEncadeado, num_u, usuario, &cont);
                }
                else {
                    adiciona(pointEncadeado, num_u, usuario, &cont, &total_set);
                }
                break;

            case 'd':
                num_u = usuario.substr(0,5);
                usuario = usuario.replace(0,5,"");
                usuario.pop_back();
                if(cont == 0){
                    adiciona_primeiro(pointEncadeado, num_u, usuario, &cont);
                }
                else {
                    adiciona(pointEncadeado, num_u, usuario, &cont, &total_set);
                }
                break;

            case 't':
                num_u = usuario.substr(0,5);
                usuario = usuario.replace(0,5,"");
                usuario.pop_back();
                if(cont == 0){
                    adiciona_primeiro(pointEncadeado, num_u, usuario, &cont);
                }
                else {
                    adiciona(pointEncadeado, num_u, usuario, &cont, &total_set);
                }
                break;
            }
        }
        cout << total_set <<endl;
        cin >> n;
    }
    
    return 0;
}
