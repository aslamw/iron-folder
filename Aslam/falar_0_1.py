import sqlite3 as sql
import os

palavras ={}
texto = []
class aslam():
    def __init__(self,palavras):
        self.escut = palavras
        self.palavras = {}
        self.banco = sql.connect('Aslam/fala.db')
        self.start = self.banco.cursor()
        self.start.execute("SELECT *FROM fala")
        self.dados = self.start.fetchall()

        #fechar
        self.banco.commit()
        self.banco.close()

    def falar(self):

        if self.escut in self.dados['palavra']:
            print(self.dados['resposta'])
        else:
            self.tratamento()

    def tratamento(self):
        peso = 1
        escute = input(f'{self.escut}? ')
        self.palavras[self.escut]=[escute,0,0,0]

        #guardar
        self.banco = sql.connect('Aslam/fala.db')
        self.start = self.banco.cursor()
        conector.execute("INSERT INTO pessoas VALUES('"+self.escut+"','"++"','maria_123@gmail.com')")

        

while True:
    txt = print('aslam>>_ ')
    IA = aslam(txt)
    IA.falar()

'''
0 = preto;
1 = azul;
2 = verde;
3 = aqua;
4 = vermelho;
5 = roxo;
6 = amarelo;
7 = branco;
8 = cinza;
9 = azul claro;
A = verde claro;
B = aqua claro;
C = vermelho claro;
D = lilás;
E = amarelo claro;
F = branco brilhante.
'''