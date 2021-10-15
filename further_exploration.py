#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:49:16 2019

@author: stevenstonaker
"""

import requests

from plotly.graph_objs import Pie
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=stars:>=0&sort=stars&per_page=100'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results
response_dict = r.json()
repo_dicts = response_dict['items']

repo_langs = []
for repo_dict in repo_dicts:
    repo_lang = repo_dict['language']
    repo_langs.append(repo_lang)
    
# Make a visualization.
data = [Pie(labels=repo_langs)]
my_layout = {
        'title': 'Top 100 languages on GitHub',
        'titlefont': {'size': 28},
        }
fig = {'data': data, 'layout': my_layout}
offline.plot(fig)