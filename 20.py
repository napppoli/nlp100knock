#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import gzip
import json

def get_wiki_content(title):
    with gzip.open('jawiki-country.json.gz') as f:
        for line in f:
            data=json.loads(line)
            if(data['title']==title):
                return data['text']
            
        return ""
        
print(get_wiki_content('イギリス'))
