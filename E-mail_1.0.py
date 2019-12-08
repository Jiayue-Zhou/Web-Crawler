# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:32:44 2018

@author: zjy
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

import time

import requests
from bs4 import BeautifulSoup
import re

def sleeptime(h,m,s):
    return h*3600+m*60+s

def sendmail(lmoney):
    #发送邮件部分
    my_sender='datamasking@163.com'
    subject="电费不足!"
    message='电费不足，请您及时缴费。剩余电费：{}元。Do not have enough balance, please pay in time. Left balance:{} yuan.'.format(lmoney,lmoney)
    msg = MIMEText(message,'plain', 'utf-8') 
    msg['From']=formataddr(["杭电智能电系统",my_sender])
    msg['To']=Header("630")
    msg['Subject']=Header(subject,'utf-8')
    # 输入Email地址和口令:
    from_addr = my_sender
    password = 'zheshimimi12'
    # 输入收件人地址:
    to_addr = ['XXX1@qq.com','XXX2@qq.com','XXX3@qq.com']
    # 输入SMTP服务器地址:
    smtp_server = "smtp.163.com"
    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


#爬虫部分
def Spider():
    
    url='http://wap.xt.beescrm.com/base/electricityHd/queryResult/ele_id/7/community_id/57/building_id/292/floor_id/2129/room_id/37083/flag/1'
    header={'user-agent':'Mozilla/5.0'}
    t1=requests.get(url,headers=header,timeout=300)
    t1.encoding='utf-8'
    soup=BeautifulSoup(t1.text,"html.parser")
    t2=soup.find('div',class_='info-box margin-top')
    t3=t2.find('p')

    t4=t3.text
    t5=re.search("[1-9]\d*\.\d*|0\.\d*[1-9]\d*$",t4)
    t6=float(t5.group())
    print(t6)
    if(t6<50):
        sendmail(t6)

second=sleeptime(0,0,10)
while(1):
    time.sleep(second)
    Spider()
    
