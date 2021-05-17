from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
import time

#[CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.naturecollection.com/brand/store/list.jsp"
    wd = webdriver.Chrome('C:/Users/Admin/Desktop/My_Python/WebDriver/chromedriver.exe')

    for i in range(1, 2): #매장 수만큼 반복
        wd.get(CoffeeBean_URL)
        time.sleep(1) #웹페이지 연결할 동안 1초 대기
        try:
            wd.execute_script("getList(%d)" %i)
            time.sleep(1) #스크립트 실행할 동안 1초 대기
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            store_info = soupCB.select("tr")
            for i in range(1,3):
                #print(store_info[i])
                #print(store_info[0].string,'1')
                #print(store_info[1].string,'2')
                #print(store_info[2].string,'3')
                #print(store_info[3].string,'4')
                #print(store_info[4].string,'5')
                #print(store_info[5].string,'6')
                store = store_info[i].find(id="shop_name")
                #address = store_info[i].find(id="shop_name")
                phone = store_info[i].find("")
                print(콜)

        except:
            continue
        return

#[CODE 0]
def main():
    result = []
    print('Nature Collection store crawling >>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result) #[CODE 1]

    CB_tbl = pd.DataFrame(result, columns = ('store', 'address','phone'))
    CB_tbl.to_csv('./NatureCollection.csv', encoding = 'cp949', mode = 'w', index = True)

if __name__ == '__main__':
    main()