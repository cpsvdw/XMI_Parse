from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('home.html')

if __name__ == '__main__':
    debugger == True
    app.run()