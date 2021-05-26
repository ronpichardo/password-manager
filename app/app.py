from flask import Flask, request, render_template

import logging, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/credentials', methods=['GET'])
def gen_password():
    return render_template('passwords.html')

@app.route('/add', methods=['GET','POST'])
def add_password():
    return render_template('add.html')

@app.route('/update', methods=['GET'])
def get_update():
    return '<h1>Page is not implemented yet</h1><br><h2>Work in Progress</h2>'

if __name__ == '__main__':

    try:
        app.run(host='0.0.0.0')

    except Exception as e:
        print(f'Error starting the server {e}')