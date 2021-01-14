# coding:utf-8
__author__ = 'Helen'
'''
description:配置全局参数
'''
import time,os

# 获取项目路径
# project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
# test_case_path = project_path+"\\test_case"
test_case_path = project_path+"\\testcase"
# excel测试数据文档存放路径
# test_data_path = project_path+"\\data\\test_Data.xlsx"
# 日志文件存储路径
# log_path = project_path+"\\log\\mylog.log"
# print u'日志路径：'+log_path
# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path+"\\report\\"
report_name = report_path+time.strftime('%Y%m%d%H%S', time.localtime())
# 异常截图存储路径,并以当前时间作为图片名称前缀
# img_path = project_path+"\\screenshot_img\\"+time.strftime('%Y%m%d%H%S', time.localtime()) + '_'
# 测试项目所有用图片路径
# img_for_test_path = project_path + "\\imgForTest\\imgForAutoTest.png"
# print (img_for_test_path)
# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.qq.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = "810592580@qq.com"  # 发件人名称
email_password = "1gerendebeiai"  # 发件人登录密码
email_To = '975215964@qq.com'  # 收件人

'''OMG项目'''
# 前台网站URL访问路径
URL_base = 'http://omgtest.sumwhy.com/login'
# 网页title
pro_title = 'OMG'
# 后台管理系统URL访问路径
backend_URL = 'http://omgtest.sumwhy.com/login'
