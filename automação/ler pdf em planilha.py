#tem que instalar java e pip install tubula
import tabula

lista_pdf = tabula.read_pdf("ResultadoVale.pdf", pages='all')#ler o pdf e page escolhe as paginas
#e pode usar link
print(len(lista_pdf))#numero de tabelas lidas

for tabela in lista_pdf:
    print(tabela)
