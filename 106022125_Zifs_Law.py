#!/usr/bin/env python
# coding: utf-8

# In[63]:


fp = open('Alice.txt','r',encoding='UTF-8')
import matplotlib.pyplot as plt
import numpy as np
line = fp.readline()
my_dict={}
#read the first line from the title
while line:
    s=line.split()
    for a in s:
        if a not in my_dict:
            my_dict[a]=1
        else:
            my_dict[a]=my_dict[a]+1    
    line = fp.readline()
fp.close()
x=[]
for key in my_dict:
    x.append(my_dict[key])
x.sort()
x.reverse()
print(len(x))
plt.loglog(range(len(x)),x)
plt.xlabel('Rank of the word')
plt.ylabel('Number of the occurence')
plt.title("Zipf's Law")
plt.show()


# In[ ]:




