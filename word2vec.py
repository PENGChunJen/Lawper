from gensim.models import word2vec

word2vec.word2vec('cut_words', 'cut_words.bin', size=100, verbose=True)
word2vec.word2vcluster('cut_words', 'cut_words_clusters.text', size=100, verbose=True)

model = word2vec.load('cut_words.bin')
print model.vectors.shape
