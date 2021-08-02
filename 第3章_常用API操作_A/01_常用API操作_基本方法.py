"""2020/09/29"""
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
sleep(2)
# send_keys() ：键盘输入
driver.find_element_by_id('kw').send_keys('python\n')

# text ：获取标签文本值
text = driver.find_element_by_link_text("百度首页").text
print(text)

# get_attribute()：获取标签属性值
value = driver.find_element_by_id('su').get_attribute('value')
print(value)

# 窗口最大化/最小化/固定大小  [ˈmæksɪmaɪz] [ˈmɪnɪmaɪz]
driver.maximize_window()
driver.minimize_window()
driver.set_window_size(400, 800)  # 测试mobile页面时使用

# current_window_handle: 获取当前窗口句柄，即标识窗口字符串
print(driver.current_window_handle)

# current_url: 获取当前窗口URL
print(driver.current_url)

# is_selected：判断定位的元素是否被选中。常用于单选或多选按钮。
# print(driver.find_element_by_xpath('xxx').is_selected())

# is_enabled：判断定位的元素是否可操作。标签属性可设置冻结状态，设置后元素不可操作，比如点击、右键等。
# print(driver.find_element_by_xpath('xxx').is_enabled())

# is_displayed：判断定位的元素是否存在
# print(driver.find_element_by_xpath('xxx').is_displayed())

# clear(): 清空输入框
# print(driver.find_element_by_xpath('xxx').clear())

# quit(): 关闭浏览器并杀死chromedriver.exe进程

# title：页面标题
print(driver.title)  # python_百度搜索

# page_source：页面源码
print("python" in driver.page_source)

# session_id：在接口测试中有使用
print(driver.session_id)  # fba8f595ef39a60dbe7f5f8e67dec313

# name：浏览器名字
print(driver.name)  # chrome

# refresh(): 刷新页面
driver.refresh()

# back(): 回退
driver.back()

# forward(): 向前
driver.forward()

sleep(2)
driver.quit()
