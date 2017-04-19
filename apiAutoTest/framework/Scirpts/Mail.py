# coding:utf8
# python2.7 mailtest.py
'''''
使用smtp和pop3 协议收发qq邮箱实验
用户名和密码需要自己填写
'''

from smtplib import SMTP
from smtplib import SMTPRecipientsRefused
from poplib import POP3
from time import sleep
import sys

smtpserver = 'mail.vipabc.com'
server = 'vipabccas.vipabc.com'
emailaddr = 'tao_twang@vipabc.com'

# 组合邮件格式
origHeaders = ['From: 847915049@qq.com',
               'To: 847915049@qq.com',
               'Subject: test msg']
origBody = ['nihao ', 'yaan', 'sichuan']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHeaders), '\r\n'.join(origBody)])

# 发送邮件部分
sendSer = SMTP(smtpserver)
getMail = POP3(server)
sendSer.set_debuglevel(1)
print sendSer.ehlo()[0]  # 服务器属性等
try:
    errs = sendSer.sendmail(emailaddr, emailaddr, origMsg)
except SMTPRecipientsRefused:
    print 'server refused....'
    sys.exit(1)
sendSer.quit()
assert len(errs) == 0, errs

print '\n\n\nsend a mail ....OK!'
sleep(10)  # 等待10秒
print 'Now get the mail .....\n\n\n'

# 开始接收邮件
revcSer = POP3(pop3server)
revcSer.user(username)
revcSer.pass_(password)

rsp, msg, siz = revcSer.retr(revcSer.stat()[0])
sep = msg.index('')
if msg:
    for i in msg:
        print i
revcBody = msg[sep + 1:]
assert origBody == revcBody
print 'successful get ....'  #coding:utf8
#python2.7 mailtest.py
'''''
使用smtp和pop3 协议收发qq邮箱实验
用户名和密码需要自己填写
'''

from smtplib import SMTP
from smtplib import SMTPRecipientsRefused
from poplib import POP3
from time import sleep
import sys

smtpserver = 'smtp.qq.com'
pop3server = 'pop.qq.com'
emailaddr = '847915049@qq.com'
username = 'XXX'
password = 'XXX'

#组合邮件格式
origHeaders = ['From: 847915049@qq.com',
    'To: 847915049@qq.com',
    'Subject: test msg']
origBody = ['nihao ','yaan','sichuan']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHeaders),'\r\n'.join(origBody)])

#发送邮件部分
sendSer = SMTP(smtpserver)
sendSer.set_debuglevel(1)
print sendSer.ehlo()[0] #服务器属性等
sendSer.login(username,password) #qq邮箱需要验证
try:
   errs = sendSer.sendmail(emailaddr,emailaddr,origMsg)
except SMTPRecipientsRefused:
   print 'server refused....'
   sys.exit(1)
sendSer.quit()
assert len(errs) == 0,errs


print '\n\n\nsend a mail ....OK!'
sleep(10) #等待10秒
print 'Now get the mail .....\n\n\n'



#开始接收邮件
revcSer = POP3(pop3server)
revcSer.user(username)
revcSer.pass_(password)

rsp,msg,siz = revcSer.retr(revcSer.stat()[0])
sep = msg.index('')
if msg:
   for i in msg:
      print i
revcBody = msg[sep+1:]
assert origBody == revcBody
print 'successful get ....'