import requests
from bs4 import BeautifulSoup

try:
    header={'user-agent':'Mozilla/5.0'}
    url='http://news.sina.com.cn/'
    t1=requests.get(url,headers=header,timeout=300)
    t1.encoding='utf-8'
    soup=BeautifulSoup(t1.text,"html.parser")
    all_a = soup.find('div', class_='ct_t_01').find_all('a')
    for a in all_a:
        print(a.text)
    print("\n\n")
    for a in all_a:
        print(a.text)
        print("\n")
        urltarget=a['href']
        t2=requests.get(urltarget,headers=header)
        t2.encoding='utf-8'
        soup2=BeautifulSoup(t2.text,"html.parser")
        if soup2.find('div', id='artibody'):
            all_p=soup2.find('div', id='artibody').find_all('p') 
            for p in all_p[0:5]:
                print(p.text)
        else:
            print("该新闻为图片或者新闻集合，暂无法读取\n\n")
            continue
        print("\n")
    c=input()
except:
    print("网络出现错误或连接超时！")
    c=input()
