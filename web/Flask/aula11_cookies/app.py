from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    resp = make_response(render_template('setcookie.html'))
    if request.method == "POST":
        dados = request.form['c']
        resp.set_cookie('testecookie', dados)
    return resp
@app.route('/getcookie')
def getcookie():
    cookieName = request.cookies.get('testecookie')
    return '<h1>valor cookie é: {}</h1>'.format(cookieName)

if __name__ == '__main__':
    app.run(debug=True)