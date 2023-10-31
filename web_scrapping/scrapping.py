#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from bs4 import BeautifulSoup
import csv
import os


# In[ ]:


rows = []
url = 'https://www.acefitness.org/resources/everyone/blog/1995/do-bodybuilding-supplements-work/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all paragraphs
paragraphs = soup.find_all('p')

# Extract text from each paragraph and join them into a single string
text = ' '.join([p.text for p in paragraphs])

for data in text:
    rows.append(rows)


df = pd.DataFrame(rows)
df.to_csv('/Users/sbp/Downloads/ScrappedData.csv', index=False)
print('Process completed successfully!')


