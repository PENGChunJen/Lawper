# -*- coding: utf-8 -*-
import gensim
import re
import jieba
model = gensim.models.Word2Vec.load("cut_words.model")
X = model.syn0

def print_similar_words(keyword):
    print 'Most similar words of '+keyword + ':',
    words = model.most_similar(keyword)
    for word in words:
        print word[0]+',',
    print ''

def find_sentence(keyword, text):
    p = ' '+keyword+ur' (.*?)。'
    pattern = re.compile(p, re.UNICODE)
    sentences = re.findall(pattern, text)
    return sentences

def print_similar_sentence(keyword, text):
    sentences = find_sentence(keyword, text)
    #print "keyword:", keyword
    if sentences:
    #    print "keyword:", keyword
        for s in sentences:
            print '\t'+keyword.encode('utf8')+s.replace(' ','').encode('utf8')+'。\n'

def print_all_similar_sentences(keyword, text):
    print_similar_sentence(keyword, text)
    keywords = model.most_similar(keyword)
    #keywords = model.most_similar(keyword, topn=5)
    for keyword in keywords:
        print_similar_sentence(keyword[0], text)

def print_extract_sentences(text):
    text = text.replace('　', '').replace(' ', '').replace('\r\n', '').decode('utf8', 'ignore').encode('raw_unicode_escape').replace('\u3000','').decode('raw_unicode_escape')
    seg_list = jieba.cut(text, cut_all=False)
    text = " ".join(seg_list)

    keyword = u"查"
    print_all_similar_sentences(keyword, text)
    keyword = u"按"
    print_all_similar_sentences(keyword, text)
    keyword = u"惟"
    print_all_similar_sentences(keyword, text)
    keyword = u"核"
    print_all_similar_sentences(keyword, text)

def extract_sentences(text):
    sentences = []
    text = text.replace('　', '').replace(' ', '').replace('\r\n', '').decode('utf8', 'ignore').encode('raw_unicode_escape').replace('\u3000','').decode('raw_unicode_escape')
    seg_list = jieba.cut(text, cut_all=False)
    text = " ".join(seg_list)

    keyword = u"查"
    ss = find_sentence(keyword, text)
    if ss:
        for s in ss:
            sentence = keyword.encode('utf8')+s.replace(' ','').encode('utf8')+'。'
            sentences.append(sentence.decode('utf8'))
    
    #keywords = model.most_similar(keyword)
    keywords = model.most_similar(keyword, topn=9)
    for keyword in keywords:
        ss = find_sentence(keyword[0], text)
        if ss:
            for s in ss:
                sentence = keyword[0].encode('utf8')+s.replace(' ','').encode('utf8')+'。'
                sentences.append(sentence.decode('utf8'))
    
    keyword = u"按"
    ss = find_sentence(keyword, text)
    if ss:
        for s in ss:
            sentence = keyword.encode('utf8')+s.replace(' ','').encode('utf8')+'。'
            find_forbidden = sentence.decode('utf8').find(u"切勿逕送上級法院")
            if find_forbidden != -1: 
                #print 'find', find_forbidden
                continue
            find_forbidden = sentence.decode('utf8').find(u"按年利率")
            if find_forbidden != -1: 
                #print 'find', find_forbidden
                continue
            find_forbidden = sentence.decode('utf8').find(u"按年息")
            if find_forbidden != -1: 
                #print 'find', find_forbidden
                continue
            sentences.append(sentence.decode('utf8'))
    
    #keywords = model.most_similar(keyword)
    keywords = model.most_similar(keyword, topn=1)
    for keyword in keywords:
        ss = find_sentence(keyword[0], text)
        if ss:
            for s in ss:
                sentence = keyword[0].encode('utf8')+s.replace(' ','').encode('utf8')+'。'
                sentences.append(sentence.decode('utf8'))
   
    keyword = u"惟"
    ss = find_sentence(keyword, text)
    if ss:
        for s in ss:
            sentence = keyword.encode('utf8')+s.replace(' ','').encode('utf8')+'。'
            sentences.append(sentence.decode('utf8'))
    
    #keywords = model.most_similar(keyword)
    keywords = model.most_similar(keyword, topn=5)
    for keyword in keywords:
        ss = find_sentence(keyword[0], text)
        if ss:
            for s in ss:
                sentence = keyword[0].encode('utf8')+s.replace(' ','').encode('utf8')+'。'
                sentences.append(sentence.decode('utf8'))
    
    keyword = u"核"
    ss = find_sentence(keyword, text)
    if ss:
        for s in ss:
            sentence = keyword.encode('utf8')+s.replace(' ','').encode('utf8')+'。'
            sentences.append(sentence.decode('utf8'))
    
    return sentences 

#text = open('../data/2015-02-02_TCD_M_13', 'rb').read()
#text = open('../data/2015-01-08_PCD_M_89', 'rb').read()
#text = open('../data/2015-02-02_KSD_M_22', 'rb').read()
#print_extract_sentences(text)

#for s in extract_sentences(text):
#    print s
