#!/usr/bin/env python
# coding: utf-8

# In[19]:


#待ち行列(キュー,queue)の実装

from collections import deque

q = deque()

q.append(5) #[5]
q.append(2) #[5, 2]
q.append(3) #[5, 2, 3]
q.append(7) #[5, 2, 3, 7]
q.popleft() #[2, 3, 7]
q.append(1) #[2, 3, 7, 1]
q.append(4) #[2, 3, 7, 1, 4]
q.popleft() #[3, 7, 1, 4]

q.reverse() #[4, 1, 7, 3]

print(list(q))

