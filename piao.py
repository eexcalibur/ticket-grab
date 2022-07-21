from splinter.browser import Browser
from time import sleep
import traceback
import sys

class Buy_Tickets(object):
	# 定义实例属性，初始化
    def __init__(self, username, passwd, order, passengers, dtime, starts, ends):
        self.username = username
        self.passwd = passwd
        # 车次，0代表所有车次，依次从上到下，1代表所有车次，依次类推
        self.order = order
        # 乘客名
        self.passengers = passengers
        # 起始地和终点
        self.starts = starts
        self.ends = ends
        # 日期
        self.dtime = dtime
        # self.xb = xb
        # self.pz = pz
        self.login_url = 'https://i.hzmbus.com/webhtml/login'
        self.lang_url = 'https://i.hzmbus.com/webhtml/'
        self.ticket_url = 'https://i.hzmbus.com/webhtml/ticket_details?xlmc_1=%E9%A6%99%E6%B8%AF&xlmc_2=%E7%8F%A0%E6%B5%B7&xllb=1&xldm=HKGZHO&code_1=HKG&code_2=ZHO'
        self.driver_name = 'chrome'
        self.executable_path = '/Users/zhangtao/tmp/chromedriver'
	# 登录功能实现
    def login(self):
        self.driver.visit(self.login_url)
        input_list = self.driver.find_by_xpath('//div[@class="input_item"]/input')
        input_list[0]._set_value('lavok32841@runfons.com')
        input_list[1]._set_value('xxx')
        self.driver.find_by_xpath('//div[@class="login_btn"]').click()
        sleep(1)

        #self.driver.fill('input', self.username)
        # sleep(1)
        #self.driver.fill('down', self.passwd)
        # sleep(1)
	# 买票功能实现
    def start_buy(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        #窗口大小的操作
        #self.driver.driver.set_window_size(700, 500)
        self.login()

        #self.driver.visit(self.lang_url)
        self.driver.find_by_xpath('//span[@class="now_lang_text"]').click()
        self.driver.find_by_text('中文简体').click()
        #self.driver.find_by_xpath('//a[@class="yd-actionsheet-item"]')[0].click()

        self.driver.visit(self.ticket_url)
        self.driver.find_by_xpath('//span[@class="sele_date"]').click()        
        self.driver.find_by_text('廿三').click()
        input_list = self.driver.find_by_xpath('//div[@class="input"]/input')
        input_list[0]._set_value('xx')
        input_list[1]._set_value('xxxx')
        #self.driver.find_by_text('我已同意').click()    
        self.driver.find_by_xpath('//span[@class="hint_icon"]').click()
        #self.driver.find_by_xpath('//div[@class="bottom"]').click()

        sleep(30)

if __name__ == '__main__':
	# 用户名
	username = 'slnazhangtao@163.com'
	# 密码
	password = 'excalibur_030706'
	# 车次选择，0代表所有车次
	order = 2
	# 乘客名，比如passengers = ['丁小红', '丁小明']
	# 学生票需注明，注明方式为：passengers = ['丁小红(学生)', '丁小明']
	passengers = ['丁彦军']
	# 日期，格式为：'2018-01-20'
	dtime = '2018-01-19'
	# 出发地(需填写cookie值)
	starts = '%u5434%u5821%2CWUY' #吴堡
	# 目的地(需填写cookie值)
	ends = '%u897F%u5B89%2CXAY' #西安

	# xb =['硬座座'] 
	# pz=['成人票']
	
	
	Buy_Tickets(username, password, order, passengers, dtime, starts, ends).start_buy()
