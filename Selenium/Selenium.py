import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time
import random

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
