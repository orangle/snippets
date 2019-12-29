#!/usr/bin/env python3
# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
 
'''
附件，内嵌图片
'''
img_list = './'
allfile=[]
 
'''
遍历文件夹获得所有图片绝对路径
'''
def getallfile(path):
    allfilelist=os.listdir(path)
    for f in allfilelist:
        if f.endswith(".png"):
            filepath=os.path.join(path, f)
            if os.path.isdir(filepath):
                getallfile(filepath)
            else:
                allfile.append(filepath)
    return allfile
 
 
def sendmail(filelist):
    sender = 'zhizhi.liu@cc.com'
    receiver = 'zhizhi.liu@cc.com'
    subject = 'python email with pictures'
    smtpserver = 'mta2.corp.cc.com'
 
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'python email'
    '''
    图片id加入所在位置 
    '''
    content = '<b>Some <i>HTML</i> text</b> and an image.<br>'
    for index in range(len(filelist)):
        if index % 2 == 0:
            content += '<img src="cid:'+str(index)+'"><br>'
        else:
            content += '<img src="cid:' + str(index) + '">'
 
    msgText = MIMEText(content, 'html', 'utf-8')
    msgRoot.attach(msgText)
     
    '''
    将图片和id位置对应起来
    '''
    index = 0
    for f in filelist:
        fp = open(f, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<'+str(index)+'>')
        index += 1
        msgRoot.attach(msgImage)
 
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
 
 
if __name__ == '__main__':
    sendmail(getallfile(img_list))