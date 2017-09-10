from Veiculo import *
# essa classe é um Banco de Dados
'''
A classe Veiculos é a classe criadora do Banco De Dados e onde a maioria das operações do BD são feitas
'''
class Veiculos:
    def __init__(self):
        self.BancoDeDados = []
    
    '''
    No metodo procurar se percorre todo o BD em busca do RENAVAM, chassi ou da placa, para achar o veiculo desejado
    e depois é mostrado na tela ele.
    '''
    def procurar(self,elemento):
        i = 0 
        total = len(self.BancoDeDados)
        while total > 0:
            if elemento == self.BancoDeDados[i].getPlaca() or elemento == self.BancoDeDados[i].getChassi() or elemento == self.BancoDeDados[i].getRENAVAM():
                tipo = self.BancoDeDados[i].getTipo()
                fabricante = self.BancoDeDados[i].getFabricante()
                modelo = self.BancoDeDados[i].getModelo()
                capacidade = self.BancoDeDados[i].getCapacidade()
                autonomia = self.BancoDeDados[i].getAutonomia()
                ano = self.BancoDeDados[i].getAno()
                placa = self.BancoDeDados[i].getPlaca()
                chassi = self.BancoDeDados[i].getChassi()
                RENAVAM = self.BancoDeDados[i].getRENAVAM()
                reservado = self.BancoDeDados[i].getReservado()
                return [tipo, fabricante, modelo, capacidade, autonomia, ano, placa, chassi, RENAVAM, reservado]
            i += 1
            total -= 1
        return 'Veiculo não existe no Banco De Dados, ou seu criterio de busca foi invalido'        
    '''
    No metodo buscar, é procurado todos os veiculos de um certo tipo que estão disponiveis para aluguel
    e é mostrado na tela uma lista com todos eles
    '''
    def buscar(self,tipo):
        tipo = tipo.lower()
        i = 0
        lista = []
        total = len(self.BancoDeDados)
        while total > 0:
            if self.BancoDeDados[i].getTipo() == tipo:
                if self.BancoDeDados[i].getReservado() == False or self.BancoDeDados[i].getReservado() == 'False':
                    tipo = self.BancoDeDados[i].getTipo()
                    fabricante = self.BancoDeDados[i].getFabricante()
                    modelo = self.BancoDeDados[i].getModelo()
                    capacidade = self.BancoDeDados[i].getCapacidade()
                    autonomia = self.BancoDeDados[i].getAutonomia()
                    ano = self.BancoDeDados[i].getAno()
                    placa = self.BancoDeDados[i].getPlaca()
                    chassi = self.BancoDeDados[i].getChassi()
                    RENAVAM = self.BancoDeDados[i].getRENAVAM()
                    reservado = self.BancoDeDados[i].getReservado()
                    atributos = tipo, fabricante, modelo, capacidade, autonomia, ano, placa, chassi, RENAVAM, reservado
                    lista.append(atributos)
                    i += 1
                    total -= 1
                else:
                    i += 1
                    total -= 1        
            else:
                i += 1
                total -= 1

        
        return lista 

    '''
    O metodo adicionar chama a classe baseada no tipo de veiculo fornecido, e adiciona as informações
    para assim poder criar o objeto e adicionar ao Banco De Dados.
    '''
    def adicionar(self, tipo, fabricante, modelo, capacidade, autonomia, ano, placa, RENAVAM, chassi, reservado):
        # colocar self.criterio e adicionar os selfs
        
        if tipo == 'van':
            return self.BancoDeDados.append(Vans(tipo, fabricante, modelo, capacidade, autonomia, ano, placa, RENAVAM, chassi, reservado))
        elif tipo == 'carro':
            return self.BancoDeDados.append(Carros(tipo, fabricante, modelo, capacidade, autonomia, ano, placa, RENAVAM, chassi, reservado))
        elif tipo == 'ute':
            return self.BancoDeDados.append(Utilitarios(tipo, fabricante, modelo, capacidade, autonomia, ano, placa, RENAVAM, chassi, reservado))
        
        

           
    '''
    No metodo veicuDisponivel ele mostra ao usuario a quantidade de veiculos que estão a disposição para aluguel
    dependendo do tipo de veiculo que seja fornecido.
    '''
    def veicuDisponivel(self,tipo):
        tipo = tipo.lower()
        cont = 0
        i = 0
        total = len(self.BancoDeDados)
        while total > 0:
            if self.BancoDeDados[i].getTipo() == tipo:
                if self.BancoDeDados[i].getReservado() == False or self.BancoDeDados[i].getReservado() == 'False':
                    cont += 1
            i += 1
            total -= 1
        return cont 


    '''
    O metodo cancelar reserva usa o metodo setReservado da Classe Veiculo, para poder alterar o status de reserva de um veiculo. 
    '''
    def cancelReserva(self,placa):
        tamanho = len(self.BancoDeDados)
        i = 0
        while tamanho > 0:
            placaC = self.BancoDeDados[i].getPlaca()
            reservado = self.BancoDeDados[i].getReservado()
            if placa == placaC:
                return self.BancoDeDados[i].setReservado(False)
            tamanho -= 1
            i += 1
            
        return 'não existe veiculo com essa placa'

