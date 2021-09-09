from datetime import date,time,datetime

data_atual = date.today()#data atual
print(data_atual.strftime('%d-%m-%y'))#modifica a apresentação da data

hora = time(hour=15, minute=18, second=30)#cria horario
print(hora)

data = datetime.now()#trás data e hora
print(data)

dia = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabádo', 'domingo')
print(dia[data.weekday()])#para traduzir

criar_date = '10/10/2020'
data_ajustada = datetime.strptime(criar_date, '%d/%m/%y')