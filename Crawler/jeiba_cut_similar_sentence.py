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

def find_sentence(keyword):
    p = ' '+keyword+ur' (.*?)。'
    pattern = re.compile(p, re.UNICODE)
    sentences = re.findall(pattern, text)
    return sentences

def print_similar_sentence(keyword):
    sentences = find_sentence(keyword)
    if sentences:
        print "keyword:", keyword
        for s in sentences:
            print '\t'+keyword.encode('utf8')+s.replace(' ','').encode('utf8')+'。\n'

def print_all_similar_sentences(keyword):
    print_similar_sentence(keyword)
    keywords = model.most_similar(keyword)
    #keywords = model.most_similar(keyword, topn=5)
    for keyword in keywords:
        print_similar_sentence(keyword[0])


text = open('../data/crash_JAN/2015-01-08_TYD_M_3', 'rb').read()
text = text.replace('　', '').replace(' ', '').replace('\r\n', '').decode('utf8', 'ignore').encode('raw_unicode_escape').replace('\u3000','').decode('raw_unicode_escape')
seg_list = jieba.cut(text, cut_all=False)
text = " ".join(seg_list)


keyword = u"查"
print_all_similar_sentences(keyword)
keyword = u"按"
print_all_similar_sentences(keyword)
