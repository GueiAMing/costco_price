from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#初始化 WebDriver
driver = webdriver.Chrome()

#打開網頁
driver.get("https://www.google.com")

#等待3秒
time.sleep(3)

#使用find_element 方法並結合By.NAME屬性定位元素
elem = driver.find_element(By.NAME,"q")

#在搜索框輸入文字
elem.send_keys("Hello")

#等待2秒
time.sleep(2)

#送出輸入的文字
elem.send_keys(Keys.RETURN)

time.sleep(5)

#返回上一頁
driver.back()


time.sleep(5)

#返回下一頁
driver.forward()

#取得搜尋結果
search_result = driver.find_element(By.ID,"search").text
print("搜尋結果:", search_result)

driver.quit()