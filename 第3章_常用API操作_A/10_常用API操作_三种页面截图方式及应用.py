from selenium import webdriver
from time import sleep
import base64

driver = webdriver.Chrome()
driver.get('http://news.baidu.com/')
driver.maximize_window()
sleep(2)

# 方法1：直接以 文件 格式保存 get_screenshot_as_file，只能保存为png格式。（最常用）  [ˈskriːn ʃɒt]
driver.get_screenshot_as_file('C:\pic\screenshot1.png')

# 方法2：二进制 字节流格式 get_screenshot_as_png，能保存任意格式。
with open('C:\pic\screenshot2.jpg', 'wb') as qq:
    qq.write(driver.get_screenshot_as_png())

# 方法3：base64 字节流格式 get_screenshot_as_base64，能保存任意格式。
# base64格式 一般用于保存数据到数据库。大有用处。
with open('C:\pic\screenshot3.png', 'wb') as qq:
    qq.write(base64.b64decode(driver.get_screenshot_as_base64().encode('ascii')))

sleep(2)
driver.quit()
