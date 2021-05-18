from flask import Flask, render_template, url_for 
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/listen')
def listen():
    return render_template("listen.html")

@app.route('/videos')
def videos():
    return "hello world this is our video routes"

@app.route('/contact')
def contact():
    return "hello world this is our contact page"