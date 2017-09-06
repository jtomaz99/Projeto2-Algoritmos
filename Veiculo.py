BancoDeDados = []

#classe abstrata
class Veiculo():
    def __init__(self,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado = False):
        self._fabricante = fabricante
        self._modelo = modelo
        self._autonomia = autonomia
        self._ano = ano
        self._placa = placa
        self._chassi = chassi
        self._RENAVAM = RENAVAM
        self._reservado = reservado #reservado ou não

    def adicionar(self):
        raise NotImplemented('não pode ser contruido na classe mãe')

    def getFabricante(self):
        return self._fabricante

    def getModelo(self):
        return self._modelo
    
    def getAutonomia(self):
        return self._autonomia

    def getPlaca(self):
        return self._placa

    def getChassi(self):
        return self._chassi

    def getRENAVAM(self):
        return self._RENAVAM

    def getReservado(self):
        return self._reservado


    def procurar(self,elemento):
        for veiculos in BancoDeDados:
            for x in veiculos[4:7]:
                if elemento == x:
                    return veiculos

    def buscar(self,tipo):
        tipo = tipo.lower()
        if tipo == 'utilitarios':
            for utilitarios in BancoDeDados:
                if len(utilitarios) == 9:
                    for x in utilitarios[7:8]:
                        if x == False:
                            print(utilitarios)
                                       
        elif tipo == 'vans':
            for vans in BancoDeDados:
                if len(vans) == 11:
                    for x in vans[7:8]:
                        if x == False:
                            print(vans)
                            
        elif tipo == 'carros':
            for carros in BancoDeDados:
                if len(carros) == 10:
                    for x in carros[7:8]:
                        if x == False:
                            print(carros)
 
                    

    def veicuDisponivel(self,tipo):
        tipo = tipo.lower()
        if tipo == 'utilitarios':
            cont_uti = 0
            for utilitarios in BancoDeDados:
                if len(utilitarios) == 9:
                    for x in utilitarios[7:8]:
                        if x == False:
                            cont_uti += 1
            print(cont_uti)
            

        elif tipo == 'vans':
            cont_van = 0
            for vans in BancoDeDados:
                if len(vans) == 11:
                    for x in vans[7:8]:
                        if x == False:
                            cont_van += 1
            print(cont_van)

        elif tipo == 'carros':
            cont_car = 0
            for carros in BancoDeDados:
                if len(carros) == 10:
                    for x in carros[7:8]:
                        if x == False:
                            cont_car += 1
            print(cont_car)


    def cancelReserva(self,placa):
        for veiculos in BancoDeDados:
            for x in veiculos:
                if x == placa:
                    self._reservado = False
                    return 
                    
        

'-----------------------------------------------------------'

class Carros(Veiculo):
    def __init__(self,fabricante,modelo,portas,autonomia,ano,placa,RENAVAM,chassi,reservado):
        Veiculo.__init__(self,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado = False)
        self._portas = portas

    def getNumPortas(self):
        return self._portas

    def adicionar(self):
        BancoDeDados.append([self._fabricante,self._modelo,self._autonomia,self._ano,self._placa,self._RENAVAM,self._chassi,self._reservado, self._portas,''])
        return



'----------------------------------'

class Vans(Veiculo):
    def __init__(self,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado,capacidade_transporte):
        Veiculo.__init__(self,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado = False)
        self._capacidade_transporte = capacidade_transporte # A capacidade de transporte das vans

    def getLotacao(self):
        return self._capacidade_transporte

    def adicionar(self):
        BancoDeDados.append([self._fabricante,self._modelo,self._autonomia,self._ano,self._placa,self._RENAVAM,self._chassi,self._reservado, self._capacidade_transporte,'',''])
        return

'-----------------------------------'

class Utilitarios(Veiculo):
    def __init__(self,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado,capaci_caçamba):
        Veiculo.__init__(self,fabricante,modelo,autonomia,ano,placa,RENAVAM,chassi,reservado = False)
        self._capaci_caçamba = capaci_caçamba

    def getCapaciCaçamba(self):
        return self._capaci_caçamba

    def adicionar(self):
        BancoDeDados.append([self._fabricante,self._modelo,self._autonomia,self._ano,self._placa,self._RENAVAM,self._chassi,self._reservado, self._capaci_caçamba])
        return
'-------------------------------------------------------'
#arquivo py separado
#class Veiculos:
    

        








    
