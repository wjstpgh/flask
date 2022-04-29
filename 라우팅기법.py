# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:50:10 2022

@author: tmark
"""
from flask import Flask

app=Flask(__name__)
@app.route('/')
def main():
    return '메인화면'

@app.route('/<get_string>')
def get_s(get_string):
    return get_string

@app.route('/<get_string>/<int:number>')
def get_num(get_string,number):
    return get_string*number

@app.route('/first/<userid>')
def userid(userid):
    return '<h3>Hello '+userid+' !</h3>'

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="8080")
    