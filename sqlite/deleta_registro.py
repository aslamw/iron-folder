from os import error
import sqlite3
from sqlite3.dbapi2 import Cursor
try:
    banco = sqlite3.connect('sqlite/base.db')#conecta e cria o banco

    conector = banco.cursor()#conecta as funçôes

    conector.execute("DELETE from pessoas WHERE idade = 40")#apaga a tabela que tenha a idade 40

    print(conector.fetchall())

    banco.commit()
    banco.close()#feixa tabela

except sqlite3.Error as erro:#informa e passa o erro
    print('não tem essa tabela',erro)