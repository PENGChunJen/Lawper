# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

f = open ("data2.txt", "r")
f_string = f.read()
f.close()
text = unicode(f_string, 'utf-8')
print(isinstance(text, unicode))

from snownlp import normal
from snownlp import seg
from snownlp.summary import textrank
from snownlp import SnowNLP




if __name__ == '__main__':

    s = SnowNLP(text)
    print(s.keywords(3))
    print(s.summary(3))
    
    t = normal.zh2hans(text)
    sents = normal.get_sentences(t)
    doc = []
    for sent in sents:
        words = seg.seg(sent)
        words = normal.filter_stop(words)
        doc.append(words)
    rank = textrank.TextRank(doc)
    rank.solve()
    for index in rank.top_index(5):
        print(sents[index])
    keyword_rank = textrank.KeywordTextRank(doc)
    keyword_rank.solve()
    for w in keyword_rank.top_index(5):
        print(w)
