import sqlite3
from sqlite3.dbapi2 import Cursor

nome = 'lorui'
idade = 27
e_mail = 'lobg@gmail'

banco = sqlite3.connect('sqlite/base.db')#conecta e cria o banco

conector = banco.cursor()#conecta as funçôes

conector.execute("INSERT INTO pessoas VALUES('"+nome+"','"+str(idade)+"','"+e_mail+"')")#coloca os dados por variavel

conector.execute("SELECT *FROM pessoas")#seleciona todos os dados da tabela
print(conector.fetchall())#mostra os dados

banco.commit()