#!/usr/bin/env python
# coding: utf-8

# #### 전복
# 
# https://archive.ics.uci.edu/ml/datasets/Abalone
# 
# data url : https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/
# 
# 1. [함수] requests 패키지를 이용해 데이터 가져와서 ndarray로 변환
# 
# 2. [함수] 성별이 'M'인 데이터를 필터, Length와 Diameter 간 상관도를 반환
# 
# 3. __name__ 값이 __main__이면, 1, 2 함수를 실행, 2번 함수의 반환 값을 프린트
# 
# bonus:
# sqlite3 데이이터베이스 생성.
# 
# 참고 : 
# 
# 테이블 DDL
#     create table abalone(
#         length number,
#         diamter number
#     );

# In[3]:


import requests
import numpy as np


# In[13]:


def fetch_uci_data(url):
    d = requests.get(url)
    t = []
    for line in d.text.split('\n'):
        if len(line) != 0:
            t.append(line.split(','))

    # len_check = set()
    # for e in t:
    #     if(len(e) == 1):
    #         print(e)
    #     len_check.add(len(e))
    # print(len_check)

    return np.array(t)

def get_corr(d):
    male_filter = (d[:, 0] == 'M')
    male_samples = d[male_filter]
    male_length = male_samples[:, 1].astype(np.float64)
    male_diameter = male_samples[:, 2].astype(np.float64)
    return np.corrcoef(male_length, male_diameter)


# In[16]:


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'

if __name__ == '__main__':
    np_data = fetch_uci_data(url)
    corr_value = get_corr(np_data)
    print(corr_value)
    print(corr_value[0, 1])

