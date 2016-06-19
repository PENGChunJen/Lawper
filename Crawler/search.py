# -*- coding: utf-8 -*-
import gensim
import json
import elasticsearch
import codecs
import jieba
import jieba.analyse
model = gensim.models.Word2Vec.load("cut_words.model")
X = model.syn0

def search(rawinput):
    courts = {"TPD":"臺灣臺北地方法院", "SLD":"臺灣士林地方法院", "PCD":"臺灣新北地方法院", "ILD":"臺灣宜蘭地方法院", "KLD":"臺灣基隆地方法院", "TYD":"臺灣桃園地方法院", "SCD":"臺灣新竹地方法院", "MLD":"臺灣苗栗地方法院", "TCD":"臺灣臺中地方法院", "CHD":"臺灣彰化地方法院", "NTD":"臺灣南投地方法院", "ULD":"臺灣雲林地方法院", "CYD":"臺灣嘉義地方法院", "TND":"臺灣臺南地方法院", "KSD":"臺灣高雄地方法院", "HLD":"臺灣花蓮地方法院", "TTD":"臺灣臺東地方法院", "PTD":"臺灣屏東地方法院", "PHD":"臺灣澎湖地方法院", "KMH":"福建高等法院金門分院", "KMD":"福建金門地方法院", "LCD":"福建連江地方法院", "KSY":"臺灣高雄少年及家事法院","TPC":"司法院－刑事補償","TPU":"司法院－訴願決定","TPJ":"司法院職務法庭", "TPS":"最高法院", "TPA":"最高行政法院", "TPP":"公務員懲戒委員會", "TPH":"臺灣高等法院", "TPH":"臺灣高等法院－訴願決定", "TPB":"臺北高等行政法院", "TCB":"臺中高等行政法院", "KSB":"高雄高等行政法院", "IPC":"智慧財產法院", "TCH":"臺灣高等法院 臺中分院","TNH":"臺灣高等法院 臺南分院", "KSH":"臺灣高等法院 高雄分院", "HLH":"臺灣高等法院 花蓮分院"}
    cases = {'M':'刑事', 'V':'民事', 'A':'行政', 'P':'公懲'}
    
    es = elasticsearch.Elasticsearch()
    scroll_filter=['_scroll_id', 'hits.total', 'hits.max_score', 'hits.hits._id','hits.hits._score', 'hits.hits._source.court', 'hits.hits._source.case', 'hits.hits._source.date' ]
    filter=['hits.total', 'hits.max_score', 'hits.hits._id','hits.hits._score', 'hits.hits._source.court', 'hits.hits._source.case', 'hits.hits._source.date' ]
    filter_text=['hits.total', 'hits.max_score', 'hits.hits._id','hits.hits._score', 'hits.hits._source.court', 'hits.hits._source.case', 'hits.hits._source.date', 'hits.hits._source.text' ]
    
    DEBUG = False 
    print "raw input: "+ rawinput
    #seg_list = jieba.cut(rawinput, cut_all = False)
    #print " ".join(seg_list)
    tags = jieba.analyse.extract_tags(rawinput, 5)
    print "keyword: ", ", ".join(tags)
    keyword = tags[0]
    #keyword = u'車禍'
    #keyword = u'竊盜'
    #keyword = u'詐欺'
    #keyword = u'侮辱'
    
    keywords = model.most_similar(keyword, topn=5)
    
    match_keywords = []
    for tag in tags:
        match_keywords.append({'match_phrase':{'text':tag}})
    for k in keywords:
        match_keywords.append({'match_phrase':{'text':k[0]}})
    
    print "keyword: "+keyword+' , related keywords:',
    for word in match_keywords:
        print word['match_phrase']['text'],
    print ''
    
    pattern = {
      'query': {
        'bool': {
          'must':{'match_phrase':{'text':keyword}},
          'should':match_keywords
        }
      }
    }
    page = es.search(
        index = 'lawper',
        doc_type = 'raw_text',
        #doc_type = 'crash',
        #filter_path = scroll_filter,
        scroll = '2m',
        search_type = 'scan',
        size = 5,
        body = pattern
        )
    sid = page['_scroll_id']
    scroll_size = page['hits']['total']
    print "total: " + str(scroll_size)
    data = []
    
    while (scroll_size > 0):
        print "Scrolling"
        page = es.scroll(scroll_id = sid, scroll = '2m')
        #print json.dumps(page, ensure_ascii=False, indent=4)
        sid = page['_scroll_id']
        scroll_size = len(page['hits']['hits'])
        print "scroll size: " + str(scroll_size)
    
        for item in page['hits']['hits']:
            print item['_id']
            t = item['_source']['text']
            from jeiba_cut_similar_sentence import extract_sentences
            sentences = extract_sentences(t.encode('utf8'))
        
            j = {
                'id':item['_id'], 
                'date':item['_source']['date'],
                'court':item['_source']['court'],
                'case':item['_source']['case'],
                'sentences':sentences
            }
            if DEBUG:
                print json.dumps(j, ensure_ascii=False, encoding='utf8', indent=4)
                print t 
            data.append(j)
    
    
    outfile = codecs.open('output.json', 'wb', 'utf-8')
    json.dump(data, outfile, ensure_ascii=False, encoding='utf8', indent=4)
    return data
#rawinput = u'宜蘭的車禍被告'
#rawinput = u'侮辱 和解 被告'
#rawinput = u'車禍'
#rawinput = u'竊盜'
#rawinput = u'詐欺'
#rawinput = u'侮辱'
#search(rawinput)
