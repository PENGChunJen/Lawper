# coding=utf-8
import time
import re
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta


h={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'en-US,en;q=0.8,fr;q=0.6,zh-TW;q=0.4,zh;q=0.2',
'Connection':'keep-alive',
'Cookie':'FJUDQRY01_1=16/1/0/0/0/0//0/////104/1/5/104/1/5/////20150105/20150105/////; ASP.NET_SessionId=dh31kh55ug5csv45ijqioeq3; BNES_ASP.NET_SessionId=e81nkgtN//5jXvMUYvtTOo83dIdXLBMzVw+mWIsCf+ZI68bHG7XlRIhWaGxOxz/xLOpIX+qv6k27qA51sJXoZ+KTI28bsVYIQo95P6XO8aE=; ASPSESSIONIDAADDBQSB=AIBMIBGDPGDEKDNODDNJCDDO; BNES_ASPSESSIONIDAADDBQSB=2WuHQ1x2im7INby/NRcYhKJ7uB3sIyR4HBx7/I4SB6DsPqCX/CN90D5fKK8WOyE60omo+bw7SZJR6/o3Ol6jl+IQuP7un8m5Zb5GoEV36EYPdnNxCCsrGg==',
'Host':'jirs.judicial.gov.tw',
'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

def dategenerator(start,end):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)

def run(payload):
    session = requests.Session()
    html = session.post(url, data=payload, headers={'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY01_1.aspx'})
    html.encoding = 'utf-8'
    
    soup = BeautifulSoup(html.text, "lxml")
    #print soup.prettify()
    links =  soup.find_all('a', href=re.compile('^FJUDQRY03'))
    if not links:
        return 
    nextpage_url = url_base+links[0]['href']
    print nextpage_url
    #html_doc = session.get(nextpage_url, headers={'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx'})
    html_doc = session.get(nextpage_url, headers=h)
    html_doc.encoding = 'utf-8'
    print 'html_doc.headers'
    print html_doc.headers
    print
    print 'html_doc.request.headers'
    print html_doc.request.headers

    soup_doc = BeautifulSoup(html_doc.text, "lxml")
    soup_doc.encoding = 'utf-8'
    print soup_doc.prettify()
    doc = soup_doc.pre.get_text()
    if PRINT_DOC:
        print doc
    #time.sleep( 1 )
    
    links =  soup_doc.find_all('a', href=re.compile('^FJUDQRY03'))
    if not links:
        return 
    print len(links)
    current_url = nextpage_url 
    nextpage_url = url_base+links[0]['href']
    print nextpage_url
    html_doc = session.get(nextpage_url, headers={'Referer':current_url})
    html_doc.encoding = 'utf-8'
    soup_doc = BeautifulSoup(html_doc.text, "lxml")
    #print soup_doc.prettify()
    doc = soup_doc.pre.get_text()
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
        doc = soup_doc.pre.get_text()
        if PRINT_DOC: 
            print doc
        links =  soup_doc.find_all('a', href=re.compile('^FJUDQRY03'))
        print len(links)
        time.sleep( 1 )



PRINT_DOC = True 
#PRINT_DOC = False 
url = 'http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx'
url_base = 'http://jirs.judicial.gov.tw/FJUD/'
#courts = ["TPC 司法院－刑事補償", "TPU 司法院－訴願決定", "TPJ 司法院職務法庭", "TPS 最高法院", "TPA 最高行政法院", "TPP 公務員懲戒委員會", "TPH 臺灣高等法院", "TPH 臺灣高等法院－訴願決定", "TPB 臺北高等行政法院", "TCB 臺中高等行政法院", "KSB 高雄高等行政法院", "IPC 智慧財產法院", "TCH 臺灣高等法院 臺中分院", "TNH 臺灣高等法院 臺南分院", "KSH 臺灣高等法院 高雄分院", "HLH 臺灣高等法院 花蓮分院", "TPD 臺灣臺北地方法院", "SLD 臺灣士林地方法院", "PCD 臺灣新北地方法院", "ILD 臺灣宜蘭地方法院", "KLD 臺灣基隆地方法院", "TYD 臺灣桃園地方法院", "SCD 臺灣新竹地方法院", "MLD 臺灣苗栗地方法院", "TCD 臺灣臺中地方法院", "CHD 臺灣彰化地方法院", "NTD 臺灣南投地方法院", "ULD 臺灣雲林地方法院", "CYD 臺灣嘉義地方法院", "TND 臺灣臺南地方法院", "KSD 臺灣高雄地方法院", "HLD 臺灣花蓮地方法院", "TTD 臺灣臺東地方法院", "PTD 臺灣屏東地方法院", "PHD 臺灣澎湖地方法院", "KMH 福建高等法院金門分院", "KMD 福建金門地方法院", "LCD 福建連江地方法院", "KSY 臺灣高雄少年及家事法院"]
courts = ["TPD 臺灣臺北地方法院"]#, "SLD 臺灣士林地方法院", "PCD 臺灣新北地方法院", "ILD 臺灣宜蘭地方法院", "KLD 臺灣基隆地方法院", "TYD 臺灣桃園地方法院", "SCD 臺灣新竹地方法院", "MLD 臺灣苗栗地方法院", "TCD 臺灣臺中地方法院", "CHD 臺灣彰化地方法院", "NTD 臺灣南投地方法院", "ULD 臺灣雲林地方法院", "CYD 臺灣嘉義地方法院", "TND 臺灣臺南地方法院", "KSD 臺灣高雄地方法院", "HLD 臺灣花蓮地方法院", "TTD 臺灣臺東地方法院", "PTD 臺灣屏東地方法院", "PHD 臺灣澎湖地方法院", "KMH 福建高等法院金門分院", "KMD 福建金門地方法院", "LCD 福建連江地方法院", "KSY 臺灣高雄少年及家事法院"]
cases = [['M','刑事'], ['V','民事'], ['A','行政'], ['P','公懲']]
#cases = [['V','民事'], ['A','行政'], ['P','公懲']]
start_date = date(2015,1,5)
end_date = date(2015,1,5)
keyword = ''
#keyword = '車禍'
for d in dategenerator(start_date, end_date):
    for court in courts:
        for case in cases:
            print d.strftime('%Y/%m/%d') + '-' + court + '-' + case[1]    
            payload = {
                'v_court':court,
                'v_sys':case[0],
                'jud_year':'',
                'sel_judword':'常用字別',
                'jud_case':'',
                'jud_no':'',
                'jud_no_end':'',
                'jt':'',
                'dy1':str( int(d.strftime('%Y'))-1911 ),
                'dm1':d.strftime('%m'),
                'dd1':d.strftime('%d'),
                'dy2':str( int(d.strftime('%Y'))-1911 ),
                'dm2':d.strftime('%m'),
                'dd2':d.strftime('%d'),
                'jmain1':'',
                'kw':keyword,
                'keyword':keyword,
                'sdate':d.strftime('%Y%m%d'),
                'edate':d.strftime('%Y%m%d'),
                'jud_title':'',
                'jmain':'',
                'Button':' 查詢',
                'searchkw':keyword
            }
            run(payload)
