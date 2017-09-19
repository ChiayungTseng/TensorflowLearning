import urllib.parse
import requests
import jieba as jb
import json
import jieba.posseg as pseg
params = urllib.parse.urlencode({'bookid': 474872, 'p': 12, 'bacon': 0})
url = "https://pay.3g.cn/book60/WeChat/Book/read?%s" % params

r=requests.request('GET',url)
obj=r.json()

str=obj['jsonList'][0]
book=json.loads(str)
content=book['content']
splictWords=jb.cut(content)
# print("/".join(splictWords))
words=pseg.cut(content)
list=[]
for word,flag in words:
    print('%s %s' % (word,flag),end='')
    if flag=='n'or flag=='nr'or flag=='v':
        list.append(word)
print()
for l in list:
    print(l,end='')
# print(json()['content'])
