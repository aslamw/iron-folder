from flask import Flask, render, template

app =Flask(__name__, template_folder='templates')

@ap.rote('/')
def index():
    return render template('index.html')

if __name__ == '__main__':
    app.run()