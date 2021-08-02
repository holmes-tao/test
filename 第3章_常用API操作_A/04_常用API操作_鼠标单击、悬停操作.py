from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
sleep(2)

# 在Selenium中将鼠标键盘操作封装在 ActionChains 类中

# 定位到 "设置" 标签
element = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')

# 创建一个鼠标操作的对象  [tʃeɪnz]
# mouse = ActionChains(driver)

# 主要操作：
# click(on_element=None)  # 鼠标单击。适用于链接、选框等元素。
# click_and_hold(on_element=None)  # 鼠标单击并且按住部分
# double_click(on_element=None)  # 鼠标双击
# context_click(on_element=None)  # 鼠标右击
# drag_and_drop(source, target)  # 鼠标拖拽
# drag_and_drop_by_offset(source, xoffset, yoffset)  # 将目标拖拽到目标位置
# key_down(value, element=None)  # 按下某个键，实现快捷键操作
# key_up(value, element=None)  # 松下某个键，一般和key_down操作一起使用
# move_to_element(to_element)  # 移动到指定元素
# move_to_element_with_offset(to_element, xoffset, yoffset)  # 移动鼠标到指定坐标
# release(on_element=None)  # 释放按下的鼠标
# perform()  # 将之前一系列的ActionChains执行

# 鼠标移动到"设置"，并悬停
ActionChains(driver).move_to_element(element).perform()
sleep(1)

# 鼠标悬停时，定位元素，超链接"搜索设置"，然后实现单击操作
driver.find_element_by_link_text("搜索设置").click()

driver.refresh()

# 鼠标在指定元素上右键1
element2 = driver.find_element_by_xpath('//*[@id="s_lg_img"]')  # 百度logo图片
sleep(1)
ActionChains(driver).context_click(element2).perform()

# 鼠标在指定元素上右键2
# ActionChains(driver).context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

sleep(1)
driver.quit()
