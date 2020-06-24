def salva_valores(posicao, inicio):
    try:
        # Acessa o arquivo existente e escreve na parte de baixo
        arquivo = open("resultados.txt", "a")
        arquivo.write(f"\nInício: {inicio} Fim {tuple(posicao)}")
        arquivo.close()

    # Se o arquivo não existir, ele cria um novo
    except NameError as f:
        with open("resultados.txt", "w") as novo:
            print(f"\nInício: {inicio} Fim {tuple(posicao)}", file=novo)

    # Provável erro de digitação do usuário
    except Exception as e:
        print(f"ERRO NÃO FATAL! {str(e)}")
        print("\nProgama continuou sua execução normalmente!\n")
