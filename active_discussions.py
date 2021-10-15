#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:49:16 2019

@author: stevenstonaker
"""

import requests
from operator import itemgetter
from plotly import offline

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
            }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

submission_links, submission_comments, submission_titles = [], [], []
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    submission_title = submission_dict['title']
    submission_titles.append(submission_dict['title'])
    print(f"Discussion link: {submission_dict['hn_link']}")
#    submission_url = submission_dict['hn_link']
#    submission_link = f"<a href='{submission_url}'>{submission_title}</a>"
    submission_link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    submission_links.append(submission_link)
    print(f"Comments: {submission_dict['comments']}")
    submission_comments.append(submission_dict['comments'])
    
    
data = [{
        'type': 'bar',
        'x': submission_links,
        'y': submission_comments,
        'hovertext': submission_titles,
        }]
my_layout = {
        'title': 'Most active topics on Hacker News',
        'xaxis': {'title': 'Discussion'},
        'yaxis': {'title': 'Comments'},
        }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='top_hn_submissions.html')