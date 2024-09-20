import requests


def CostcoPriceGoogleForm_Some( product_name, discount_value, price_value, you_pay_value, url):


    # Google 表單回應 URL
    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSey5888hWPghPVJf7-U4kfgUif23z5ro5uomrwHBbVfYZG0ug/formResponse'#曉明costco表單

    # 填寫的數據
    data = {
        'entry.804991618': product_name,
        'entry.506963088': discount_value,
        'entry.278277512': price_value,
        'entry.1081109346': you_pay_value,
        'entry.1523850910': url,

        # 更多的 entry 可以根據需求添加
    }

    # 發送 POST 請求
    response = requests.post(form_url, data=data)
    
    # 檢查回應狀態
    if response.status_code == 200:
        print("表單提交成功!")
        return "表單提交成功!"
    else:
        print(f"提交失敗，狀態碼: {response.status_code}")
        return f"提交失敗，狀態碼: {response.status_code}"


def CostcoPriceGoogleForm_All( product_name, discount_value, price_value, you_pay_value, url):


    # Google 表單回應 URL
    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfDN5JYJ1DTx116jq-Dr7n_apCsJP2gVHN_gnOK5GZ16zDcyg/formResponse'#曉明costco表單

    # 填寫的數據
    data = {
        'entry.804991618': product_name,
        'entry.506963088': discount_value,
        'entry.278277512': price_value,
        'entry.1081109346': you_pay_value,
        'entry.1523850910': url,

        # 更多的 entry 可以根據需求添加
    }

    # 發送 POST 請求
    response = requests.post(form_url, data=data)
    
    # 檢查回應狀態
    if response.status_code == 200:
        print("表單提交成功!")
        return "表單提交成功!"
    else:
        print(f"提交失敗，狀態碼: {response.status_code}")
        return f"提交失敗，狀態碼: {response.status_code}"


    