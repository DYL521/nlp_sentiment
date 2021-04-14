from snownlp import SnowNLP

s1 = SnowNLP("这本书质量真不太好!")
print("SnowNLP：{}".format(s1.words))

import jieba

s2 = jieba.cut(u"这本书的质量太不好了！", cut_all=False)
print("jieba: {}".format(list(s2)))
