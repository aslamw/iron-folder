import os
import time

os.system('cls')
os.system('color 3')
print(os.getcwd())
os.system('prompt g$')

#a = os.popen(cmd='dir',mode='r').read() pega os dados


class IA():
    def __init__(self):
        self.functions = ['venv','ativar']
        
    def tratamento(self):
        self.desejo = input('=>_')
        if self.desejo in self.functions:
            eval(f'self.{self.desejo}()')

    def venv(self):

        os.system('color 5')
        print('carregando local')
        time.sleep(1)
        nome = input('digite o nome do seu ambiente virtual: ')
        os.system('cls')
        versao = input('vai colocar alguma verção anterior do python: ')

        if versao == 'sim':
            os.system('cls')
            dirr = input('digite o seu diretorio da sua versão python: ')
            os.system('cls')
            try:
                os.system(f'virtualenv -p {dirr}\python.exe {nome}')
            except:
                print('vc fez alguma merda')
                self.tratamento()

        else:
            os.system('cls')
            os.system(f'virtualenv {nome}')
        
        os.system('color 2')
        print('ambiente criado')
        self.tratamento()
    
    def ativar(self):
        time.sleep(1)
        os.system('cls')
        os.system('color E')
        os.system('cd Scripts')
        os.system('activate')
        a = True
        while a:
            ter = input('=>_')
            os.system(ter)

kyu = IA().tratamento()
