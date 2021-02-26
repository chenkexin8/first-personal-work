#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import requests



headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

### 准备工作
comment = []
comments= []
data='1613891192468'
cursor='0'

for i in range(0,1269):
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+cursor+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+data
    source = requests.get(url, headers=headers).content.decode()
    comment= re.findall('content":"(.*?),"',source,re.S)
    comments.append(comment)
    cursor=re.findall('"last":"(.*?)"',source,re.S)[0].replace("\n","").replace(" ","")
    data=str(int(data)+1)
#print(comments)
    
# ### 3. 将提取评论保存
f = open("comments.txt","w",encoding='utf-8')
for list1 in comments:
        for comment in list1:
            f.write(comment)
            f.write('\n')
f.close()
#print(comments)


# In[ ]:




