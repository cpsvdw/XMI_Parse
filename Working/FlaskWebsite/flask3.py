from flask import Flask, render_template, request
from werkzeug import secure_filename

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('home.html')


@app.route('/aufbau')
def aufbau():
    return render_template('aufbau.html')


# send data from this route to html
# to access we need jinja, special web syntax to access through html
@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.debug = True
    app.run()
