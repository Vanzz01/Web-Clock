from time import strftime

from flask import Flask

app = Flask(__name__)

def time():
    string = strftime('%H:%M:%S %p')
    return string

@app.route('/')
def render():
    display = time()
    return display

if __name__=='__main__':
    app.run(host="0.0.0.0",port=4455,debug=True)