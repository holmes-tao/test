from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# 弹出框 确认 文件
url = r'C:\01PycharmProjects\09_Selenium_Web自动化\01_基础_思课帮_201905\第3章_常用API操作_A\alert.html'
driver.get(url)
driver.maximize_window()
sleep(2)
driver.find_element_by_id("button").click()
sleep(2)

# 声明弹出框目标对象   [əˈlɜːrt]
alert = driver.switch_to.alert
print(alert.text)
# 1. 弹出框 确认
alert.accept()
# 2. 弹出框 取消
# alert.dismiss()
# 3. 弹出框 输入。JS输入弹框 不支持谷歌浏览器，支持火狐。
# alert.send_keys("selenium")

sleep(2)
driver.quit()
