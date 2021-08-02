from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
sleep(2)

# 常用键盘事件
# Keys.BACK_SPACE: 删除键
# Keys.SPACE: 空格键
# Keys.TAB: Tab键
# Keys.ESCAPE: 回退键
# Keys.ENTER: 回车键
# Keys.CONTROL, 'a': Ctrl + A   不区分大小写
# Keys.CONTROL, 'x': Ctrl + X
# Keys.CONTROL, 'v': Ctrl + V
# Keys.CONTROL, 'c': Ctrl + C
# Keys.SHIFT, '/': ?
# Keys.F1: F1键
# Keys.F12: F12键


driver.find_element_by_xpath('//*[@id="kw"]').send_keys('25k\n')
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.SHIFT,'/') # 等同如
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('?')
sleep(2)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL, 'a')  # 不区分大小写
sleep(2)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL, 'x')
sleep(2)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL, 'v')
sleep(2)
driver.find_element_by_xpath('//*[@id="su"]').click()
sleep(2)

sleep(2)
driver.quit()
