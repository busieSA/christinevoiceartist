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
    return render_template("videos.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")