class Controle:
    def __init__(self):
        return

    def criar_BD(self):
        info = open('veicul.txt', 'r')
        veiculos = info.readlines()
        info.close()

        BancoDeDados = []

        for l in veiculos[1:]:
            l = l.strip() 
            tokens = l.split() 
            BancoDeDados.append(tokens)

            # falta transformar em objetos, chamando as classes Carros, Vans e a outra
            # e chamando o metodo adicionar delas
            # antes fazer algo p identificar qual deve ser chamada
        return BancoDeDados

    
