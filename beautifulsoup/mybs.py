from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def ssunders_store(result):
    for page in range(1,32): #페이지 32까지 순환
        ssunder_url = 'http://www.mythunder.co.kr/board/index.php?board=map_01&sca=all&type=list&select=&search=%d=2&now_date=ZQ2LU' %page #썬더치킨 url
        print(ssunder_url)
        html = urllib.request.urlopen(ssunder_url)
        soupSsunders = BeautifulSoup(html, 'html.parser') #BeautifulSoup 객체 생성 후 파싱
        tag_div = soupSsunders.find_all('div', attrs={'class':'board_list_text'}) #board_list_text라는 클래스 이름인 div태그를 찾음
        for store in tag_div: 
            if len(store) <= 6: # 제일마지막을 판단함 마지막에 가면 지점정보 x 31페이지에 6개밖에없음
                break
            store_name = store.find(class_="board_list_title").get_text() #get_text() 사용하는 이유는 string을 사용하면 자식태그가 2개 이상일떄 none이 뜨기떄문 /지점명
            store_address = store.find_all('dl')[0].find('dd').string #주소
            store_phone = store.find_all('dl')[1].find('dd').string #전화번호
            store_open = store.find_all('dl')[2].find('dd').string # 오픈날짜
            # print(store_address)
            result.append([store_name]+[store_address]+[store_phone]+[store_open]) #result값에 추가
    return

def main():
     result = []
     print('ssunders store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
     ssunders_store(result) #[CODE 1] 호출
     ssunders_tbl = pd.DataFrame(result, columns = ('store','address','phone', 'store_open')) #데이터 프레임 생성
     ssunders_tbl.to_csv('C:/Users/user/Desktop/인공지능실습/work/beautifulsoup/ssunders1.csv', encoding ='cp949', mode = 'w', index = True) #엑셀파일로 생성
     del result[:]

if __name__ == '__main__':
    main()
