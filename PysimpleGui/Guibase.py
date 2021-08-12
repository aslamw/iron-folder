import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.theme(new_theme='DarkBlue14')#olhar na documentação para mudar
        #Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],#(5,0) ocupa 5 letras e na mesma linha
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='Gmail'),sg.Checkbox('Outlook',key='Outlook'),sg.Checkbox('Yahoo',key='Yahoo')],
            [sg.Text('Aceita cartão:')],
            [sg.Radio('sim','cartão',key='S'),sg.Radio('não','cartão',key='N')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='vel')],
            [sg.Button('Enviar')],
            [sg.Output(size=(22,10))]
        ]

        #Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)

        #Extrair dados da tela
        '''self.button, self.values = self.janela.Read()'''
    def Inicio(self):
        #colocando valores key nas variaveis
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            gmail = self.values['Gmail']
            outlook = self.values['Outlook']
            yahoo = self.values['Yahoo']
            cartao = self.values['S']
            cartao2 = self.values['N']
            velol = self.values['vel']
            #mostrando os valores
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'aceita gmail: {gmail}')
            print(f'aceita outlook: {outlook}')
            print(f'aceita yahoo: {yahoo}')
            print(f'aceita cartão: {cartao}')
            print(f'Não aceita cartão: {cartao2}')
            print(f'velocidade: {velol}')
            print('---------------------------')

tela = TelaPython()
tela.Inicio()