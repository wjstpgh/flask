# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:14:22 2022

@author: tmark
"""

from flask import Flask,jsonify

app=Flask(__name__)
@app.route('/jsontest')
def client():
    data={'key':'value','json':'test'}
    return jsonify(data)

@app.route('/test_server')
def server():
    data={'host':'127.0.0.1','port':'8080'}
    return jsonify(data)

if __name__=='__main__':
    app.run(host='127.0.0.1',port='8080')


