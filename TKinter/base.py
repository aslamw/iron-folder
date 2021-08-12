from tkinter import*

janela = Tk()
janela.title('teste app')#titulo
janela.geometry('500x250+600+300')#tamanho da janela depois do + posição da janela na área
janela.resizable(True , True)#não pode almentar ou diminuir a tela 0 pode ser no lugar de False
janela.minsize(width=500,height=250)#tamanho minimo permitido
janela.maxsize(800,600)#tamanho maximo
janela.state('zoomed')#inicia em tela cheia___ iconic deixa minimizado
janela.iconbitmap('TKinter/alq.ico')#muda o icone
janela['bg'] = 'blue'#muda a cor de fundo com dir(TK) ver as keys

#dimesão da janela
la = 500
lag = 300

#resolução da janela
largura = janela.winfo_screenmmwidth()
altura = janela.winfo_screenmmheight()

#posição da janela
posx = largura/2 - la
posy = altura/2 - lag


#botão
bt1 = Button(janela, text='Executar', command=lambda: click('olá'))
bt1.pack()#para existir

#estilos de label
label1 = Label(janela, text='olá', bg='#ffff00', fg='red',font='time 10 bold italic',width=10,relief='solid',bd=5).pack()#solid e bd para borda
label1 = Label(janela,text='label2', relief='groove', bd=5).pack()
label1 = Label(janela,text='label3', relief='flat', bd=5).pack()
label1 = Label(janela,text='label4', relief='raised', bd=5).pack()
label1 = Label(janela,text='label5', relief='sunken', bd=5).pack()
label1 = Label(janela,text='label6', relief='ridge', bd=5).pack()

janela.geometry("%dx%d+%d+%d" %(largura, altura, posx, posy))


#função
def click(x):
    print(x)

janela.mainloop()#fechamento