# coding=utf-8
import requests
from bs4 import BeautifulSoup

payload = {
'v_court':'TPD 臺灣臺北地方法院',
'v_sys':'M',
'jud_year':'',
'sel_judword':'常用字別',
'jud_case':'',
'jud_no':'',
'jud_no_end':'',
'jt':'',
'dy1':'105',
'dm1':'1',
'dd1':'1',
'dy2':'105 ',
'dm2':'4',
'dd2':'31',
'jmain1':'',
'kw':'竊盜',
'keyword':'竊盜',
'sdate':'20160101',
'edate':'20160431',
'jud_title':'',
'jmain':'',
'Button':' 查詢',
'searchkw':'竊盜'
}
res = requests.post("http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx", data = payload)
res.encoding = 'utf-8'
print res.text

soup = BeautifulSoup(res.text, "html-parser")
#print soup.text
#print soup.contents
#print soup.select('html')[0]
print soup.select('#title') 	# id="title"
#print soup.select('.link')  	# class="link"
