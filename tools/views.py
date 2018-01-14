from flask import Flask, request
from ctocr import extract_pdf
import subprocess, sys, os, glob
from werkzeug.utils import secure_filename
app = Flask(__name__)
try:
    os.mkdir('document')
except:
    pass
app.config['UPLOAD_FOLDER'] = '/document'
@app.route('/ocr', methods=['POST'])
def index():
    if 'file' in request.files:
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(filename)
        extract_pdf(file)
        cmd = "python tools/demo.py --no-gpu"
        os.system(cmd)
    return file.filename

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5342)
