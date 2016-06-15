# -*- coding: utf-8 -*-
import gensim
model = gensim.models.Word2Vec.load("cut_words.model")
X = model.syn0
words = model.most_similar(u"查")
for word in words:
    print word[0].encode('utf8')
words = model.most_similar(u"按")
for word in words:
    print word[0].encode('utf8')
words = model.most_similar(u"車禍")
for word in words:
    print word[0].encode('utf8')
# print (type(X))
# print (X.shape)
