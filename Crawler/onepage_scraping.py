# coding=utf-8
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
headers = {'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY01_1.aspx'}
headers2 = {'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx'}
session = requests.Session()
html = session.post(url, data=payload, headers=headers)
html.encoding = 'utf-8'

soup = BeautifulSoup(html.text, "lxml")
#print soup.prettify()
nextpages =  soup.find_all('a', href=re.compile('^FJUDQRY02'))


links =  soup.find_all('a', href=re.compile('^FJUDQRY03'))
for link in links:
    new_url = url_base+link['href']
    print new_url
    html = session.get(new_url, headers=headers2)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, "lxml")
    #print soup.prettify()
    doc = soup.pre
    print doc
