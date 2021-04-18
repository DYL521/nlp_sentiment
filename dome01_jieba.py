from snownlp import SnowNLP
import time
from collections import Counter

# 1、简单使用
s1 = SnowNLP("这本书质量真不太好!")
print("SnowNLP：{}".format(s1.words))

import jieba

s2 = jieba.cut(u"这本书的质量太不好了！", cut_all=False)
print("jieba: {}".format(list(s2)))

# 2、 简单中文分词

cut_words = ""
all_words = ""
f = open("C-class-fenci.txt", "w")
for line in open('C-class.txt', encoding='utf-8'):
    line.split('\n')
    seg_list = jieba.cut(line, cut_all=False)
    cut_words = (" ".join(seg_list))
    f.write(cut_words)
    all_words += cut_words
else:
    f.close()

# 输出结果：
all_words = all_words.split()
print(all_words)

# 词频统计
c = Counter()
for x in all_words:
    if len(x) > 1 and x != '\r\n':
        c[x] += 1

# 输出词频最高的前10个词
print('\n词频统计结果：')
for (k, v) in c.most_common(10):
    print("%s:%d" % (k, v))

# 存储数据
name = time.strftime("%Y-%m-%d") + "-fc.csv"
fw = open(name, 'w', encoding='utf-8')
i = 1
for (k, v) in c.most_common(len(c)):
    fw.write(str(i) + ',' + str(k) + ',' + str(v) + '\n')
    i = i + 1
else:
    print("Over write file!")
    fw.close()
