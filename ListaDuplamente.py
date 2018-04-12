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
class No:
	def __init__(self,item,ante,prox):
		self.item = item
		self.prox = prox
		self.ante = ante

class ListaDuplamente:
	primeiro = None
	ultimo = None

	def inserir(self,item):
		novo_no = No(item,None,None)

		if self.primeiro is None:
			self.primeiro = novo_no
			self.ultimo = novo_no
		else:
			novo_no.ante = self.ultimo
			novo_no.prox = None
			self.ultimo.prox = novo_no
			self.ultimo = novo_no
	
	def remover(self,item):
		no_atual = self.primeiro
		while no_atual is not None:
			if no_atual.item == item:
				if no_atual.ante is None:
					self.primeiro = no_atual.prox
					no_atual.prox.ante = None
				else:
					no_atual.ante.prox = no_atual.prox
					no_atual.prox.ante = no_atual.ante
			no_atual = no_atual.prox
	
	def comparar(self,obj1,obj2):
		if ob1 < obj2:
			return -1
		elif obj1 == ob2:
			return 0
		elif obj1 > obj2:
			return 1
	
	def __len__(self):
		temp = 0
		aux = self.primeiro
		while aux is not None:
			temp += 1
			aux = aux.prox
		return temp
			

        #pelo index os atributos
	def adicionar_candidato(self,ano_ele2,sigla_uf5,codigo_car8,descri_car9,nome10,id_cand11,num_urna12,cpf13,nome_urna14,situacao16,num_part17,sigla_part18,nome_part19,codigo_ocup24,descri_ocup25,data_nas26,sexo30,grau_ins32,estado_civ34,uf_nas39,nome_mun41,situacao_pos44,bens):
		self.inserir(Candidato(ano_ele2,sigla_uf5,codigo_car8,descri_car9,nome10,id_cand11,num_urna12,cpf13,nome_urna14,situacao16,num_part17,sigla_part18,nome_part19,codigo_ocup24,descri_ocup25,data_nas26,sexo30,grau_ins32,estado_civ34,uf_nas39,nome_mun41,situacao_pos44,bens))
		return 
    
	







	'''def compararCandidatos(self):
		Candidato.primeiro.prox.getNome()


self.primeiro.prox.getNome()'''


	
