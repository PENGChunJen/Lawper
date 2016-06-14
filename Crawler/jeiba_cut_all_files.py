#encoding=utf8
import jieba
import jieba.analyse
import codecs
import os

jieba.set_dictionary('../NLP/jieba/extra_dict/dict.txt.big')
data_path = '../data/raw_text/'
output_file = 'cut_words'
outfile = codecs.open(output_file, 'wb', 'utf-8')

for file_name in os.listdir(data_path):
    print file_name,
    text = open(data_path+file_name, 'rb').read().strip(' \r\n　')
    #print "Input：", text 

    text = text.replace('　', '').replace(' ', '').replace('\r\n', '').decode('utf8', 'ignore').encode('raw_unicode_escape').replace('\u3000','').decode('raw_unicode_escape').encode('utf8')


    seg_list = jieba.cut(text, cut_all=False)
    output_text = " ".join(seg_list)
    for line in output_text:
        outfile.write(line)


#seg_list = jieba.cut_for_search(content)
#print "Output: Search Mode"+" ".join(seg_list)

    tags = jieba.analyse.extract_tags(text, 10)
    print "Top 10 Keywords：", ",".join(tags)
