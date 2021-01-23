# coding:utf-8
__author__ = 'Helen'
'''
description:邮件发送最新的测试报告
'''
import os,smtplib,os.path
from Omg.config import Parameter as Pr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Omg.Common import log


class send_email:
    def __init__(self):
        self.mylog = log.log()

    # 定义邮件内容
    def email_init(self,report,reportName):
        with open(report,'rb')as f:
            mail_body = f.read()

        # 创建一个带附件的邮件实例
        msg = MIMEMultipart()
        # 以测试报告作为邮件正文
        msg.attach(MIMEText(mail_body,'html','utf-8'))
        report_file = MIMEText(mail_body,'html','utf-8')
        # 定义附件名称（附件的名称可以随便定义，你写的是什么邮件里面显示的就是什么）
        report_file["Content-Disposition"] = 'attachment;filename='+reportName
        msg.attach(report_file) # 添加附件
        msg['Subject'] = 'OMG后台自动化测试报告:'+reportName # 邮件标题
        msg['From'] = Pr.email_name  #发件人
        msg['To'] = Pr.email_To  #收件人列表
        try:
            server = smtplib.SMTP(Pr.smtp_sever)
            server.login(Pr.email_name,Pr.email_password)
            server.sendmail(msg['From'],msg['To'].split(';'),msg.as_string())
            server.quit()
        except smtplib.SMTPException:
            self.mylog.error(u'邮件发送测试报告失败 at'+__file__)
    #     def email():
    #         smtpserver = "smtp.qq.com"
    #         mail_pass = "wbggcwlpmxwwbdef"
    #         username = "810592580@qq.com"
    #         reveiver = ['975215964@qq.com']
    #
    #         subjet = 'python email test'
    #         msg = MIMEMultipart('mixed')
    #         msg['subject'] = subjet
    #         msg['FROM'] = '赵芸杰<810592580@qq.com>'
    #         msg['TO'] = ";".join(username)
    #
    #         # 构建文本
    #         text = "我的朋友，祝你早午晚都安"
    #         text_plain = MIMEText(text, 'plain', 'utf-8')
    #         msg.attach = (text_plain)
    #         sendimagefile = open(r'C:\Users\41669\Pictures\我不想努力了.jpg', 'rb').read()
    #         image = MIMEImage(sendimagefile)
    #         image.add_header('Content-ID', '<imagel>')
    #         image["Content-Disposition"] = 'attachment;filename = "always supper cool.jpg'
    #         msg.attach(image)
    #
    #         smtp = smtplib.SMTP()
    #         smtp.connect(smtpserver)
    #         smtp.login(username, mail_pass)
    #         smtp.sendmail(username, reveiver, msg.as_string())
    #         smtp.quit()

    def sendReport(self):
        # 找到最新的测试报告
        report_list = os.listdir(Pr.report_path)
        report_list.sort(key=lambda fn: os.path.getmtime(Pr.report_path+fn) if not os.path.isdir(Pr.report_path+fn) else 0)
        new_report = os.path.join(Pr.report_path,report_list[-1])
        # 发送邮件
        self.email_init(new_report,report_list[-1])



