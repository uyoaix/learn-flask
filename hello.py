#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 学习flask框架


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!' % name

if __name__ == '__main__':
    app.run(debug=True)

