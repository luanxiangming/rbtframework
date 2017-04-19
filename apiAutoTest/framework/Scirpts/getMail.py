# -*- encoding: utf-8 -*-
# author : rayment
# CreateDate : 2013-01-24

import imaplib
import email
# 设置命令窗口输出使用中文编码
import sys
import re
import base64

reload(sys)
sys.setdefaultencoding('utf-8')


# 保存文件方法（都是保存在指定的根目录下）
def savefile(filename, data, path):
    try:
        filepath = path + filename
        print 'Saved as ' + filepath
        f = open(filepath, 'wb')
    except:
        print('filename error')
        f.close()
    f.write(data)
    f.close()


# 字符编码转换方法
def my_unicode(s, encoding):
    if encoding == 'gb2312':
        return unicode(s, 'gbk')
    elif encoding:
        return unicode(s, encoding)
    else:
        return unicode(s)


# 获得字符编码方法
def get_charset_mail(message, default="ascii"):
    # Get the message charset
    return message.get_charset_mail()
    return default


# 解析邮件方法（区分出正文与附件）
def parseEmail(msg, mypath):
    mailContent = None
    contenttype = None
    suffix = None
    for part in msg.walk():
        if not part.is_multipart():
            contenttype = part.get_content_type()
            filename = part.get_filename()
            charset = get_charset_mail(part)
            # 是否有附件
            if filename:
                h = email.Header.Header(filename)
                dh = email.Header.decode_header(h)
                fname = dh[0][0]
                encodeStr = dh[0][1]
                if encodeStr != None:
                    if charset == None:
                        fname = fname.decode(encodeStr, 'gbk')
                    else:
                        fname = fname.decode(encodeStr, charset)
                data = part.get_payload(decode=True)
                print('Attachment : ' + fname)
                # 保存附件
                if fname != None or fname != '':
                    # savefile(fname, data, mypath)
                    print 'have accessory!'
            else:
                if contenttype in ['text/plain']:
                    suffix = '.txt'
                if contenttype in ['text/html']:
                    suffix = '.htm'
                if charset == None:
                    mailContent = part.get_payload(decode=True)
                else:
                    mailContent = part.get_payload(decode=True).decode(charset)
    return (mailContent, suffix)


# 获取邮件方法
def getMail():
    # mailhost = 'vipabccas.vipabc.com'
    # account = 'tao_twang@vipabc.com'
    # password = base64.decodestring('QWRtaW4xMjM=\n')
    mailhost = 'imap.163.com'
    account = 'vipabcapitest007@163.com'
    password = base64.decodestring('QWRtaW4xMjM=\n')
    mypath = 'D:\\testEmail\\'
    port = 993
    ssl = 1
    # 是否采用ssl
    if ssl == 1:
        imapServer = imaplib.IMAP4_SSL(mailhost, port)
    else:
        imapServer = imaplib.IMAP4(mailhost, port)
    imapServer.login(account, password)
    imapServer.select()
    # 邮件状态设置，新邮件为Unseen
    # Message statues = 'All,Unseen,Seen,Recent,Answered, Flagged'
    resp, items = imapServer.search(None, "All")
    number = 1
    formname = ''
    l1 = items[0].split()
    l2 = [int(l1) for l1 in l1 if l1]
    mailList =[]
    for i in sorted(l2, reverse=True):
        # get information of email
        resp, mailData = imapServer.fetch(i, "(RFC822)")
        mailText = mailData[0][1]
        msg = email.message_from_string(mailText)
        ls = msg["From"].split(' ')
        strfrom = ''
        if (len(ls) == 2):
            # fromname = email.Header.decode_header((ls[0]).strip('\"'))
            formname = ls[1]
            # strfrom = 'From : ' + my_unicode(fromname[0][0], fromname[0][1]) + ls[1]
        else:
            strfrom = 'From : ' + msg["From"]
        strdate = 'Date : ' + msg["Date"]
        subject = email.Header.decode_header(msg["Subject"])
        sub = my_unicode(subject[0][0], subject[0][1])
        strsub = 'Subject : ' + sub

        mailContent, suffix = parseEmail(msg, mypath)
        # 命令窗体输出邮件基本信息
        print '\n'
        print 'No : ' + str(number)
        print formname
        print strdate
        print strsub
        '''
        print 'Content:'
        print mailContent
        '''
        # # 保存邮件正文
        if (suffix != None and suffix != '') and (mailContent != None and mailContent != ''):
            # savefile(str(number) + suffix, mailContent, mypath)
            number = number + 1
            mailList.append(mailContent)
        if number == 10:
            break
    imapServer.close()
    imapServer.logout()
    return  mailList


if __name__ == "__main__":
    # 邮件保存在e盘
    mypath = 'D:\\getEmail'
    print 'begin to get email...'
    getMail()
