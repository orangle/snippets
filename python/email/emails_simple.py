# send email with attachments
import emails
from emails.template import JinjaTemplate as T 

SMTP = 'smtp.i-erya.com'
USERNAME = 'noreply@i-erya.com'
PASSWORD = ''


def send_email():
    message = emails.html(subject=T('Payment Receipt No.{{ billno }}'),
                        html=T('<p>Dear {{ name }}! This is a receipt...<br><br>'),
                        mail_from=('auto-reporter', USERNAME))
    message.attach(data=open('readme.md', 'r'), filename="readme.txt")
    r = message.send(to=('Orangleliu', 'zhizhi.liu@elmeast.com'),
                    render={'name': 'Orangleliu', 'billno': '141051906163'},
                    smtp={'host': SMTP, 'user': USERNAME, 'password': PASSWORD})
    
    print(r.status_code)


if __name__ == "__main__":
    send_email()