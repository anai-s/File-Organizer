import smtplib
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:

    def __init__(self, msg = MIMEMultipart()) -> None:
        self.msg = msg

    def set_up(self, params): 
        self.msg['From'] = formataddr((params['fromname'], params['fromaddr'])) 
        self.msg['To'] = formataddr((params['toname'], params['toaddr']))
        self.msg['Subject'] = params['subject']
        self.fromaddr = params['fromaddr']
        self.fromname = params['fromname']
        self.toaddr = params['toaddr']
        self.toname = params['toname']
        self.fromapppwd = params['fromapppwd']

    def send_email(self, content, smtp= 'smtp.gmail.com'):
        self.msg.attach(MIMEText(content, 'plain'))
        try:
            server = smtplib.SMTP(smtp, 587)
        except Exception as e: 
            print(e) 
            server = smtplib.SMTP_SSL(smtp, 465)
        server.starttls()
        server.login(self.fromaddr, self.fromapppwd) 
        text = self.msg.as_string()
        server.sendmail(self.fromaddr, self.toaddr, text)
        server.quit()