# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:08:19 2022

@author: tmark
"""

from flask import Flask

app=Flask(__name__)
@app.route('/yoo')
def yoo():
    return 'this page is yoo'

if __name__=='__main__':
    app.run(host='127.0.0.1', port='8080')
