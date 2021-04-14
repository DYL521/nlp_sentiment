from snownlp import SnowNLP

s1 = SnowNLP("我今天很开心")
print("s1 情感分数: {}".format(s1.sentiments))
