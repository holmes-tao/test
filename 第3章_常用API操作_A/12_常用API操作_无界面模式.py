from selenium import webdriver
from time import sleep

# 从Chrome59版本开始，支持Headless模式，即无界面模式。
# 1. 创建ChromeOptions对象
chrome_options = webdriver.ChromeOptions()
# 2. 添加--headless参数
chrome_options.add_argument('--headless')
# 3. 传递 ChromeOptions 到 ChromeOptions对象
# driver = webdriver.Chrome(chrome_options=chrome_options)  # 新版本 chrome_options 已弃用
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('python\n')
print(driver.title)

sleep(2)
driver.quit()
