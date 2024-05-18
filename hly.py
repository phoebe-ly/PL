#會用到的套件
import requests 
from bs4 import BeautifulSoup
import pandas as pd # 如果要做列表

# 模擬使用者瀏覽器
# 我要的網頁
url = 'https://www.ptt.cc/bbs/Boy-Girl/M.1668436949.A.EBD.html'
# 偽裝成正常登入，讓request有headers供網頁偵查
headers = {
      "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
}
headers = {"Referer":url}
r1 = requests.get(url,headers=headers)
#開啟一個文檔
file=open("HLY.txt",mode="w",encoding="utf-8") 

soup = BeautifulSoup(r1.text,'lxml')
titles = soup.find_all('div',class_="push")#尋找class="bbs-screen bbs-content"的div標籤

comment=[]
for item in titles :
    c1= item.find('span','f3 push-content').text.strip()
    comment.append(c1)
df = pd.DataFrame(comment)
df