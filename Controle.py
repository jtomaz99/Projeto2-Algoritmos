# -*- coding: utf-8 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e estrutura de dados
Autor:  José Tomáz Gonçalves de Lima (jtgl)
Email:  jtgl@cin.ufpe.br
Data:   2018-04-05
Copyright(c) 2018 José Tomáz
'''
from Candidato import Candidato
from Bem import Bem
from ListaDuplamente import No
from ListaDuplamente import ListaDuplamente

class Criar:
    def __init__(self):
        self.__lista = ListaDuplamente()

    def getLista(self):
        return self.__lista
          

    def listando(self,path):
        lista_estados = ['AC','AL','AM','AP','BA','BR','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']
        banco_prov = []
        for x in lista_estados:
            estado = path + x + '.txt'
            info = open(estado, 'r')
            candidatos = info.readlines()
            info.close()


            for l in candidatos:
                l = l.strip()
                tokens = l.split(';')
                banco_prov.append(tokens)

        
        for dados in banco_prov:
            self.__lista.adicionar_candidato(dados[2].strip('"'),dados[5].strip('"'),dados[8].strip('"'),dados[9].strip('"'),dados[10].strip('"'),dados[11].strip('"'),dados[12].strip('"'),dados[13].strip('"'),dados[14].strip('"'),dados[16].strip('"'),dados[17].strip('"'),dados[18].strip('"'),dados[19].strip('"'),dados[24].strip('"'),dados[25].strip('"').strip('"'),dados[26].strip('"'),dados[30].strip('"'),dados[32].strip('"'),dados[34].strip('"'),dados[39].strip('"'),dados[41].strip('"'),dados[44].strip('"'),'#NULO')
        return 'Lista criada com sucesso'

    def listandoDados(self,path_candidatos,path_bens):
        self.listando(path_candidatos)
        lista_estados = ['AC','AL','AM','AP','BA','BR','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']
        banco_prov = []
        for x in lista_estados:
            estado = path_bens + x + '.txt'
            info = open(estado, 'r')
            bens = info.readlines()
            info.close

            for l in bens:
                l = l.strip()
                tokens = l.split(';')
                banco_prov.append(tokens)

        contador = len(self.getLista())
        while contador > 0:
            contador -= 1
            aux = self.getLista().primeiro.prox
            for dados in banco_prov:
                ID = aux.item.getIdCandidato()
                if int(ID) == int(dados[5].strip('"')):
                    aux.item.setListaBens(Bem(dados[5].strip('"'),dados[6].strip('"'),dados[7].strip('"'),dados[8].strip('"'),dados[9].strip('"')))
                    break
                else:
                    aux = self.getLista().primeiro.prox

        return 'Bens colocados com sucesso'







                
#para ver os candidatos na lista faz:
#a = Criar()
#a.listando()
#print(a.getLista().primeiro.prox.item)



