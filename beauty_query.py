#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import random
from pymongo import MongoClient, DESCENDING

mongo_client = MongoClient()
ptt_db = mongo_client.beauty_board_db
article_col = ptt_db.beauty_article_col

conditions = {}

def query(conditions=conditions):
    push_number = conditions['push_number']
    keyword = conditions['keyword']
    post_number = conditions['post_number']

    if keyword:
        nodes = list(article_col.find({'title': {'$regex': keyword}})
                     .sort('date', DESCENDING).limit(post_number))
        for node in nodes:
            i = random.randint(0, len(node['pic'])-1)
            node['pic'] = node['pic'][i]
        return nodes

    if push_number:
        result = article_col.find({'push': {'$gte': push_number}}).\
            sort('date', DESCENDING)
    else:
        result = article_col.find().sort('date', DESCENDING)

    if post_number:
        result = result.limit(post_number)

    nodes = list(result)
    for node in nodes:
        i = random.randint(0, len(node['pic'])-1)
        node['pic'] = node['pic'][i]
    return nodes


def set_condition(push_number=None, keyword=None, post_number=30):
    conditions['push_number'] = push_number
    conditions['keyword'] = keyword  # unicode problem u'xxxx'
    conditions['post_number'] = post_number


def gen_html(nodes):
    url = 'http://www.ptt.cc/bbs/Beauty/'
    print('<!DOCTYPE HTML>')
    print('<head><meta charset="UTF-8"></head>')
    print('<body>')
    for node in nodes:
        print('<a href="{}{url}.html" target="_blank">原始文章</a>'.format(url, **node))
        print('<br>')
        print('<img src="{pic}" alt="" height="" width="">'.format(**node))
        print('<br>')
        print('<br>')
    print('</body>')


if __name__ == '__main__':
    set_condition()
    nodes = query()
    gen_html(nodes)
