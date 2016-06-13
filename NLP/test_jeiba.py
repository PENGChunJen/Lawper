#encoding=utf8
import jieba
import jieba.analyse
import codecs

jieba.set_dictionary('jieba/extra_dict/dict.txt.big')

text = open('legal_crash.txt', 'rb').read().strip(' \r\n　')
#print "Input：", text 

text = text.replace('　', '').replace(' ', '').replace('\r\n', '').decode('utf8').encode('raw_unicode_escape').replace('\u3000','').decode('raw_unicode_escape').encode('utf8')


seg_list = jieba.cut(text, cut_all=False)
output_text = " ".join(seg_list)
outfile = codecs.open('cut.txt', 'wb', 'utf-8')
for line in output_text:
    outfile.write(line)


#seg_list = jieba.cut_for_search(content)
#print "Output: Search Mode"+" ".join(seg_list)

tags = jieba.analyse.extract_tags(text, 10)
print "Top 10 Keywords：", ",".join(tags)
