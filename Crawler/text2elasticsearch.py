# -*- coding: utf-8 -*-

import os, fnmatch, re
import elasticsearch
from datetime import date, timedelta

es = elasticsearch.Elasticsearch()
data_path = '../data/crash/'
#es.indices.delete(index='lawper', ignore=[400, 404])
#es.indices.create(index='lawper', ignore=400)

start_date = date(2015,2,1)
end_date = date(2015,2,28)
def dategenerator(start,end):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)

failed_list = open('failed_list_crash', 'wr')
def text2elasticsearch(court, case, date):
    match_filename = date.strftime('%Y-%m-%d')+'_'+court+'_'+case+'_*'
    #print match_filename

    for file_name in os.listdir(data_path):
        if fnmatch.fnmatch(file_name, match_filename):
            #utf8_text = open(data_path+file_name, 'r').read().replace('\r','').decode('utf8')
            #print file_name
            f = open(data_path+file_name, 'r')
            line = f.readline().strip(' \t\n\r').decode('utf8')
            #utf8_id = replace_chinese_numbers(line)
            first_digit_in_string = re.search('\d', line)
            if first_digit_in_string is None:
                line = f.readline().strip(' \t\n\r').decode('utf8')
                first_digit_in_string = re.search('\d', line)
            if first_digit_in_string is None:
                utf8_id = file_name+'_chineseNumberFailure'
                failed_list.write(utf8_id+'\n')
            else:
                utf8_id = line[first_digit_in_string.start():]
            
            utf8_court = courts[court].decode('utf8')
            utf8_case =  cases[case].decode('utf8')
            utf8_text = open(data_path+file_name, 'r').read().decode('utf8')
            doc = {
                'court':utf8_court,
                'case':utf8_case,
                'date':date.strftime('%Y-%m-%d'),
                'text':utf8_text
            }
            #print doc['text']
            #es.index(index = 'lawper', doc_type = 'raw_text', id = utf8_id, body = doc)
            es.index(index = 'lawper', doc_type = 'crash', id = utf8_id, body = doc)
            print file_name, utf8_id


courts = {"TPD":"臺灣臺北地方法院", "SLD":"臺灣士林地方法院", "PCD":"臺灣新北地方法院", "ILD":"臺灣宜蘭地方法院", "KLD":"臺灣基隆地方法院", "TYD":"臺灣桃園地方法院", "SCD":"臺灣新竹地方法院", "MLD":"臺灣苗栗地方法院", "TCD":"臺灣臺中地方法院", "CHD":"臺灣彰化地方法院", "NTD":"臺灣南投地方法院", "ULD":"臺灣雲林地方法院", "CYD":"臺灣嘉義地方法院", "TND":"臺灣臺南地方法院", "KSD":"臺灣高雄地方法院", "HLD":"臺灣花蓮地方法院", "TTD":"臺灣臺東地方法院", "PTD":"臺灣屏東地方法院", "PHD":"臺灣澎湖地方法院", "KMH":"福建高等法院金門分院", "KMD":"福建金門地方法院", "LCD":"福建連江地方法院", "KSY":"臺灣高雄少年及家事法院","TPC":"司法院－刑事補償","TPU":"司法院－訴願決定","TPJ":"司法院職務法庭", "TPS":"最高法院", "TPA":"最高行政法院", "TPP":"公務員懲戒委員會", "TPH":"臺灣高等法院", "TPH":"臺灣高等法院－訴願決定", "TPB":"臺北高等行政法院", "TCB":"臺中高等行政法院", "KSB":"高雄高等行政法院", "IPC":"智慧財產法院", "TCH":"臺灣高等法院 臺中分院","TNH":"臺灣高等法院 臺南分院", "KSH":"臺灣高等法院 高雄分院", "HLH":"臺灣高等法院 花蓮分院"}
cases = {'M':'刑事', 'V':'民事', 'A':'行政', 'P':'公懲'}
for date in dategenerator(start_date, end_date):
    for court in courts:
        for case in cases:
            text2elasticsearch(court, case, date)


