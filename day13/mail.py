

def send():
    from email import encoders
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart

    import smtplib

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = '2660389207@qq.com' #input('From: ')
    password = 'iutzuuodpxrpeaec'#input('Password: ')
    to_addr = '2431320433@qq.com'#input('To: ')
    smtp_server = 'smtp.qq.com'#input('SMTP server: ')

    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr('李鑫 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('计算器报告', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('计算器报告', 'plain', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个文件:
    with open('D:\PYTHON1\python_day\day13\计算器报告.html', 'rb') as f:
        # 设置附件的MIME和文件名，这里是html类型:
        mime = MIMEBase('html', 'html', filename='计算器报告.html')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='计算器报告.html')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

