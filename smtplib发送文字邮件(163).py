import smtplib
from email.mime.text import MIMEText
mail_host='smtp.163.com'
receivers=['1601664015@qq.com']#接受邮箱的人
receiver=';'.join(receivers)
password='tl1995'#此处未邮箱授权码   为发送人的邮箱授权码
sender='18782048160@163.com'#发送邮箱的人
contents='Python发送文字'
msg=MIMEText(contents,'plain','utf-8')
msg['From']=sender
msg['To']=receiver
msg['Subject']='主题'
try:
    server=smtplib.SMTP()
    server.connect(mail_host,25)
    server.login(sender,password)
    server.sendmail(sender,receivers,msg.as_string())
    server.close()
    print('发送成功')
except smtplib.SMTPException:
    print('无法发送')