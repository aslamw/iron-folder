#----------------Ambiente virtual Venv
'''----------------CMD
python -m venv nome

........para ativar
cd .\nome\Scripts\Activate.ps1 ____PowerShell
cd .\nome\Scripts\Activet.bat ___CMD
........para desativar
deactivate
'''

#se ouver problema set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned ____Power.S

#------------------------------virtualenv
'''----------------CMD
pasta: virtualenv nome ____cria o ambiente
prompt $g ___simplifica o cmd
pip list _____ver os pacotes
pip freeze  _____baixados e suas dependencias
prompt __________ diretorio
virtualenv -p diretorio_py\python.exe nome ________cria com a verção que vc baixar


........................para ativar
pasta\Scripts\activate
'''
#--------------------------------------tratando Djando-----------------------------------------------------------------
'''
django-admin startproject aulaD  ____criar pasta django
django-admin startapp nome    ______cria pasta mais completa
python .\manage.py runserver  ____criar o servidor
python .\manage.py sqlmigrate nomeAPP numero ________ver banco de dados sqlite3
python .\manage.py showmigrations _________ver estatos dos migrates
python .\manage.py migrate _________testa as migrates
python .\manage.py startapp nome ________curia um app
python manage.py runserver  __________liga o servidor
python manage.py migrate ___________cria o django admin no settings
python manage.py createsuperuser --username nome  __________cria usuario e senha
python manage.py makemigrations nome do projeto_models  ______migração
python manage.py sqlmigrate core 001  _______cria tabela

'''

#-------------------------------------------.EXE-----------------------------------
#pyinstaller --onefile nome.py ___________se for com interface     -w antes do nome.py
