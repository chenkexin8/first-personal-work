#!/usr/bin/env python
# coding: utf-8

# In[2]:


import jieba
import json

comments= open("comments.json", "r", encoding='utf-8').read()
    
 # 使用精确模式对文本进行分词
words = jieba.lcut(comments) 
    
 # 通过键值对的形式存储词语及其出现的次数
counts = {} 

# 获取停用词
stopwords = [i.strip() for i in open('comments.txt', encoding='utf-8').readlines()]
for word in words:
    # 去除单词和停用词
    if len(word) != 1 and word not in stopwords:
        # 遍历所有词语，每出现一次其对应的值加 1
        counts[word] = counts.get(word, 0) + 1
    else:
        continue
          
# 将键值对转换成列表
items = list(counts.items())

# 根据词语出现的次数进行从大到小排序
items.sort(key=lambda x: x[1], reverse=True)

#print(items)

#对代码进行输出格式调整

List = []
for i in range(len(items)):
    DictList = {}
    word, count = items[i]
    if count >= 10:
        DictList['name'] = word
        DictList['value'] = count
        List.append(DictList)
#print(List)
        
#保存为json数据   
data = {}
data['data'] = List

f = open("jieba.json","w",encoding='utf-8')
json.dump(data, f, ensure_ascii=False, indent=4)
f.close() 


# In[ ]:




