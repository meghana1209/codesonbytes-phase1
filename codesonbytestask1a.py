# -*- coding: utf-8 -*-
"""codesonbytestask1a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zi8Zqp5UZLISbu6UTtCAwqz0BSy7ZyQo
"""

pip install pandas

import pandas as pd

import requests

api_url = "https://jsonplaceholder.typicode.com/posts"

response=requests.get(api_url)

if response.status_code==200:
  data=response.json()
  df=pd.DataFrame(data)
  df.to_csv("posts_dataset.csv",index=False)
  df.to_csv("posts_dataset.csv",index=False)
else:
  print(f"Erorr;{response.status_code}")
