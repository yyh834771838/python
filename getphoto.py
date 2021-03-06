import requests
from bs4 import BeautifulSoup
import os

def getHTML(hlt,url):
    try:
        r = requests.get(url)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo,'html.parser')
        for link in soup.find_all('img'):
            hlt.append(link.get('src'))
    except:
        print("")

def main():
    start_url = 'https://gratisography.com/'
    root = "C://photo//"
    depth = 2 
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '/page/' + str(i+1)
            getHTML(infolist,url)
            for urlp in infolist:
                path = root + urlp.split('/')[-1]
                try:
                    if not os.path.exists(root):
                        os.mkdir(root)
                    if not os.path.exists(path):
                        r = requests.get(urlp)
                        with open(path,'wb') as f:
                            f.write(r.content)
                            f.close()
                            print("文件保存成功")
                    else:
                        print("文件已存在")
                except:
                    print("爬取失败")
        except:
            continue

main()
