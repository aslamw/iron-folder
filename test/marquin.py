import os
import random as rd
os.system('prompt $g')
os.system('cls')

class IA():
    def __init__(self):
        self.login = {}
        self.nome =''

        self.comandos = ['jogo1', 'jogo2', 'rank']
                                   
    def logi(self):
        os.system('color 1')

        conta1 = input('digite seu login: ')
        self.nome = conta1
        os.system('cls')

        if conta1 in self.login.keys():
            print('olá {} sua pontuação {}'.format(conta1,self.login[conta1]))
        else:
            self.login[conta1]=0
            print('conta criada')

    def tratamento(self):
        os.system('color 1')
        dialogo = input('faça sua escolha, em duvida mande um help: ')
         
        while True:
            if dialogo in self.comandos:
                eval(f'self.{dialogo}()')
            elif dialogo == 'help':
                print(f'aque está seus comandos {self.comandos}')
                self.tratamento()

    def rank(self):
        for i in self.login.keys():
            print(f'jogador {i} pontos {self.login[i]}')
        self.tratamento()

    def jogo1(self):
        os.system('cls')
        
        Numero = rd.randint(9, 999)
        n = 1
        try:
            while True:
                print(n*'°')
                res = int(input('Adivinhe o número de 9 até 999: '))
                n += 1

                os.system('cls')
                if res == 'return':
                    self.tratamento()
                elif res == Numero:
                    print('Boa vc ganhou mas 100 Pontos')
                    self.login[self.nome] += 100
                    self.tratamento()
                    break
                elif res < Numero:
                    print('aumente um pouco')
                elif res > Numero:
                    print('diminua ae bicho')
                else:
                    print('tá poxa menor')
        except:
            print('só é permitido números inteiros')
            self.tratamento()
    
    def jogo2(self):
        os.system('cls')
        os.system('color E')
        palavras = ['cobra','elefante','passaro','zebra','cachorro','cavalo']
        text = rd.choice(palavras)   #pega um aleatorio
        parte = list(text)        #divide
        parte2 = list(len(parte)*'_')      #separa por linhas
        dados = {'erro':0,'tentativa':0,'parte':parte2,'letra':[],'letra2':[]} #organiza os dados

        while True:
            print(f'ache as letras {dados["parte"] }')
            txt = input('digite uma letra: ')
            os.system('cls')
            if txt == 'return':
                self.tratamento()

            elif txt == 'exit':
                self.tratamento()

            elif dados['tentativa'] <= 15:#limite de tentativas

                if txt in text:
                    start = 0

                    for i in parte:
                        if i == txt: #quando acerta
                            dados['parte'][start]=i
                            start +=1
                            dados['letra'].append(i)
                        else:# não é essa letra para add
                            start +=1

                    if dados['parte'] == parte:           # ganhou boy
                        print('Boa você ganhou 100 pontos')
                        self.login[self.nome]+=50
                        self.tratamento()

                    dados['tentativa'] += 1

                else:  #quando erra
                    os.system('cls')
                    dados['erro']+=1
                    print(dados['erro']*'):',' \n não tem letra')
                    dados['tentativa'] += 1

            else:#GAME OVER
                os.system('color c')
                print('perdeu cara! mais de 15 tentativas')
                input('aperte ENTER')
                self.tratamento()
            
mocu = IA()
mocu.logi()
mocu.tratamento()