from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
sleep(2)

driver.find_element_by_xpath('//a[text()="贴吧"]').click()
sleep(5)

# driver.close()  # close以后，后面会报错
# 获取所有句柄  [ˈhændl]
handles = driver.window_handles
print(handles)
# 打印当前句柄 [ˈkɜːrənt]
print(driver.current_window_handle)
# 关闭当前标签页
driver.close()
# 切换句柄
driver.switch_to.window(handles[-1])
print(driver.current_window_handle)
print(driver.title)

sleep(2)
driver.quit()
