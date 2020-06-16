from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
import time

# 测试通过cookie绕开验证码登陆公司邮箱

url = "https://mail.bonc.com.cn/"
driver = webdriver.Chrome()
driver.get(url)

url1 = ""

# 读取csv
with open('cookie.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        driver.add_cookie({'name': row[0], 'value': row[1]})
        print(row[0]+','+row[1])
        if row[0] == "Coremail.sid":
            url1 = url + "coremail/XT3/index.jsp?sid=" + row[1]
            print(url1)

driver.get(url1)
