#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 学习flask框架


from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!' % name

if __name__ == '__main__':
    manager.run()

