from Veiculos import *
from Veiculo import *
'''
A classe controle cria um Banco de Dados chamando a Classe Veiculos, para assim poder operar com seus metodos
'''
class Controle:
    def __init__(self):
        self.BD = Veiculos()

    '''
    O metodo criar_BD lê o arquivo txt e passa para uma lista ja organizado e separado (usando o strip e o split)
    depois disso é chamado o metodo adicionar, para criar todos os objetos e colocar no Banco De Dados. 
    '''
    def criar_BD(self):
        info = open('veiculos.txt', 'r')
        veiculos = info.readlines()
        info.close()

        BancoDD = []


        for l in veiculos:
            l = l.strip() 
            tokens = l.split() 
            BancoDD.append(tokens)
        

        for veiculos in BancoDD:
            if veiculos[0] == 'carro':
                self.BD.adicionar(veiculos[0],veiculos[1],veiculos[2],veiculos[3],veiculos[4],veiculos[5],veiculos[6],veiculos[7],veiculos[8],veiculos[9])

            elif veiculos[0] == 'van':
                self.BD.adicionar(veiculos[0],veiculos[1],veiculos[2],veiculos[3],veiculos[4],veiculos[5],veiculos[6],veiculos[7],veiculos[8],veiculos[9])

            elif veiculos[0] == 'ute':
                self.BD.adicionar(veiculos[0],veiculos[1],veiculos[2],veiculos[3],veiculos[4],veiculos[5],veiculos[6],veiculos[7],veiculos[8],veiculos[9])

        
        return

    '''
    O metodo veculDisp percorre o Banco De Dados contando quantos veiculos estão disponiveis para aluguel
    e no final retorna esse valor
    '''
    def veiculDisp(self):
        cont = 0
        for x in self.BD.BancoDeDados:
            reserva = x.getReservado()
            if reserva == False or reserva == 'False':
                cont +=1
        return cont
            
    '''
    o metodo salvarTxt deleta todo o txt de inicio e depois adiciona todos os dados que existem dentro do Banco De Dados
    '''
    def salvarTxt(self):
        arquivo = open('veiculos.txt', "r+")
        linhas = arquivo.readlines()
        arquivo.close()
        del linhas

        i = 0
        tamanho = len(self.BD.BancoDeDados)
        arquivo = open('veiculos.txt', 'w')
        while tamanho > 0:
            tipo = self.BD.BancoDeDados[i].getTipo()
            fabricante = self.BD.BancoDeDados[i].getFabricante()
            modelo = self.BD.BancoDeDados[i].getModelo()
            capacidade = self.BD.BancoDeDados[i].getCapacidade()
            autonomia = self.BD.BancoDeDados[i].getAutonomia()
            ano = self.BD.BancoDeDados[i].getAno()
            placa = self.BD.BancoDeDados[i].getPlaca()
            chassi = self.BD.BancoDeDados[i].getChassi()
            RENAVAM = self.BD.BancoDeDados[i].getRENAVAM()
            reservado = self.BD.BancoDeDados[i].getReservado()
            dados = tipo + '\t' + fabricante + '\t' + modelo + '\t' + capacidade + '\t' + autonomia + '\t' + ano + '\t' + placa + '\t' + chassi + '\t' + RENAVAM + '\t' + str(reservado) + '\n'
            arquivo.writelines(dados)
            tamanho -= 1
            i += 1

    
        return
    '''
    O metodo reservar pega a placa do carro desejado e percorre o banco de dados a procura
    quando acha realisa a operação de setReservado para trocar o status da reserva.
    '''
    def reservar(self,placa):
        tamanho = len(self.BD.BancoDeDados)
        i = 0
        while tamanho > 0:
            placaC = self.BD.BancoDeDados[i].getPlaca()
            reservado = self.BD.BancoDeDados[i].getReservado()
            if placa == placaC:
                return self.BD.BancoDeDados[i].setReservado(True)
            tamanho -= 1
            i += 1
            
        return 'não existe veiculo com essa placa'
    '''
    O metodo cancelar, usa o metodo cancelReserva da Classe Veiculos pegando a placa e trocando o status da reserva
    '''
    def cancelar(self,placa):
        return self.BD.cancelReserva(placa)
    '''
    O metodo listarCertoTipo usa o metodo veicuDisponivel da Classe Veiculos, pegando o tipo de veiculo desejado
    e retornando uma lista com todos os veiculos do tipo desejado que estão disponiveis para se alugar.
    '''
    def listarCertoTipo(self,tipo):
        return self.BD.buscar(tipo)


'''
Uma interface basica para facilitar os testes, nela quando for pedido o tipo tem que ser colocado
carro, ute ou van, para funcionar, senão o programa vai quebrar, não foi uma interface complexa
logo não foi implementado um tratamento de erros
'''
a = Controle()
continuar = True
while continuar:

    print('digite 1 para criar o banco de dados')
    print('digite 2 para buscar veiculos pela placa, chassi ou RENAVAM')
    print('digite 3 para adicionar')
    print('digite 4 para listar todos os veiculos disponiveis de um certo tipo')
    print('digite 5 para mostrar a quantidade total de veiculos disponiveis')
    print('digite 6 para reservar')
    print('digite 7 para cancelar a reserva')
    print('digite 8 para salvar do banco de dados para o txt')
    print('digite 9 para finalizar o programa')
    print('para você operar com 100% primeiro crie o banco de dados digitando 1')
    comando = input('-->')
    if comando == '1':
        a.criar_BD()
        print('se quiser fazer mais operações digite "1", caso contrario digite qualquer outro digito')
        continuação = input('-->')
        if continuação == '1':
            print(' ')
        else:
            continuar = False

    elif comando == '2':
        elemento = input('digite a placa do carro, o chassi ou o RENAVAM -->')
        print(a.BD.procurar(elemento))
        print('se quiser fazer mais operações digite "1", caso contrario digite qualquer outro digito')
        continuação = input('-->')
        if continuação == '1':
            print(' ')
        else:
            continuar = False

    elif comando == '3':
        tipo = input('coloque o tipo do veiculo -->')
        fabricante = input('coloque o fabricante do veiculo -->')
        modelo = input('coloque o modelo do veiculo -->')
        capacidade = input('coloque a capacidade do veiculo -->')
        autonomia = input('coloque a autonomia do veiculo -->')
        ano = input('coloque o ano do veiculo -->')
        placa = input('coloque a placa do veiculo -->')
        chassi = input('coloque o chassi do veiculo -->')
        RENAVAM = input('coloque o RENAVAM do veiculo -->')
        reservado = input('coloque se o veiculo está reservado ou não com "True" para sim ou "False" para não -->')
        
        a.BD.adicionar(tipo,fabricante,modelo,capacidade,autonomia,ano,placa,chassi,RENAVAM,reservado)
        print('se quiser fazer mais operações digite "1", caso contrario digite "2"')
        continuação = input('-->')
        if continuação == '1':
            print(' ')
        else:
            continuar = False

    elif comando == '4':
        tipo = input('coloque o tipo do veiculo que se deseja ver -->')
        print(a.listarCertoTipo(tipo))
        print('se quiser fazer mais operações digite "1", caso contrario digite qualquer outro digito')
        continuação = input('-->')
        if continuação == '1':
            print(' ')
        else:
            continuar = False

    elif comando == '5':
        print(a.veiculDisp())
        print('se quiser fazer mais operações digite "1", caso contrario digite qualquer outro digito')
        continuação = input('-->')
        if continuação == '1':
            print(' ')
        else:
            continuar = False

    elif comando == '6':
        placa = input('coloque a placa do veiculo desejado -->')
        a.reservar(placa)
        print('se quiser fazer mais operações digite "1", caso contrario digite qualquer outro digito')
        continuação = input('-->')
        if continuação == '1':
            print(' ')
        else:
            continuar = False

    elif comando == '7':
        placa = input('coloque a placa do veiculo desejado -->')
        a.cancelar(placa)
        print('se quiser fazer mais operações digite "1", caso contrario digite qualquer outro digito')
        continuação = input('-->')
        if continuação == '1':
            print(' ')
        else:
            continuar = False

    elif comando == '8':
        a.salvarTxt()
        print('se quiser fazer mais operações digite "1", caso contrario digite qualquer outro digito')
        continuação = input('-->')
        if continuação == '1':
            print(' ')
        else:
            continuar = False

    elif comando == '9':
        continuar = False

    else:
        comando = input('coloque novamente o comando -->')







