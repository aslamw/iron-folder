import sqlite3
from sqlite3.dbapi2 import Cursor

banco = sqlite3.connect('sqlite/base.db')#conecta e cria o banco

conector = banco.cursor()#conecta as funçôes

#conector.execute('CREATE TABLE pessoas (nome text, idade integer, email text)')#cria a tabela pessoas

#conector.execute("INSERT INTO pessoas VALUES('Maria',40,'maria_123@gmail.com')")#coloca informação na tabela pessoas

conector.execute("SELECT *FROM pessoas")#seleciona todos os dados da tabela
print(conector.fetchall())#mostra os dados

banco.commit()