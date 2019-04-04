import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

mail_host='smtp.163.com'
receivers=['1601664015@qq.com']#接受邮箱的人
receiver=';'.join(receivers)
password='tl1995'#此处未邮箱授权码   为发送人的邮箱授权码
sender='18782048160@163.com'#发送邮箱的人

msg=MIMEMultipart('alternative')
msg['From']=sender
msg['To']=receiver
msg['Subject']='Python邮箱发送图片'

#邮箱正文
msg.attach(MIMEText('<html><body><h1>Hello</h1>'
                    '<p><img src="D:\\测试\\abc.jpg"></p>'
                    '</body></html><>','html','utf-8'))

file_path=r'D:\测试\abc.jpg'
with open(file_path,'rb') as f:
    mm=MIMEBase('image','jpg',filename='adc.jpg')
    mm.add_header('Content-Disposition','attachment',filename='abc.jpg')
    mm.add_header('Content-ID','<0>')
    mm.add_header('X-Attachment-Id','0')
    mm.set_payload(f.read())
    encoders.encode_base64(mm)
    msg.attach(mm)
try:
    server=smtplib.SMTP()
    server.set_debuglevel(1)
    server.connect(mail_host,25)
    server.login(sender,password)
    server.sendmail(sender,receivers,msg.as_string())
    server.close()
    print('发送成功')
except smtplib.SMTPException:
    print('无法发送')