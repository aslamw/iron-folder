import sqlite3
from sqlite3.dbapi2 import Cursor

nome = 'tuka'
idade = 23
e_mail = 'wg@gmail'

banco = sqlite3.connect('sqlite/base.db')#conecta e cria o banco

conector = banco.cursor()#conecta as funçôes

conector.execute("UPDATE pessoas SET nome = 'andre' WHERE idade = 27")#coloca informação na tabela pessoas

conector.execute("SELECT *FROM pessoas")#seleciona todos os dados da tabela
print(conector.fetchall())#mostra os dados

banco.commit()