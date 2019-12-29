# coding:utf-8
import emails
from emails.template import JinjaTemplate as T 

SMTP = 'smtp.126.com'
USERNAME = 'liuzhizhi123@126.com'
PASSWORD = ''

def send_email():
    message = emails.html(subject=T('Html email Testing'),
                        html=T(open('email_tmpl.html').read()),
                        mail_from=('auto-reporter', USERNAME))
    message.attach(data=open('readme.md', 'r'), filename="readme.txt")
    message.attach(filename="test.png", content_disposition="inline", data=open("test.png", "rb"))
    r = message.send(to=('Orangleliu', USERNAME),
                    render={'name': 'ALL', 'img_name': "test.png"},
                    smtp={'host': SMTP})
    
    print(r.status_code)


if __name__ == "__main__":
    send_email()