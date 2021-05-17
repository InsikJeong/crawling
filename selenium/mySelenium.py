from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
import time

#[CODE 1]
def Goobne_store(result):
    Goobne_URL = "https://www.goobne.co.kr/store/search_store.jsp"
    wd = webdriver.Chrome('C:/Users/user/Desktop/인공지능실습/work/selenium/chromedriver.exe')

    for i in range(1, 106): #매장 수만큼 반복
        wd.get(Goobne_URL)
        time.sleep(1) #웹페이지 연결할 동안 1초 대기
        try:
            wd.execute_script("store.getList(%d)" %i) #store.getList 함수를 사용하여 다음페이지를 계속 불러옴
            time.sleep(1) #스크립트 실행할 동안 1초 대기
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser') # 파싱
            store_info = soupCB.select("tbody") #tbody태그를 찾음
            for i in range(0,2):
                tr = store_info[i].find_all('tr') #tr태그를 찾음 
                for j in range(0,10):
                    td = tr[j].find_all('td') #그안의 td정보 다 불러옴
                    store_name = td[0].get_text()
                    store_phone = td[1].string
                    store_address = td[2].find('a').get_text()
                    result.append([store_name]+[store_address]+[store_phone]) #result 값에 추가
                    # print(result)
        except:
            continue
    return

#[CODE 0]
def main():
    result = []
    Goobne_store(result) #[CODE 1]

    CB_tbl = pd.DataFrame(result, columns = ('store', 'address','phone')) #3개 속성으로 데이터 프레임 생성
    CB_tbl.to_csv('./Goobne.csv', encoding = 'cp949', mode = 'w', index = True) #엑셀파일 생성

if __name__ == '__main__':
    main()