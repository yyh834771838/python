import requests
import re

def getHTMLText(url):
    try:
        kv = {'cookie':'miid=417873231361854147; t=de991b68440e8d203b91d29f1449ec6c; cna=HXRgFIEhS2YCAXOcjYSreOFX; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; UM_distinctid=1680cf786b615c-0951e86fc90608-6313363-e1000-1680cf786b7d32; tracknick=%5Cu822Arise; lgc=%5Cu822Arise; tg=0; enc=%2BgohxpfuYdPMkx6tz%2FveLQsEGmFb1MGJ3Gok4FjjGqIcBtSJS0NtpaGAZMhRAzz%2B0VbTY1n3WRhTfu01qi9row%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; uc3=vt3=F8dByRIsQBrxuoCegek%3D&id2=UNX8ggGNJ88HCQ%3D%3D&nk2=2R3O76iV&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; _cc_=URm48syIZQ%3D%3D; mt=ci=96_1&np=; _m_h5_tk=dbde5df3223cf17a28ff0648ec784607_1546434014282; _m_h5_tk_enc=e73f76a948ea1751618532101df98e8c; v=0; cookie2=1736fa0a34e82daf9c6d32f3df544ed2; _tb_token_=e6e818e01ee85; uc1=cookie14=UoTYMD9ZGpncXg%3D%3D; l=aB0jtq3pysEb4pDKBMaYBsv-fVt-O95P_YD91Ma62Tqkehd0oNSmRNrR-VwRp_qC55Oy_K-Jw; isg=BBISzufamoHKy-Einxf0vfRoY9j-Lc44LMUJitxrH0Ww77LpxLNmzRgJW0tTwI5V',
              'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        proxies={'https:':'https://121.227.76.129'}
        r = requests.get(url,proxies=proxies,headers = kv,timeout=30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
            print("")

def printGoodslist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = '笔记本'
    depth = 2
    start_url = 'https://s.taobao.com/search?q='+goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue

    printGoodslist(infoList)

main()    
