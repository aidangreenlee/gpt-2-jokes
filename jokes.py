#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gpt_2_simple as gpt2
import os
from datetime import datetime


# In[2]:

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='/tf/GPT2/checkpoint/run1')

# In[8]:

jokepath = '/tf/GPT2/'

def genjoke(prefix:str=0, temperature=.7, truncate:bool=True, length=80):
    os.chdir(jokepath)
    if truncate == True:
        truncate2 = '\n'
    else:
        truncate2 = False
    
    gpt2.generate(sess,
                  length=length,
                  temperature=temperature,
                  prefix=prefix,
                  nsamples=1,
                  batch_size=1,
#                  return_as_list=True,
                  truncate=truncate2
                  )
#    gen = gen[0].rsplit('\n',1)[0]
#    gen = gen.split('\n')
    return;
