from logging import debug
from flask import Flask, render_template
app = Flask(__name__) 


@app.route('/')
def index():
    return render_template("index.html", phrase="hello")


@app.route('/names')
def namelist():
    names = [
        {'first_name' : 'Stef', 'last_name' : 'Curry'},
        {'first_name' : 'dude', 'last_name' : 'mcdooder'},
        {'first_name' : 'Michael', 'last_name' : 'Scott'}
    ]
    return render_template("index.html", names = names)

if __name__=="__main__":
    app.run(debug=True)

