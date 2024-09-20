# Costco price crawler bu selenium
## 目錄

- [專案介紹](#專案介紹)
- [開發工具](#開發工具)
- [開始使用](#開始使用)

## 專案介紹
1. **專案目的**：因應有購買costco某些固定商品的需求，撰寫爬蟲來查詢折扣力度。
2. **爬蟲好處**：減少手動瀏覽各網頁所花費的時間、精力。
3. **功能**：
    1. 爬取某些特定商品，傳送是否折扣、折扣力度，商品網址到指定的google sheet。
    2. 除了上述功能外，額外爬取所有折扣商品傳送到定google sheet。

## 開發工具
1. Visual Studio Code
2. Python 3.10.10(虛擬環境)
3. git


## 開始使用
1. 安裝[開發工具](#開發工具)中三樣東西
2. 打開Visual Studio Code 開啟資料夾
3. 開啟Terminal(最上方Terminal->New Terminal) 快捷鍵 ctrl + `
4. 安裝套件，在Teriminal輸入
```
pip install -r requirements.txt
```
5. 下載資料夾
```
git clone https://github.com/GueiAMing/costco_price.git
```
6. 切換目錄到costco_price
``` 
cd ./costco_price
```
7. 修改程式碼
- 在googleform_functions.py中替換'your google form url'成自行設定的表單，或者刪除04、02_1之中有關的函式
8. 抓取特定商品
```
python 04_some_product.py
```
9. 抓取所有商品
```
python 02_1_all_product.py
```
