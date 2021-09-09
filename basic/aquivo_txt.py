from os import write
import shutil


arquivo = open('teste.txt','w')#cria arquivo ou abre
arquivo.write('hello word')
arquivo.close()

arquivo = open('teste.txt', 'a')#atualiza
arquivo.write('very good life')
arquivo.close()

arquivo = open('teste','r')#ler qualquer arquivo
texto = arquivo.read()
arquivo.close()

#shutil.copy(nome_arquivo, diretorio/new_name) copiar arquivo
#shutil.move(nome_arquivo, diretorio/new_name) mover