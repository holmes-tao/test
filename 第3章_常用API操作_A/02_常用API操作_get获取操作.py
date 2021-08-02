from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
sleep(2)

driver.find_element_by_xpath('//a[text()="贴吧"]').click()
sleep(3)

try:
    assert "python" in driver.page_source
except Exception as e:
    # 保存页面截图到文件
    driver.get_screenshot_as_file('D:/get截图.png')  # 保存到系统C盘可能会失败，找不到截图，建议保存到D盘。
    print('用例执行失败')
else:
    print('用例执行通过')

sleep(2)
driver.close()
