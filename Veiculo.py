'''
A classe Veiculo é uma classe abstrata, uma superclasse que auxilia na criação de todos os veiculos (carros, vans e utilitarios)
e os metodos get que existem dentro dela  servem para conseguir pegar as informações de dentro dos objetos que vão ser criados,
para serem usados pelo programa todo.
'''
class Veiculo():
    def __init__(self,tipo,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado):
        self.__tipo = tipo
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__autonomia = autonomia
        self.__ano = ano
        self.__placa = placa
        self.__chassi = chassi
        self.__RENAVAM = RENAVAM
        self.__reservado = reservado #reservado ou não
    '''
    todos os metodos get servem p usar as respectivas informações mostradas
    '''
    def getTipo(self):
        return self.__tipo

    def getFabricante(self):
        return self.__fabricante

    def getModelo(self):
        return self.__modelo
    
    def getAutonomia(self):
        return self.__autonomia

    def getAno(self):
        return self.__ano

    def getPlaca(self):
        return self.__placa

    def getChassi(self):
        return self.__chassi

    def getRENAVAM(self):
        return self.__RENAVAM

    def getReservado(self):
        return self.__reservado
    '''
    o metodo set serve para alterar a reserva dentro da classe Controle 
    '''
    def setReservado(self,reservado):
        self.__reservado = reservado
        return self.__reservado

        

'-----------------------------------------------------------'
'''
Classe filha de Veiculo, onde cria os carros
'''
class Carros(Veiculo):
    def __init__(self,tipo,fabricante,modelo,capacidade,autonomia,ano,placa,RENAVAM,chassi,reservado):
        Veiculo.__init__(self,tipo,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado)
        self.__capacidade = capacidade

    def getCapacidade(self):
        return self.__capacidade
    # os adicionar tudo no banco de dados não aqui
   



'----------------------------------'
'''
Classe filha de Veiculo, onde cria as vans
'''
class Vans(Veiculo):
    def __init__(self,tipo,fabricante,modelo,capacidade_transporte,autonomia,ano,placa,RENAVAM,chassi,reservado):
        Veiculo.__init__(self,tipo,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado)
        self.__capacidade_transporte = capacidade_transporte # A capacidade de transporte das vans

    def getCapacidade(self):
        return self.__capacidade_transporte

    
'-----------------------------------'
'''
Classe filha de Veiculo, onde cria os utilitarios
'''
class Utilitarios(Veiculo):
    def __init__(self,tipo,fabricante,modelo,capaci_caçamba,autonomia,ano,placa,RENAVAM,chassi,reservado):
        Veiculo.__init__(self,tipo,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado)
        self.__capaci_caçamba = capaci_caçamba

    def getCapacidade(self):
        return self.__capaci_caçamba

    
'-------------------------------------------------------'
