#!/usr/bin/env python
# coding: utf-8

# In[28]:


def fac(i):
    if i == 0:
        return 1
    else:
        return i*fac(i-1)
    
print(fac(4)) #24

