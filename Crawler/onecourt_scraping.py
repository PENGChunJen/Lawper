# coding=utf-8
import time
import re
import requests
from bs4 import BeautifulSoup

url = 'http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx'
url_base = 'http://jirs.judicial.gov.tw/FJUD/'
courts = ["TPC 司法院－刑事補償", "TPU 司法院－訴願決定", "TPJ 司法院職務法庭", "TPS 最高法院", "TPA 最高行政法院", "TPP 公務員懲戒委員會", "TPH 臺灣高等法院", "TPH 臺灣高等法院－訴願決定", "TPB 臺北高等行政法院", "TCB 臺中高等行政法院", "KSB 高雄高等行政法院", "IPC 智慧財產法院", "TCH 臺灣高等法院 臺中分院", "TNH 臺灣高等法院 臺南分院", "KSH 臺灣高等法院 高雄分院", "HLH 臺灣高等法院 花蓮分院", "TPD 臺灣臺北地方法院", "SLD 臺灣士林地方法院", "PCD 臺灣新北地方法院", "ILD 臺灣宜蘭地方法院", "KLD 臺灣基隆地方法院", "TYD 臺灣桃園地方法院", "SCD 臺灣新竹地方法院", "MLD 臺灣苗栗地方法院", "TCD 臺灣臺中地方法院", "CHD 臺灣彰化地方法院", "NTD 臺灣南投地方法院", "ULD 臺灣雲林地方法院", "CYD 臺灣嘉義地方法院", "TND 臺灣臺南地方法院", "KSD 臺灣高雄地方法院", "HLD 臺灣花蓮地方法院", "TTD 臺灣臺東地方法院", "PTD 臺灣屏東地方法院", "PHD 臺灣澎湖地方法院", "KMH 福建高等法院金門分院", "KMD 福建金門地方法院", "LCD 福建連江地方法院", "KSY 臺灣高雄少年及家事法院"]
PRINT_DOC = True
#for court in courts:
court = 'HLD 臺灣花蓮地方法院'
print court    
payload = {
    'v_court':court,
    'v_sys':'M',
    'jud_year':'',
    'sel_judword':'常用字別',
    'jud_case':'',
    'jud_no':'',
    'jud_no_end':'',
    'jt':'',
    'dy1':'104',
    'dm1':'1',
    'dd1':'5',
    'dy2':'104',
    'dm2':'1',
    'dd2':'5',
    'jmain1':'',
    'kw':'',
    'keyword':'',
    'sdate':'20150105',
    'edate':'20150105',
    'jud_title':'',
    'jmain':'',
    'Button':' 查詢',
    'searchkw':''
}
'''
keyword = '車禍'
payload = {
    'v_court':court,
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
    'kw':keyword,
    'keyword':keyword,
    'sdate':'',
    'edate':'',
    'jud_title':'',
    'jmain':'',
    'Button':' 查詢',
    'searchkw':keyword
}
'''
headers = {'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY01_1.aspx'}
headers2 = {'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx'}
session = requests.Session()
html = session.post(url, data=payload, headers=headers)
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, "lxml")
#print soup.prettify()
links =  soup.find_all('a', href=re.compile('^FJUDQRY03'))
nextpage_url = url_base+links[0]['href']
print nextpage_url
html_doc = session.get(nextpage_url, headers=headers2)
html_doc.encoding = 'utf-8'
soup_doc = BeautifulSoup(html_doc.text, "lxml")
#print soup_doc.prettify()
doc = soup_doc.pre
if PRINT_DOC:
    print doc
#time.sleep( 1 )

links =  soup_doc.find_all('a', href=re.compile('^FJUDQRY03'))
print len(links)
current_url = nextpage_url 
nextpage_url = url_base+links[0]['href']
print nextpage_url
html_doc = session.get(nextpage_url, headers={'Referer':current_url})
html_doc.encoding = 'utf-8'
soup_doc = BeautifulSoup(html_doc.text, "lxml")
#print soup_doc.prettify()
doc = soup_doc.pre
if PRINT_DOC:
    print doc
links =  soup_doc.find_all('a', href=re.compile('^FJUDQRY03'))
time.sleep( 1 )

print len(links)
while len(links) == 8:
    current_url = nextpage_url 
    nextpage_url = url_base+links[2]['href']
    print nextpage_url
    html_doc = session.get(nextpage_url, headers={'Referer':current_url})
    html_doc.encoding = 'utf-8'
    soup_doc = BeautifulSoup(html_doc.text, "lxml")
    doc = soup_doc.pre
    if PRINT_DOC: 
        print doc
    links =  soup_doc.find_all('a', href=re.compile('^FJUDQRY03'))
    print len(links)
    time.sleep( 1 )
