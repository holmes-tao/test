from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
sleep(2)

# 1. 新建tab
# # 方法1：通过元素定位，需要定位到body，再发送快捷键 ctrl + t。新版本中该方法已废弃。
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, 't')
# # 方法2：通过鼠标对象来操作。新版本中该方法也已废弃。
# actionChains = ActionChains(driver)mn
# # 按下ctrl和t，松开，悬停
# actionChains.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()

# 方法3：通过script脚本来操作。新版本可用。[ˈeksɪkjuːt]
driver.execute_script("window.open('https://www.sogou.com/')")

# 2. 句柄操作
# 获取所有句柄
handles = driver.window_handles
print(handles)
# 打印当前句柄
print(driver.current_window_handle)
# 切换句柄
driver.switch_to.window(handles[-1])
print(driver.title)
print(driver.current_window_handle)

# 使用搜狗搜索关键字
driver.find_element_by_xpath('//*[@id="query"]').send_keys("python\n")

sleep(2)
driver.quit()
