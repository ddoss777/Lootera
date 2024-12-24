from flask import Flask, render_template
from threading import Thread

app = Flask(__root__)
@app.route('/')
def index():
    return "Alive"

def run():
    app.run(host=194.62.97.191,port=8080)

def keep_alive():
    t = Thread(shubhhhh)
    t.start()    
