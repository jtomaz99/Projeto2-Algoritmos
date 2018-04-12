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
from Bem import Bem
from ListaDuplamente import ListaDuplamente

class Candidato():
    def __init__(self,ano_eleição, estado, codigo_cargo, descrição_cargo, nome_candidato, id_candidato, num_urna, cpf, nome_urna, situação_candidatura, numero_partido, sigla_partido, nome_partido, codigo_ocupação, descrição_ocupação, data_nascimento, sexo, grau_instrução, estado_civil, uf_nascimento, municipio_nascimento, situação_candidato, lista_bens):
        self.__ano_eleição = ano_eleição
        self.__estado = estado  #Sigla da UF
        self.__codigo_cargo = codigo_cargo
        self.__descrição_cargo = descrição_cargo
        self.__nome_candidato = nome_candidato
        self.__id_candidato = id_candidato
        self.__num_urna = num_urna
        self.__cpf = cpf
        self.__nome_urna = nome_urna
        self.__numero_partido = numero_partido
        self.__nome_partido = nome_partido
        self.__sigla_partido = sigla_partido
        self.__codigo_ocupação = codigo_ocupação
        self.__descrição_ocupação = descrição_ocupação
        self.__data_nascimento = data_nascimento
        self.__sexo = sexo
        self.__grau_instrução = grau_instrução
        self.__estado_civil = estado_civil
        self.__uf_nascimento = uf_nascimento
        self.__municipio_nascimento = municipio_nascimento
        self.__situação_candidato = situação_candidato
        self.__situação_candidatura = situação_candidatura
        self.__lista_bens = lista_bens


    #metodos "get"
    def getAnoEleição(self):
        return self.__ano_eleição
    
    def getEstado(self):
        return self.__estado
    
    def getCodigoCargo(self):
        return self.__codigo_cargo
    
    def getDescriçãoCargo(self):
        return self.__descrição_cargo
    
    def getNomeCandidato(self):
        return self.__nome_candidato
    
    def getIdCandidato(self):
        return self.__id_candidato
    
    def getNumUrna(self):
        return self.__num_urna
    
    def getCpf(self):
        return self.__cpf
    
    def getNomeUrna(self):
        return self.__nome_urna
    
    def getNumeroPartido(self):
        return self.__numero_partido
    
    def getSiglaPartido(self):
        return self.__sigla_partido
    
    def getCodigoOcupação(self):
        return self.__codigo_ocupação

    def getDescriçãoOcupação(self):
        return self.__descrição_ocupação
    
    def getDataNascimento(self):
        return self.__data_nascimento
    
    def getSexo(self):
        return self.__sexo
    
    def getGrauInstrução(self):
        return self.__grau_instrução
    
    def getEstadoCivil(self):
        return self.__estado_civil
    
    def getUfNascimento(self):
        return self.__uf_nascimento
    
    def getMunicipioNascimento(self):
        return self.__municipio_nascimento
    
    def getSituaçãoCandidato(self):
        return self.__situação_candidato
    
    def getSituaçãoCandidatura(self):
        return self.__situação_candidatura
    
    def getListaBens(self):
        return self.__lista_bens


    #metodos para mudança de dados a baixo:
    def setAnoEleição(self,novo_ano):
        self.__ano_eleição = novo_ano
        return self.__ano_eleição
    
    def setEstado(self,novo_estado):
        self.__estado = novo_estado
        return self.__estado

    def setCodigoCargo(self,novo_codigo_cargo):
        self.__codigo_cargo = novo_codigo_cargo
        return self.__codigo_cargo
    
    def setDescriçãoCargo(self,nova_descrição_cargo):
        self.__descrição_cargo = nova_descrição_cargo
        return self.__descrição_cargo

    def setNomeCandidato(self,novo_nome_candidato):
        self.__nome_candidato = novo_nome_candidato
        return self.__nome_candidato
    
    def setIdCandidato(self,novo_id_candidato):
        self.__id_candidato = novo_id_candidato
        return self.__id_candidato

    def setNumUrna(self,novo_num_urna):
        self.__num_urna = novo_num_urna
        return self.__num_urna
    
    def setCpf(self,novo_cpf):
        self.__cpf = novo_cpf
        return self.__cpf

    def setNomeUrna(self,novo_nome_urna):
        self.__nome_urna = novo_nome_urna
        return self.__nome_urna
    
    def setNumeroPartido(self,novo_numero_partido):
        self.__numero_partido = novo_numero_partido
        return self.__numero_partido
    
    def setSiglaPartido(self,nova_sigla_partido):
        self.__sigla_partido = nova_sigla_partido
        return self.__sigla_partido
    
    def setCodigoOcupação(self,novo_codigo_ocupação):
        self.__codigo_ocupação = novo_codigo_ocupação
        return self.__codigo_ocupação
    
    def setDescriçãoOcupação(self,nova_descrição_ocupação):
        self.__descrição_ocupação = nova_descrição_ocupação
        return self.__descrição_ocupação
    
    def setDataNascimento(self,nova_data_nascimento):
        self.__data_nascimento = nova_data_nascimento
        return self.__data_nascimento
    
    def setSexo(self,novo_sexo):
        self.__sexo = novo_sexo
        return self.__sexo
    
    def setGrauInstrução(self,novo_grau_instrução):
        self.__grau_instrução = novo_grau_instrução
        return self.__grau_instrução
    
    def setEstadoCivil(self,novo_estado_civil):
        self.__estado_civil = novo_estado_civil
        return self.__estado_civil
    
    def setUfNascimento(self,novo_uf_nascimento):
        self.__uf_nascimento = novo_uf_nascimento
        return self.__uf_nascimento
    
    def setMunicipioNascimento(self,novo_municipio_nascimento):
        self.__municipio_nascimento = novo_municipio_nascimento
        return self.__municipio_nascimento
    
    def setSituaçãoCandidato(self,nova_situação_candidato):
        self.__situação_candidato = nova_situação_candidato
        return self.__situação_candidato
    
    def setSituaçãoCandidatura(self,nova_situação_candidatura):
        self.__situação_candidatura = nova_situação_candidatura
        return self.__situação_candidatura
    
    def setListaBens(self,nova_lista_bens):
        self.__lista_bens = nova_lista_bens
        return self.__lista_bens

    #implementar depois da classe bem.
    def __str__(self):
        nome_urna = self.getNomeUrna()
        num_urna = self.getNumUrna()
        sigla = self.getSiglaPartido()
        cargo = self.getDescriçãoCargo()
        UF = self.getEstado()
        municipio = self.getMunicipioNascimento()
        UfNas = self.getUfNascimento()
        return nome_urna + ' -- ' + num_urna + ' -- ' + sigla + '\n' + cargo + '(' + UF +')' + '\n' + municipio + '(' + UfNas + ')' + '\n' 



    #quando for feita a lista duplamente encadeada mudar isso.
    def incluirBem(self,bem):
        lista_bens = self.getListaBens()
        lista_bens.append(bem)
        return setListaBens(lista_bens)
        

