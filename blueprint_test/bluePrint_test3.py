# -*- coding:utf-8 -*-
from flask import Flask,Blueprint,url_for,render_template_string

shop=Blueprint('shop',__name__) 
# 蓝图对象名字的作用是用来区分蓝图对象的注册函数以便生成不同的url
@shop.route('/')
def v_index():
    return '''<li><a href="/admin">Here is shop you can go admin</a></li>'''

admin=Blueprint('admin',__name__)
@admin.route('/')
def v_index():
    return '''<li><a href="/shop">Here is admin you can go shop</a></li>'''

app=Flask(__name__)
app.register_blueprint(shop,url_prefix='/shop')
app.register_blueprint(admin,url_prefix='/admin')

@app.route('/')
def v_index():
    tpl='''
        <ul>
            <li><a href="{{ url_for('shop.v_index') }}">shop</a></li> 
            <li><a href="{{ url_for('admin.v_index') }}">admin</a></li>
        </ul>
    '''
    # 这里可以看到，虽然shop和admin都有注册函数v_index，但是因为它们的蓝图对象名不一样，就可以以此为区分告诉系统生成不同的url，而生成的url不同靠的是注册时的参数url_prefix不同
    return render_template_string(tpl)

app.run(host='0.0.0.0')
