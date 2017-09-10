from Veiculos import *
from Veiculo import *

class Controle:
    def __init__(self):
        self.BD = Veiculos()


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

            # falta transformar em objetos, chamando as classes Carros, Vans e a outra
            # e chamando o metodo adicionar delas
            # antes fazer algo p identificar qual deve ser chamada
        
        return

    
    def veiculDisp(self):
        cont = 0
        for x in self.BD.BancoDeDados:
            reserva = x.getReservado()
            if reserva == False or reserva == 'False':
                cont +=1
        return cont
            
    
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

    def cancelar(self,placa):
        return self.BD.cancelReserva(placa)

    def listaCertoTipo(self,tipo):
        return self.BD.veicuDisponivel(tipo)





