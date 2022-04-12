from flask import Flask, render_template

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


if __name__ == '__main__':
    app.debug = True
    app.run()

print(app.config)
