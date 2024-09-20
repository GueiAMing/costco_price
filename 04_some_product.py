from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import time
from googleform_functions import CostcoPriceGoogleForm_Some

#設置 Chrome 的選項
chrome_options = Options()
chrome_options.add_argument('--headless') # 啟用 headless 模式

#初始化 WebDriver
driver = webdriver.Chrome(options=chrome_options)

item_dict ={
            "雀巢 金牌冰萃濾袋研磨咖啡 10 公克 X 40 包":"https://www.costco.com.tw/Food-Dining/Drinks/Coffee/Nescafe-Gold-Cold-Brew-Bag-10-g-X-40-Pack/p/132545",
            "愛之味 蜂蜜燕麥 340毫升 X 12入 一次2箱":"https://www.costco.com.tw/Food-Dining/Drinks/Beverages-Juice/AGV-Honey-Oatmeal-Drink-340-ml-X-12-Count/p/973132",
            "愛之味 純濃燕麥 340毫升 X 12入 一次2箱":"https://www.costco.com.tw/Food-Dining/Drinks/Beverages-Juice/AGV-100-Oatmeal-Drink-340-ml-X-12-Count/p/97313",
            "萬歲牌 總匯點心包 42公克 X 20入 一次2箱":"https://www.costco.com.tw/Food-Dining/Snacks/Nuts-Jerky/Viva-Dry-Roasted-Trail-Mix-42-g-X-20-Pack/p/119227",
            "Kirkland Signature 科克蘭 三層抽取衛生紙 120抽 X 72入":"https://www.costco.com.tw/Househould-Baby-Toys/Household-Essentials/Toilet-Paper-Paper-Towels/Kirkland-Signature-3-Ply-Interfold-Bath-Tissue-120-Sheet-X-72-Count/p/189999",
            "Redoxon 力度伸 維他命C+D+鋅發泡錠(柳橙口味) 45錠 (15錠 X 3條)":"https://www.costco.com.tw/Health-Beauty/Supplements/Multi-Letter-Vitamins/Redoxon-CDZinc-Effervescent-Orange-Flavor-45-Tablet-15-Tablet-X-3-Pack/p/200762",
            "Samlip 法式小麵包蒜香口味 120公克 X 6入":"https://www.costco.com.tw/Food-Dining/Snacks/Cookies-Chips/Samlip-Garlic-Baguette-120-g-X-6-Pack/p/126612",

}
for item in item_dict:
    url = item_dict[item]
    driver.get(url=url)
    time.sleep(3)
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
        

    CostcoPriceGoogleForm_Some( product_name, discount_value, price_value, you_pay_value, url)
    time.sleep(5)


dashtext = "---------------------------------------------"
CostcoPriceGoogleForm_Some(product_name=dashtext, discount_value=dashtext, price_value=dashtext, you_pay_value=dashtext, url=dashtext)

driver.quit()


