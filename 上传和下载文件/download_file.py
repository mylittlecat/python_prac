# encoding=utf-8
from flask import Flask
from flask import send_from_directory
from flask import url_for
import os.path

app=Flask(__name__)
dirpath=app.root_path # 获取当前目录路径

print dirpath

@app.route("/download/<filename>")
def downloader(filename):
    """这个文件可以通过访问app.route()函数注册的url下载运行这个程序的计算机上的指定路径的文件夹中的所有文件。"""
    return send_from_directory(dirpath,filename,as_attachment=True)
with app.test_request_context():
    print url_for('downloader',filename='download_file.py')
app.run(host="0.0.0.0")
