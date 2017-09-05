# coding:utf-8
# 用于发邮件
import smtplib
from email.mime.text import MIMEText
_user = "Your qq email address"
_pwd = "Your pwd"
_to = "dst email address"
msg = MIMEText("Test") # 内容
msg["Subject"] = "A email from python code." # 主题
msg["From"] = _user
msg["To"] = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException, e:
    print "Failed,%s" % (e)
