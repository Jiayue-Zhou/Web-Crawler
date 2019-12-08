from bs4 import BeautifulSoup
import requests
import os
while(1):

    try:
        header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        m=requests.get('https://www.qiushibaike.com/text/',headers=header)
        m.encoding='utf-8'
        soup1=BeautifulSoup(m.text,"html.parser")
        div_a=soup1.find('div',id='content-left').find_all('span')
        for a in div_a:
            a1=a.find('span',class_='dash')
            if a1:
                a2=a1.next_sibling.next_sibling
                url='https://www.qiushibaike.com'+a2['href']
                j=requests.get(url,headers=header)
                j.encoding='utf-8'
                soup2=BeautifulSoup(j.text,"html.parser")
                t=soup2.find('div',class_='content')
                print(t.text)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                input("按回车键看下一个糗事...\n")
                temp=os.system('cls')
            else:
                continue
        
        
    
    
    
    
    
    except:
        print('error!')
        c=input()
