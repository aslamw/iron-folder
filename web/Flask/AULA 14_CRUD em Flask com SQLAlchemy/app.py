from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
# pip install flask-sqlalchemy     para instalar o alchemy

app = Flask(__name__, template_folder='tempate')
app.config['SQLALCHEMY DATABASE_URI'] = 'sqlite://estudantes.sqlite3'

db = SQLAlchemy(app)
class estudante(db.Model):
    pass

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)