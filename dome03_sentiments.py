from snownlp import SnowNLP

s1 = SnowNLP("我今天很开心")
print("s1 情感分数: {}".format(s1.sentiments))


s2 = SnowNLP("我想打人")
print("s2 情感分数: {}".format(s2.sentiments))
