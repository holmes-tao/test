from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')

temp = driver.find_elements_by_link_text('设置')[1]
ActionChains(driver).move_to_element(temp).perform()
driver.find_element_by_link_text('设置搜索').click()
sleep(3)
ele = driver.find_elements_by_id('nr')

# 1. Select对象方法
# 获取下拉框选项的方法：
# (1) select_by_index(num)
# (2) select_by_value(value)
# (3) select_by_visible_text(text)
Select(ele).select_by_index(1)  # 0开始，1标识第二个选项

# Select对象属性
# (1) options: 下拉框所有的选项元素
# (1) all_selected_options: 下拉框中已经选中的选项元素
# (1) first_selected_option: 下拉框中第一个选中的选项元素
ops = Select(ele).first_selected_option
print(ops.text)
sleep(2)
driver.quit()
