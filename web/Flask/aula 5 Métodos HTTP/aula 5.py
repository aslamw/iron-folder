from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder='static')

@app.route('/add', methods=["GET","POST"])
def add():
    if request.method == "POST":
        return dumps(request.form)
    return "OKK GET"

if __name__ == '__main__':
    app.run()
    