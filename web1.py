# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 13:18:06 2019

@author: Administrator
"""

from flask import Flask as web
import time
app =web(__name__)

@app.route("/")
def hello():
    return "Hi from Flask"

@app.route("/wish")
def hell():
    return "good afteernoon"

@app.route("/now")
def now():
    return str(time.ctime(time.time()))

app.run(port=8081)


