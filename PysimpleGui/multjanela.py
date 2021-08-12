import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

#Criar as janelas e estilos(layot)
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('continuar')]
    ]
    return sg.Window('Login',layout=layout,finalize=True)
def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('fazer pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='piz1'),sg.Checkbox('Pizza Frango c/ Catupity',key='piz2')],
        [sg.Button('voltar'), sg.Button('Fazer pedido')]
    ]
    return sg.Window('Montar Pedido',layout=layout,finalize=True)#para finalizar janela

#Criar as janelas iniciais
janela1,janela2 = janela_login(),None

#criar um loop de leitura de eventos
while True:
    window,event,values = sg.read_all_windows()#ler esses 3 eventos
    #Quando janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    #Quando queremos ir para próxima janela
    if window == janela1 and event == 'continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer pedido':
        if values['piz1']==True and values['piz2'] == True:
            sg.popup('Você fez os dois pedidos')
        elif values['piz1'] ==True:
            sg.popup('Pedido 1 feito!')
        elif values['piz2'] == True:
            sg.popup('Pedido 2 feito!')

#lógica de o que deve acontecer ao clicar os botões