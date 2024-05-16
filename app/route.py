from flask import render_template

def hello_world():
    return "Hello, MVC框架!"

def index():
    return render_template('index.html') 

def index_1():
    username = 'Belinda'
    date = '2024-05-26'
    return render_template('index_1.html', username=username, date=date)
    return render_template('index_1.html') 