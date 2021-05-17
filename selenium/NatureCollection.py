from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
import time

#[CODE 1]
def NatureCollection_store(result):
    NatureCollection_URL = "https://www.naturecollection.com/brand/store/list.jsp"
    wd = webdriver.Chrome('C:/Users/user/Desktop/인공지능실습/work/selenium/chromedriver.exe')

    for i in range(1, 93): #매장 수만큼 반복
        wd.get(NatureCollection_URL)
        time.sleep(1) #웹페이지 연결할 동안 1초 대기
        try:
            wd.execute_script("getList(%d)" %i)
            time.sleep(1) #스크립트 실행할 동안 1초 대기
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            store_info = soupCB.select("tbody")
            for i in range(0,2):
                tr = store_info[i].find_all('tr')
                print(tr)
                for j in range(0,10):
                    td = tr[j].find_all('td')
                    store = td[1].find('a').string
                    phone = td[2].find('a').string
                    address = td[3].find('a').string
                    result.append([store]+[address]+[phone])
                    print(result)

        except:
            continue
        return

#[CODE 0]
def main():
    result = []
    print('Nature Collection store crawling >>>>>>>>>>>>>>>>>>>>>>>>')
    NatureCollection_store(result) #[CODE 1]

    CB_tbl = pd.DataFrame(result, columns = ('store', 'address','phone'))
    CB_tbl.to_csv('./NatureCollection.csv', encoding = 'cp949', mode = 'w', index = True)

if __name__ == '__main__':
    main()
