from flask import Flask, render_template, request, send_file
import os

from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='template')
upload_fold = os.path.join(os.getcwd(),'upload')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['imagem']
    savePath = os.path.join(upload_fold, secure_filename(file.filename))
    file.save(savePath)
    return 'upload frito com sucesso'
    
@app.route('/get-file/<filename>')
def getFile(filename):
    file = os.path.join(upload_fold, filename + '.png')
    return send_file(file, mimetype='imagem/png')

if __name__ == '__main__':
    app.run(debug=True)