# -*- coding:utf-8 -*-
from flask import Flask,Blueprint
app=Flask(__name__)

@app.route('/')
def app_index():
    return '<a herf="/ezbp/">go blueprint</a>'

ezbp=Blueprint("zebp",__name__)
#What dose __name__ mean?
@ezbp.route('/')
def ezbp_index():
    return 'Welcome to my blueprint'

app.register_blueprint(ezbp,url_prefix='/ezbp')

app.run(host='0.0.0.0')
