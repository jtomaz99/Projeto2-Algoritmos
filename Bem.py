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
class Bem:
    def __init__(self, id_candidato, codigo_tipo_bem, descrição_tipo_bem, descrição_detalhada_bem, valor_bem):
        self.__id_candidato = id_candidato
        self.__codigo_tipo_bem = codigo_tipo_bem
        self.__descrição_tipo_bem = descrição_tipo_bem
        self.__descrição_detalhada_bem = descrição_detalhada_bem
        self.__valor_bem = valor_bem

    def getIdCandidato(self):
        return self.__id_candidato
    
    def getCodigoTipoBem(self):
        return self.__codigo_tipo_bem
    
    def getDescriçãoTipoBem(self):
        return self.__descrição_tipo_bem
    
    def getDescriçãoDetalhadaBem(self):
        return self.__descrição_detalhada_bem
    
    def getValorBem(self):
        return self.__valor_bem
    
    def __str__(self):
        codigo = getCodigoTipoBem()
        descrição_tipo = getDescriçãoTipoBem()
        valor = getValorBem()
        descrição_detalhada = getDescriçãoDetalhadaBem()
        return codigo + ' -- ' + descrição_tipo + ' -- ' + valor + '\n' + descrição_detalhada
    