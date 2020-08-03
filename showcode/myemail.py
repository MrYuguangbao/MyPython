import smtplib      # 导入 smtplib 邮件处理库
from email.mime.text import MIMEText
from email.utils import formataddr

mail_server = "smtp.163.com"        # 发件人的 SMTP 服务器
port = "25"  # 服务端口

sender = "******@163.com"     # 发件人邮箱帐号
sender_passw = "******"         # 发件人邮箱密码(第3方登录授权密码)
receiver = "******@qq.com"      # 收件人邮箱帐号

msg = MIMEText('python邮件发送测试。', "plain", "utf-8")      # 邮件内容（正文）  需要发送HTML文件时，plain 改为 html 即可!
msg['From'] = formataddr(["发件人邮箱昵称", sender])      # 发件人信息
msg['To'] = formataddr(["收件人邮箱昵称", receiver])      # 收件人信息
msg['Subject'] = "邮件的主题"       # 邮件的主题

def sendMail(mail_server, port, sender,sender_passw, receiver):
    try:
        mail = smtplib.SMTP(mail_server, port)  # 使用SMTP()方法指向服务器（使用QQ邮箱服务器时，需改用 SMTP_SSL()方法）
        mail.login(sender, sender_passw)    # 请求服务器，登录帐号
        mail.sendmail(sender, [receiver], msg.as_string() )   # 发送邮件(给receiver传入列表时，表示群发)
        mail.quit()     # 断开连接
        print("邮件发送成功！")
    except:
        mail.quit()
        print("邮件发送失败！")

sendMail(mail_server, port, sender, sender_passw, receiver)