# coding=utf-8
#import json
import re
import requests
from bs4 import BeautifulSoup

url = 'http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx'
url_base = 'http://jirs.judicial.gov.tw/FJUD/'
payload = {
    'v_court':'TPD 臺灣臺北地方法院',
    'v_sys':'M',
    'jud_year':'',
    'sel_judword':'常用字別',
    'jud_case':'',
    'jud_no':'',
    'jud_no_end':'',
    'jt':'',
    'dy1':'',
    'dm1':'',
    'dd1':'',
    'dy2':'',
    'dm2':'',
    'dd2':'',
    'jmain1':'',
    'kw':'車禍',
    'keyword':'車禍',
    'sdate':'',
    'edate':'',
    'jud_title':'',
    'jmain':'',
    'Button':' 查詢',
    'searchkw':'車禍'
}
headers = {
    #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Accept-Encoding':'gzip, deflate',
    #'Accept-Language':'en-US,en;q=0.8,fr;q=0.6,zh-TW;q=0.4,zh;q=0.2',
    #'Cache-Control':'max-age=0',
    #'Connection':'keep-alive',
    #'Content-Length':'359',
    #'Content-Type':'application/x-www-form-urlencoded',
    #'Cookie':'FJUDQRY01_1=16/1/0/0/0/0//0////////////%u8ECA%u798D//%u8ECA%u798D///////%u8ECA%u798D; ASPSESSIONIDCSAATTAT=CPAKNDIBOPJGOJMPFBPGGEPE; BNES_ASPSESSIONIDCSAATTAT=WwO9WgPCguYmCwcKGc5zzN0w/jn9kXa8E/g6EBWZtg0LuekmxzsRQd9kmc6IXMnAJkTIokoqpn+fPYZEn0yYRdWwJkMVf4LcGakUDRF3dJ5m0GJ6ve+xFg==; ASP.NET_SessionId=ydhgt1rwglimpmym21z041aq; BNES_ASP.NET_SessionId=Ce+essMx0DejHhLbiYhQXCOGOPDMub+MBoCkGHiLkgT2YCbenXfioT7NW7aVRVk/rP7Ajprctw7rYctUXdJr83SxpidqWy4ncHHXCx/djrw=',
    #'Host':'jirs.judicial.gov.tw',
    #'Origin':'http://jirs.judicial.gov.tw',
    'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY01_1.aspx',
    #'Upgrade-Insecure-Requests':'1',
    #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
session = requests.Session()
html = session.post(url, data=payload, headers=headers)
html.encoding = 'utf-8'
#print html.text

soup = BeautifulSoup(html.text, "lxml")
#print soup.prettify()
nextpages =  soup.find_all('a', href=re.compile('^FJUDQRY02'))
links =  soup.find_all('a', href=re.compile('^FJUDQRY03'))
#print type(url_base)
#print type(links[0]['href'])
new_url = url_base+links[0]['href']
print new_url




#####################################################################

#new_url = 'http://jirs.judicial.gov.tw/FJUD/FJUDQRY03_1.aspx?id=1&v_court=TPD+%e8%87%ba%e7%81%a3%e8%87%ba%e5%8c%97%e5%9c%b0%e6%96%b9%e6%b3%95%e9%99%a2&v_sys=M&jud_year=&jud_case=&jud_no=&jud_no_end=&jud_title=&keyword=%e8%bb%8a%e7%a6%8d&sdate=&edate=&page=&searchkw=%e8%bb%8a%e7%a6%8d&jmain=&cw=0'

new_headers = {
    #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Accept-Encoding':'gzip, deflate, sdch',
    #'Accept-Language':'en-US,en;q=0.8,fr;q=0.6,zh-TW;q=0.4,zh;q=0.2',
    #'Connection':'keep-alive',
    #'Cookie':'FJUDQRY01_1=16/1/0/0/0/0//0////////////%u8ECA%u798D//%u8ECA%u798D///////%u8ECA%u798D; ASPSESSIONIDCSAATTAT=CPAKNDIBOPJGOJMPFBPGGEPE; BNES_ASPSESSIONIDCSAATTAT=WwO9WgPCguYmCwcKGc5zzN0w/jn9kXa8E/g6EBWZtg0LuekmxzsRQd9kmc6IXMnAJkTIokoqpn+fPYZEn0yYRdWwJkMVf4LcGakUDRF3dJ5m0GJ6ve+xFg==; ASP.NET_SessionId=ydhgt1rwglimpmym21z041aq; BNES_ASP.NET_SessionId=Ce+essMx0DejHhLbiYhQXCOGOPDMub+MBoCkGHiLkgT2YCbenXfioT7NW7aVRVk/rP7Ajprctw7rYctUXdJr83SxpidqWy4ncHHXCx/djrw=',
    #'Host':'jirs.judicial.gov.tw',
    'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx',
    #'Upgrade-Insecure-Requests':'1',
    #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
'''
new_payload = {
    'id':'1',
    'v_court':'TPD 臺灣臺北地方法院',
    'v_sys':'M',
    'jud_year':'',
    'jud_case':'',
    'jud_no':'',
    'jud_no_end':'',
    'jud_title':'',
    'keyword':'車禍',
    'sdate':'',
    'edate':'',
    'page':'',
    'searchkw':'車禍',
    'jmain':'',
    'cw':'0'
}
'''

html = session.get(new_url, headers=new_headers)
#html = session.get(new_url, data=payload, headers={'Referer':url})

html.encoding = 'utf-8'
#print html.text
soup = BeautifulSoup(html.text, "lxml")
#print soup.prettify()
doc = soup.pre
#doc = s.extract()
#d = doc.decode('utf-8').encode('utf-8')
print doc
#for link in links:
    #print link['href']
#print soup.find_all(#Table3)
#print soup.text
#print soup.contents
#print soup.select('html')[0]
#print soup.find("TABLE", {"id":"Table3"})[0] 	# id="title"
#print soup.select('.link')  	# class="link"
