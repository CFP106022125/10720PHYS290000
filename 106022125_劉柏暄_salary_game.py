#!/usr/bin/env python
# coding: utf-8

# In[117]:


import random
import numpy as np
import matplotlib.pyplot as plt
 
n=1000                           # number of people
k=2000                           # round of paper scissor stone
m=10000                          # money the people have at the start
p=2000                           # the price of win/lose a game
R=np.zeros(n)+1                  # (setting)
N=np.zeros(n)+m                  # money the people have at the start in array mode
while k>=0:                      # the battle has begun!!
    if np.size(N)>=2:            # there must be at least two people to play
        while np.sum(R)!=0:      # decide the result of the game
            for battle in range(0,np.size(N)):
                R[battle]=random.randint(-1,1)
        N=N+R*p
        index=np.where(N<p)      # find the people who does not have enough money to play the next game
        N=np.delete(N,index)     # eliminate!!
        R=np.zeros(np.size(N))+1 # prepare for the mext game
    k=k-1                       
for U in range(0,n-np.size(N)):  # add the people who was eliminated back
    N=np.append(N,0)
plt.hist(N)                      # plot the graph
plt.xlabel('the money a person has')
plt.ylabel('the number of people ')
plt.title("competition's result")


# In[ ]:


print(np.size(R))


# In[ ]:




