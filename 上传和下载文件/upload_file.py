# -*- coding:utf-8 -*-
import os
from flask import Flask,request,redirect,url_for
from werkzeug import secure_filename
from flask import send_from_directory #provide visit for files which were uploaded 

UPLOAD_FOLDER='/home/bijy/My Documents'
ALLOWED_EXTENSIONS=set(['txt','pdf','png','jpg','jpeg','gif']) #只能上传指定类型的文件防止恶意上传文件覆盖服务器的配置文件

app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER #app.config[...] 中保存的是路径

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET','POST'])
def upload_file():
    """保存上传的文件到指定位置并将网页重定向到uploaded_file()函数注册的url上"""
    if request.method=='POST':
        file=request.files['file']
        if file and allowed_file(file.filename):
            filename=secure_filename(file.filename) # 不支持中文文件名!
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/home/bijy/My Documents/<filename>')# <filename> is parament of function uploaded_file
def uploaded_file(filename):
    """在网页上显示出上传文件的内容"""
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

app.run(host='0.0.0.0')
