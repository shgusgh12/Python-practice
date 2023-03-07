import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

#res.text 주소에서 가져온 html 정보
# soup 객체로 얻어온다
soup = BeautifulSoup(res.text,"lxml")
#print(soup.title.get_text())

#첫번째로 발견되는 a태그의 정보 soup.a
# print(soup.a)
# print(soup.a["href"])  #a element의 속성(href) '값' 정보를 출력


#class 값이 Nbtn upload 인 a element를 찾아줘
#print(soup.find("a", attrs={'class':'Nbtn_upload'}))

#print(soup.find('li', attrs={'class':'rank01'}))
# rank1 = soup.find('li', attrs={'class':'rank01'})
# print(rank1.a.get_text())
#rank1의 형제 관계에 있는 태그 rank2로 지정 
# rank2 = rank1.next_sibling.next_sibling #개행이 있어서 next_sibling 두번 사용
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank1 태그 기준으로 다음 항목을 찾는데 li만 찾는다 (개행 무시)
# rank2 =rank1.find_next_sibling('li')
# print(rank2.a.get_text())
#다른 형제들 출력
# all = rank2.find_next_siblings('li')
# print(all)





