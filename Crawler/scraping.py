# coding=utf-8
import gc
import time
import re
import requests
import os.path
import codecs
from bs4 import BeautifulSoup
from datetime import date, timedelta
import cPickle as pickle

#data_path = '../data/'
data_path = '../data/HighCourt/'

def dategenerator(start,end):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)

def run(payload, filename):
    session = requests.Session()
    count = 0
    html = session.post(url, data=payload, headers={'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY01_1.aspx'})
    html.encoding = 'utf-8'
    
    soup = BeautifulSoup(html.text, "lxml")
    #print soup.prettify()
    links =  soup.find_all('a', href=re.compile('^FJUDQRY03'))
    if not links:
        session.post(url, headers={'Connection':'close'})
        del soup, session
        gc.collect()
        return count
    nextpage_url = url_base+links[0]['href']
    #print nextpage_url
    html_doc = session.get(nextpage_url, headers={'Referer':'http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx'})
    html_doc.encoding = 'utf-8'
    soup_doc = BeautifulSoup(html_doc.text, "lxml")
    if soup_doc.pre is None:
        print html_doc.text
        session.post(nextpage_url, headers={'Connection':'close'})
        del html_doc, soup_doc, session
        gc.collect()
        return count
    else:
        doc = soup_doc.pre.get_text()
        count = count+1
        outfile_name = filename+'_'+str(count)
        outfile = codecs.open(data_path+outfile_name, 'wb', 'utf-8')
        outfile.write(doc)
        outfile.close()
        if PRINT_DOC:
            print doc
    time.sleep( 1 )
    
    links =  soup_doc.find_all('a', href=re.compile('^FJUDQRY03'))
    if not links:
        return count
    #print len(links)
    current_url = nextpage_url 
    nextpage_url = url_base+links[0]['href']
    #print nextpage_url
    html_doc = session.get(nextpage_url, headers={'Referer':current_url})
    html_doc.encoding = 'utf-8'
    soup_doc = BeautifulSoup(html_doc.text, "lxml")
    if soup_doc.pre is None:
        print html_doc.text
        session.post(nextpage_url, headers={'Connection':'close'})
        del html_doc, soup_doc, session
        gc.collect()
        return count
    else:
        doc = soup_doc.pre.get_text()
        count = count+1
        outfile_name = filename+'_'+str(count)
        outfile = codecs.open(data_path+outfile_name, 'wb', 'utf-8')
        outfile.write(doc)
        outfile.close()
        if PRINT_DOC:
            print doc
    links =  soup_doc.find_all('a', href=re.compile('^FJUDQRY03'))
    time.sleep( 1 )
    
    #print len(links)
    while len(links) == 8:
        current_url = nextpage_url 
        nextpage_url = url_base+links[2]['href']
        #print nextpage_url
        html_doc = session.get(nextpage_url, headers={'Referer':current_url})
        html_doc.encoding = 'utf-8'
        soup_doc = BeautifulSoup(html_doc.text, "lxml")
        
        if soup_doc.pre is None:
            print html_doc.text
            session.post(nextpage_url, headers={'Connection':'close'})
            del html_doc, soup_doc, session
            gc.collect()
            return count
        else:
            doc = soup_doc.pre.get_text()
            count = count+1
            outfile_name = filename+'_'+str(count)
            outfile = codecs.open(data_path+outfile_name, 'wb', 'utf-8')
            outfile.write(doc)
            outfile.close()
            if PRINT_DOC:
                print doc
        
        links =  soup_doc.find_all('a', href=re.compile('^FJUDQRY03'))
        #print len(links)
        time.sleep( 1 )

    session.post(nextpage_url, headers={'Connection':'close'})
    del html_doc, soup_doc, session
    gc.collect()
    return count

#PRINT_DOC = True 
PRINT_DOC = False 
url = 'http://jirs.judicial.gov.tw/FJUD/FJUDQRY02_1.aspx'
url_base = 'http://jirs.judicial.gov.tw/FJUD/'
#courts = ["TPC 司法院－刑事補償", "TPU 司法院－訴願決定", "TPJ 司法院職務法庭", "TPS 最高法院", "TPA 最高行政法院", "TPP 公務員懲戒委員會", "TPH 臺灣高等法院", "TPH 臺灣高等法院－訴願決定", "TPB 臺北高等行政法院", "TCB 臺中高等行政法院", "KSB 高雄高等行政法院", "IPC 智慧財產法院", "TCH 臺灣高等法院 臺中分院", "TNH 臺灣高等法院 臺南分院", "KSH 臺灣高等法院 高雄分院", "HLH 臺灣高等法院 花蓮分院", "TPD 臺灣臺北地方法院", "SLD 臺灣士林地方法院", "PCD 臺灣新北地方法院", "ILD 臺灣宜蘭地方法院", "KLD 臺灣基隆地方法院", "TYD 臺灣桃園地方法院", "SCD 臺灣新竹地方法院", "MLD 臺灣苗栗地方法院", "TCD 臺灣臺中地方法院", "CHD 臺灣彰化地方法院", "NTD 臺灣南投地方法院", "ULD 臺灣雲林地方法院", "CYD 臺灣嘉義地方法院", "TND 臺灣臺南地方法院", "KSD 臺灣高雄地方法院", "HLD 臺灣花蓮地方法院", "TTD 臺灣臺東地方法院", "PTD 臺灣屏東地方法院", "PHD 臺灣澎湖地方法院", "KMH 福建高等法院金門分院", "KMD 福建金門地方法院", "LCD 福建連江地方法院", "KSY 臺灣高雄少年及家事法院"]
#courts = ["TPD 臺灣臺北地方法院", "SLD 臺灣士林地方法院", "PCD 臺灣新北地方法院", "ILD 臺灣宜蘭地方法院", "KLD 臺灣基隆地方法院", "TYD 臺灣桃園地方法院", "SCD 臺灣新竹地方法院", "MLD 臺灣苗栗地方法院", "TCD 臺灣臺中地方法院", "CHD 臺灣彰化地方法院", "NTD 臺灣南投地方法院", "ULD 臺灣雲林地方法院", "CYD 臺灣嘉義地方法院", "TND 臺灣臺南地方法院", "KSD 臺灣高雄地方法院", "HLD 臺灣花蓮地方法院", "TTD 臺灣臺東地方法院", "PTD 臺灣屏東地方法院", "PHD 臺灣澎湖地方法院", "KMH 福建高等法院金門分院", "KMD 福建金門地方法院", "LCD 福建連江地方法院", "KSY 臺灣高雄少年及家事法院","TPC 司法院－刑事補償", "TPU 司法院－訴願決定", "TPJ 司法院職務法庭", "TPS 最高法院", "TPA 最高行政法院", "TPP 公務員懲戒委員會", "TPH 臺灣高等法院", "TPH 臺灣高等法院－訴願決定", "TPB 臺北高等行政法院", "TCB 臺中高等行政法院", "KSB 高雄高等行政法院", "IPC 智慧財產法院", "TCH 臺灣高等法院 臺中分院", "TNH 臺灣高等法院 臺南分院", "KSH 臺灣高等法院 高雄分院", "HLH 臺灣高等法院 花蓮分院"]
#courts = ['TPS 最高法院']
courts = ["TPS 最高法院", "TPA 最高行政法院", "TPH 臺灣高等法院", "TPB 臺北高等行政法院", "TCB 臺中高等行政法院", "KSB 高雄高等行政法院", "IPC 智慧財產法院", "TCH 臺灣高等法院 臺中分院", "TNH 臺灣高等法院 臺南分院", "KSH 臺灣高等法院 高雄分院", "HLH 臺灣高等法院 花蓮分院", "KMH 福建高等法院金門分院", "KSY 臺灣高雄少年及家事法院"]
cases = [['M','刑事'], ['V','民事'], ['A','行政'], ['P','公懲']]
start_date = date(2015,1,1)
end_date = date(2015,1,31)
keyword = ''
#keyword = '車禍'
total_doc_num = 0
for d in dategenerator(start_date, end_date):
    for court in courts:
        for case in cases:
            #filename = d.strftime('%Y/%m/%d') + '_' + court + '_' + case[1],    
            filename = d.strftime('%Y-%m-%d') + '_' + str(court[0])+str(court[1])+str(court[2]) + '_' + str(case[0])
            print filename,
              
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
            doc_num = run(payload,str(filename))
            total_doc_num = total_doc_num + doc_num
            print '#document = '+str(doc_num),
            print "total = "+str(total_doc_num)
            #time.sleep( 1 )
    
