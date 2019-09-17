#!/usr/bin/env python
# coding: utf-8

# In[2]:


import urllib.request
import csv
import codecs
from datetime import datetime
import logging
import argparse
import sys
import re

def downloadDATA(url):
    """
    """
    print(url)
    csvstream = urllib.request.urlopen(url)
    csv_data = csv.reader(codecs.iterdecode(csvstream, 'utf-8'))
    data = list(csv_data)
    return data

def searchForImageHits(csv_data):
    total_lines = 0
    matched_lines = 0
    for line in csv_data:
        total_lines+=1
        pattern = r'(.*jpg|.*gif|.*png)'
        if re.match(pattern, line[0], re.I):
            matched_lines+=1
    print(f"Image requests account for {(matched_lines/total_lines)*100}% of all requests.")

def findMostPopularBrowser(csv_data):
    browsers = {'Internet': 0, 'Firefox': 0, 'Chrome': 0, 'Safari': 0}
    i_pattern = r'(.*Internet.*)'
    f_pattern = r'(.*Firefox.*)'
    c_pattern = r'(.*Chrome.*)'
    s_pattern = r'(.*Safari.*)'
    for line in csv_data:
        if re.match(i_pattern, line[2]):
            browsers['Internet']+=1
        if re.match(f_pattern, line[2]):
            browsers['Firefox']+=1
        if re.match(c_pattern, line[2]):
            browsers['Chrome']+=1
        if re.match(s_pattern, line[2]):
            browsers['Safari']+=1
    max_value = max(browsers.values())
    max_keys = [k for k, v in browsers.items() if v == max_value]
    print(f"{max_keys[0]} has {max_value} hits.")

def totalHitsHour(csv_data):
    in_hour = {}
    for line in csv_data:
        date_object = datetime.strptime(line[1], '%Y-%m-%d %H:%M:%S')
        if date_object.hour in in_hour.keys():
            in_hour[date_object.hour]+=1
        else:
            in_hour[date_object.hour] = 0
    print(in_hour)
    for key, value in in_hour.items():
        print(f'Hour {key} has {value} hits')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    url = args.url
    try:
        csv_data = downloadDATA(url)
        searchForImageHits(csv_data)
        findMostPopularBrowser(csv_data)
        totalHitsHour(csv_data)
    except Exception as e:
        sys.exit(f"Innappropriate Error Message {e}")

if __name__ == "__main__":
    main()


# In[ ]:




