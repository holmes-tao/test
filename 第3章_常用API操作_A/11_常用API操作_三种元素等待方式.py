from selenium import webdriver
from time import sleep, ctime
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待针对元素必用
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待针对元素必用
from selenium.webdriver.support import expected_conditions as EC  # 预期条件类(里面包含方法可以调用，用于显示等待)
from selenium.webdriver.common.by import By  # 用于元素定位
from selenium.common.exceptions import NoSuchElementException  # 找不到元素异常

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 1. 强制等待 使用time模块的sleep()方法
sleep(2)  # 强制等待2s

# 2. 隐式等待 implicitly_wait(time_to_wait)              [ɪmˈplɪsətli]
# 针对当下的 webdriver对象 进行的等待时长的设置。一次设置，终生有效。
# 必须等待页面加载完成才会进入到后续的操作，或者等待超时再进入后续的操作。
# 隐式等待对整个driver的周期都起作用，因此只需要设置一次即可。
# 隐式等待是针对全局元素设置进行等待。
# 原理：
#     周期性（默认每隔0.5秒）重新寻找元素，直到该元素找到。
#     或者超出指定最大等待时长，这时才抛出异常（如果是 find_elements 之类的方法， 则是返回空列表）。
driver.implicitly_wait(5)  # 设置最大等待时长为5s

try:
    print(ctime())
    driver.find_element_by_id('kw').send_keys('python')
    driver.find_element_by_id('su111').click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())

sleep(3)

# 3. 显式等待 WebDriverWait()
# WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
# 是针对指定的元素进行等待判定，需要通过from selenium.webdriver.support.wait import WebDriverWait导入模块
#     driver : 所创建的浏览器对象
#     timeout : 最长时间长度（默认单位：秒）
#     poll_frequency : 间隔检测时长（每）默认0.5秒
#     ignored_exceptions : 超时后的异常信息，默认情况下抛NoSuchElementException异常。
driver.get('https://www.baidu.com')
# 3.1 与until()或者until_not()方法结合使用
# 调用该方法提供的驱动程序作为参数，直到返回值为True或False
# WebDriverWait(driver,10).until(method，message="")
# WebDriverWait(driver,10).until_not(method，message="")
# 另外，lambda提供了一个运行时动态创建函数的方法，匿名函数。
driver.find_element_by_id('kw').send_keys('Selenium 自学网')
# element = WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_id("su"))
element = WebDriverWait(driver, 5, 0.5).until(lambda x: x.find_element_by_id("su111"), message='未找到该元素！嘿嘿')
# 3.2 与expected_conditions结合使用
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'su')), message="")
element.click()

sleep(3)
driver.quit()

# 注意：当隐式等待和显示等待一起被使用时，系统的等待时间取决于最长的等待时间。
# WebDriverWait元素等待和全局设置：https://zhuanlan.zhihu.com/p/143357537
