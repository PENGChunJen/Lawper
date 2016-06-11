
from snownlp import seg
seg.train('data.txt')
seg.save('seg.marshal')
#from snownlp import tag
#tag.train('199801.txt')
#tag.save('tag.marshal')
#from snownlp import sentiment
#sentiment.train('neg.txt', 'pos.txt')
#sentiment.save('sentiment.marshal')
