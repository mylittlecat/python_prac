# -*- coding:utf-8 -*-
from flask import Flask,Blueprint

shop=Blueprint('shop','shop') # first parameter defines the name of blueprint
@shop.route('/')
def v_index():
    return 'shop root'

vip=Blueprint('vip','vip')
@vip.route('/')
def v_index():
    return 'vip homepage'

admin=Blueprint('admin','admin')
@admin.route('/')
def v_index():
    return 'admin root'

app=Flask(__name__)

app.register_blueprint(shop,url_prefix='/')
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(vip,url_prefix='/vip')

app.run(host='0.0.0.0')
