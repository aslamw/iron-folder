import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io
import os


class tabela():
    def __init__(self,dados):
        self.dados = dados
        plt.plot(self.dados)
        self.img = plt.gcf()
        layout = [[sg.Image(key="-IMAGE-")], 
            [sg.Input(size=(25,1),key='-file-')],
            [sg.Button("Load Image")]
        ]
        self.app = sg.Window('tabela').layout=layout
    def iniciar(self):
        while True:
            self.button, self.values = self.app.Read()
            if self.button == 'Load Image':
                bio = io.BytesIO()
                self.img.save(bio, format="PNG")
                self.app["-IMAGE-"].update(data=bio.getvalue())
x = np.array([1,2,3,4,5,6,7,8])
app = tabela(x)

app.iniciar()