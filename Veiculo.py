#classe abstrata
class Veiculo():
    def __init__(self,tipo,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado):
        self.tipo = tipo
        self.fabricante = fabricante
        self.modelo = modelo
        self.autonomia = autonomia
        self.ano = ano
        self.placa = placa
        self.chassi = chassi
        self.RENAVAM = RENAVAM
        self.reservado = reservado #reservado ou não
       
    def getTipo(self):
        return self.tipo

    def getFabricante(self):
        return self.fabricante

    def getModelo(self):
        return self.modelo
    
    def getAutonomia(self):
        return self.autonomia

    def getAno(self):
        return self.ano

    def getPlaca(self):
        return self.placa

    def getChassi(self):
        return self.chassi

    def getRENAVAM(self):
        return self.RENAVAM

    def getReservado(self):
        return self.reservado

    def setReservado(self,reservado):
        self.reservado = reservado
        return self.reservado

        
   # classe veiculo separada das subclasses.---->
'-----------------------------------------------------------'

class Carros(Veiculo):
    def __init__(self,tipo,fabricante,modelo,capacidade,autonomia,ano,placa,RENAVAM,chassi,reservado):
        Veiculo.__init__(self,tipo,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado)
        self.capacidade = capacidade

    def getCapacidade(self):
        return self.capacidade
    # os adicionar tudo no banco de dados não aqui
   



'----------------------------------'

class Vans(Veiculo):
    def __init__(self,tipo,fabricante,modelo,capacidade_transporte,autonomia,ano,placa,RENAVAM,chassi,reservado):
        Veiculo.__init__(self,tipo,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado)
        self.capacidade_transporte = capacidade_transporte # A capacidade de transporte das vans

    def getCapacidade(self):
        return self.capacidade_transporte

    
'-----------------------------------'

class Utilitarios(Veiculo):
    def __init__(self,tipo,fabricante,modelo,capaci_caçamba,autonomia,ano,placa,RENAVAM,chassi,reservado):
        Veiculo.__init__(self,tipo,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado)
        self.capaci_caçamba = capaci_caçamba

    def getCapacidade(self):
        return self.capaci_caçamba

    
'-------------------------------------------------------'
