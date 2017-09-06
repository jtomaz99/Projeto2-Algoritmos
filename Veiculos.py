from Controle import *

class Veiculos:
    def __init__(self):
        a = Controle()
        BancoDeDados = a.criar_BD()
        self.BancoDeDados = BancoDeDados
    
    def procurar(self,elemento):
        for veiculos in self.BancoDeDados:
            for x in veiculos:
                if elemento == x:
                    return veiculos

    def buscar(self,tipo):
        tipo = tipo.lower()
        if tipo == 'utilitarios':
            for utilitarios in self.BancoDeDados:
                if len(utilitarios) == 9 or utilitarios[0] == 'ute':
                    for x in utilitarios:
                        if x == False:
                            print(utilitarios)
                                       
        elif tipo == 'vans':
            for vans in self.BancoDeDados:
                if len(vans) == 11 or vans[0] == 'van':
                    for x in vans:
                        if x == False:
                            print(vans)
                            
        elif tipo == 'carros':
            for carros in self.BancoDeDados:
                if len(carros) == 10 or carros[0] == 'carro':
                    for x in carros:
                        if x == False:
                            print(carros)
 
                    

    def veicuDisponivel(self,tipo):
        tipo = tipo.lower()
        if tipo == 'utilitarios':
            cont_uti = 0
            for utilitarios in self.BancoDeDados:
                if len(utilitarios) == 9 or utilitarios[0] == 'ute':
                    for x in utilitarios:
                        if x == False:
                            cont_uti += 1
            print(cont_uti)
            

        elif tipo == 'vans':
            cont_van = 0
            for vans in self.BancoDeDados:
                if len(vans) == 11 or vans[0] == 'van':
                    for x in vans:
                        if x == False:
                            cont_van += 1
            print(cont_van)

        elif tipo == 'carros':
            cont_car = 0
            for carros in self.BancoDeDados:
                if len(carros) == 10 or carros[0] == 'carro':
                    for x in carros:
                        if x == False:
                            cont_car += 1
            print(cont_car)


    def cancelReserva(self,placa):
        for veiculos in self.BancoDeDados:
            for x in veiculos:
                if x == placa:
                    self._reservado = False
                    return 
    
