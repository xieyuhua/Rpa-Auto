import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time
import random

# element.send_keys('xhoo2024')
# element.click()
# element.text
# element.get_attribute('href')  你可以获取元素的任何HTML属性，比如href、src、title等。
# element.is_displayed()  判断元素是否可见
# element.is_enabled()  判断元素是否可被点击
# element.clear()  清除元素中的文本（通常用于输入框）：
# element.submit()  提交表单（如果元素是一个表单或表单内的提交按钮）
# element.value_of_css_property('color') 获取元素的CSS属性值
# location = element.location  获取元素的位置和大小
# size = element.size  和大小
# print(f"Location: {location}, Size: {size}")
# element.screenshot('element_screenshot.png')    截图（保存元素的截图到文件）



driver = webdriver.Edge()
# 启动浏览器驱动
driver.get("https://vip.com/view/login")
# 把网址输入到驱动里面

# 定位并输入用户名和密码（这里以CSDN的输入框为例）
username_input = driver.find_element(By.XPATH, '//*[@name="username"]')  # 根据实际情况修改XPath
username_input.send_keys('xo2024')

password_input = driver.find_element(By.XPATH, '//*[@name="password"]')  # 根据实际情况修改XPath
password_input.send_keys('xo2024')

# 将会查找页面上所有 <a> 标签，然后返回第一个其 href 属性或可见文本包含 "评价" 这个词的元素
# review_a = driver.find_element(By.PARTIAL_LINK_TEXT, " 登 录 ")
# review_a.click()
# time.sleep(10)
# 使用类名定位元素
element = driver.find_element(By.CLASS_NAME, 'main__account__btn')
# 执行点击操作
element.click()

time.sleep(10)
driver.get("https://vip.com/view/orderReason/refund")

while 1:
    reviews = []
    while len(reviews) < 20000:
        try:
            comment_list = driver.find_elements(By.CLASS_NAME, "cell")
            for comment in comment_list:
                reviews.append(comment.text)
                print(f"已爬取{len(reviews)}条评论...")
            next_page_link = driver.find_element(By.CLASS_NAME, "btn-next")
            next_page_link.click()
        except StaleElementReferenceException:
            time.sleep(random.uniform(1, 3))
    driver.get("https://vip.com/view/orderReason/refund")
    print(reviews)
    
driver.quit()
