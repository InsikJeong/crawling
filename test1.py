from bs4 import BeautifulSoup
import urllib.request as req

# html="""
# <html><body>
#     <h1 id="title">스크레이핑이란?</h1>
#     <p id="body">웹 페이지를 분석하는 것</p>
#     <p>원하는 부분을 추출하는 것</p>
# </body></html>
# """

# soup= BeautifulSoup(html,'html.parser')

# # h1 = soup.html.body.h1
# # p1 = soup.html.body.p
# # p2 = p1.next_sibling.next_sibling

# # print("h1 = " + h1.string)
# # print("p = " + p1.string)
# # print("p = " + p2.string)

# title=soup.find(id="title")
# body=soup.find(id="body")

# print("#title = "+title.string)
# print("#body = "+body.string)


# html="""
# <html><body>
#     <ul>
#         <li><a href="http://www.naver.com">naver</a></li>
#         <li><a href="http://www.daum.net">daum</a></li>
#     </ul>
# </body></html>
# """

# soup = BeautifulSoup(html,"html.parser")

# links=soup.find_all("a")

# for a in links:
#     href = a.attrs['href']
#     text = a.string
#     print(text,">",href)

# url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# res = req.urlopen(url)

# soup = BeautifulSoup(res,"html.parser")

# title = soup.find('title').string
# wf = soup.find("wf").string
# print(title)
# print(wf)

# url="http://info.finance.naver.com/marketindex/"
# res=req.urlopen(url)

# soup=BeautifulSoup(res,"html.parser")

# price=soup.select_one("div.head_info > span.value").string
# print("usd/krw =",price)

url="https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC"
res= req.urlopen(url)
soup=BeautifulSoup(res,"html.parser")

a_list=soup.select("#mw-content-text > div > ul > li a")

for a in a_list:
    name=a.string
    print("-",name)

# url = "https://www.google.com/search?q=cat&source=lnms&tbm=isch&sa=X&ved=2ahUKEwia3rvdhpLnAhXJMd4KHe7tDFEQ_AUoAXoECBIQAw&biw=955&bih=838&dpr=1.13#imgrc=7b8otwecOvn5bM:"
# res = req.urlopen(url)
# soup=BeautifulSoup(res,"html.parser")

# cat_list=soup.sel("#rg_s > div:nth-child(2) > a.rg_l > img")
