import wikipedia as wi

#wi.languages()
wi.set_lang("pt-br")
inf = wi.search('olá')
print(inf)