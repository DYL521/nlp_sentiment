import jieba
from jieba import analyse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1、中文分词
cut_words = ""

for line in open("C-class.txt", encoding='utf-8'):
    line.split("\n")
    seg_list = jieba.cut(line, cut_all=False)
    cut_words += (" ".join(seg_list))

# jieba.load_userdict("userdict.txt")              # 自定义词典
# jieba.analyse.set_stop_words('stop_words.txt')   # 停用词词典

# 提取主题词，返回的词频其实就是TF-IDF
keywords = analyse.extract_tags(
    cut_words,
    topK=50,
    withWeight=True,
    allowPOS=('a', 'e', 'n', 'nr', 'ns', 'v')  # 词性 形容词 叹词 名词 动词
)
# 返回列表
print(keywords)

# 2、数据存储
pd.DataFrame(keywords, columns=['词语', '重要性']).to_excel('TF_IDF关键词前50.xlsx')

# keyword本身包含两列数据
ss = pd.DataFrame(keywords, columns=['词语', '重要性'])
# print(ss)


# # ------------------------------------3、数据可视化------------------------------------
plt.figure(figsize=(10, 6))
plt.title('TF-IDF Ranking')
fig = plt.axes()
plt.barh(range(len(ss.重要性[:25][::-1])), ss.重要性[:25][::-1])
fig.set_yticks(np.arange(len(ss.重要性[:25][::-1])))
# font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc')
fig.set_yticklabels(ss.词语[:25][::-1])
fig.set_xlabel('Importance')
plt.show()
