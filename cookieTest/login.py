from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# 测试通过cookie绕开验证码登陆公司邮箱

url = "https://mail.bonc.com.cn/"
driver = webdriver.Chrome()
driver.get(url)

driver.find_element(By.ID, "uid").send_keys("zhangshilin@bonc.com.cn")
driver.find_element(By.ID, "password").send_keys("305424820@ab")

time.sleep(10)
driver.find_element(By.ID, "login_button").click()

# 首次登陆后获取cookie
cookie_list = driver.get_cookies()

print(cookie_list)

with open("cookie.csv", "w") as fw:
    writer = csv.writer(fw)
    for cookie in cookie_list:
        writer.writerow([cookie['name'], cookie['value']])

driver.find_element(By.ID, "navFid_1").click()

driver.quit()

