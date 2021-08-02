from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://news.baidu.com/')
driver.maximize_window()
sleep(1)

# # 方法1：使用目标元素参考去拖动。不能在页面上看到拖动效果。
# 页面上有些元素有时候需要页面下滑后才能加载，例如图片，可能会定位失败，所以这种方法有时候可能不适用。
# target_element = driver.find_element_by_link_text('娱乐')
# driver.execute_script("return arguments[0].scrollIntoView();", target_element)
# target_element.click()

# 方法2：使用像素值粗略拖动。能在页面上看到拖动效果。
#                                      左右,上下
# driver.execute_script('window.scrollTo(0,300)')
# sleep(2)
# driver.execute_script('window.scrollTo(0,600)')

pix = 1000
for i in range(3):
    driver.execute_script(f"scroll(0,{pix})")  # 坐标原点在左上角。
    pix += 1000
    sleep(2)

# driver.find_element_by_xpath('//*[@id="yule"]/div[1]/div/h2/a').click()

# 使滚动条滑到底部(亲测：只能滑动到已加载完成的地方)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

sleep(1)
driver.quit()
