import smtplib
from email.mime.text import MIMEText
mail_host='smtp.qq.com'
receivers='3182668966@qq.com'
sender='1601664015@qq.com'
password='kmapcmqvjlidbace'

contents='Python发送文字'
msg=MIMEText(contents,'plain','utf-8')
msg['From']=sender
msg['To']=receivers
msg['Subject']='主题'
try:
    server=smtplib.SMTP_SSL(mail_host,465)
    server.login(sender,password)
    server.sendmail(sender,receivers,msg.as_string())
    server.close()
    print('发送成功')
except smtplib.SMTPException:
    print('无法发送')