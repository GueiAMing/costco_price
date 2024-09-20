from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from googleform_functions import CostcoPriceGoogleForm_All

import time
#設置 Chrome 的選項
chrome_options = Options()
chrome_options.add_argument('--headless') # 啟用 headless 模式

#初始化 WebDriver
driver = webdriver.Chrome(options=chrome_options)

for i in range(5):
    if i == 0:
        url = "https://www.costco.com.tw/c/hot-buys" #折扣的第1頁
        dashtext = "---------------------------------------------"
        CostcoPriceGoogleForm_All( product_name=dashtext, discount_value=dashtext, price_value="分隔線"+dashtext, you_pay_value=dashtext,url=url)
    else:
        url = "https://www.costco.com.tw/c/hot-buys" + f"?page={i}" #折扣的第2,3,4....頁
    driver.get(url=url)
    time.sleep(3)
    try:
        item_dict = {}#製作折扣商品的字典，key商品名稱，value商品網址
        for j in range(1,49):
            #因為tag是Flex所以透過XPATH定位，又一頁要定位的有48個，所以for迴圈跑1~48
            Xpath = f"/html/body/main/div[4]/sip-product-listing/div/div/div[2]/sip-page-slot/sip-product-list/div/section/div[3]/div/ul/sip-product-list-item[{j}]"
            elem = driver.find_element(By.XPATH, Xpath) 
            item = elem.find_element(By.CLASS_NAME,"thumb")
            item_name = item.get_attribute('title')
            item_href = item.get_attribute('href')
            item_dict[item_name] = item_href
            # time.sleep(3)
        print(item_dict)
        print("================")
        for item in item_dict:
            url = item_dict[item]
            driver.get(url=url)
            time.sleep(5)
            product_name = item
            discount_value = str()
            price_value = str()
            you_pay_value = str()
            try:
                elem1 = driver.find_element(By.CLASS_NAME,"price-value")
                price_value = elem1.text
                elem2 = driver.find_element(By.CLASS_NAME,"you-pay-value")
                print(item,f"有折扣{elem2.text}")
                discount_value = "有折扣"
                you_pay_value = elem2.text

                write_data_to_form = [product_name, discount_value, price_value, you_pay_value]
                print(write_data_to_form)
            except NoSuchElementException:
                print(item,"沒有折扣")
                discount_value = "沒有折扣"
                elem = driver.find_element(By.TAG_NAME,"sip-format-price")
                print(elem.text)
                price_value = elem.text
                you_pay_value = elem.text
                write_data_to_form = [product_name, discount_value, price_value, you_pay_value]
                print(write_data_to_form)
            CostcoPriceGoogleForm_All( product_name, discount_value, price_value, you_pay_value, url)
            time.sleep(3)
    except NoSuchElementException:
        print("找無商品")
        time.sleep(2)
    finally:
        dashtext = "---------------------------------------------"
        CostcoPriceGoogleForm_All(product_name=dashtext, discount_value=dashtext, price_value=f"第{i+1}頁"+dashtext, you_pay_value=dashtext, url=dashtext)


driver.quit()