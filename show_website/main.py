#!/usr/bin/env python
# -*- coding:utf-8 -*-
#该程序并不需要第一行代码,这意味着不能用./main.py命令来运行!

from flask import Flask
from flask import render_template # 呈现页面
from flask import url_for # 构造函数的url
from flask import redirect # 页面重定向
from flask import request

app=Flask(__name__)

@app.route('/')
def home_page():
    """将页面跳转至index.html"""
    return redirect(url_for('login'))

@app.route('/index/index.html')
# @app.route('/index/<name>')
def index():
    return render_template('index.html')

@app.route('/index/chart.html')
def chart():
    return render_template('chart.html')

@app.route('/index/empty.html')
def empty():
    return render_template('empty.html')

@app.route('/index/form.html')
def form():
    return render_template('form.html')

@app.route('/index/tab-panel.html')
def tab_panel():
    return render_template('tab-panel.html')

@app.route('/index/table.html')  # 对应页面中的Responsive Tables
def table():
    return render_template('table.html')

@app.route('/index/ui-elements.html')
def ui_elements():
    return render_template('ui-elements.html')

@app.route('/login',methods=['POST','GET'])
def login():
    """登录界面"""
    error=None
    if request.method=='POST':
        if request.form['username']=='admin@acorn.com':
            return redirect(url_for('index',username=request.form['username']))
        else:
            error='Invalid username/password'
    return render_template('login.html',error=error)

with app.test_request_context():
    """打印上述每个函数的url"""
    print url_for('home_page')
    print url_for('index')
    print url_for('chart')
    print url_for('empty')
    print url_for('form')
    print url_for('table')
    print url_for('tab_panel')
    print url_for('ui_elements')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000) # 设置为0.0.0.0为什么打不开？port=8888为什么不能正常显示? 需要输入正确的ip:port
#    app.run()
