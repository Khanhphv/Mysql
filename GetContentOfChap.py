# !/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

class GetConentOfChap:
    def __init__(self, link):
        self.link = link
        self.storycontent = ''

    def get_content(self):
        # self.link = urllib.request.urlopen('https://truyenfull.vn/choc-tuc-vo-yeu-mua-mot-tang-mot-241019/chuong-1/')
        response = urllib.request.urlopen(self.link)
        # response = self.link

        html = response.read()
        content = BeautifulSoup(html, 'html.parser')
        self.name = content.find('a', {'class': "chapter-title"}).text

        # noi dung cua the chapter-c
        list_story = content.find('div', {"id": "chapter-c"})
        arr = str(list_story).split()
        # r = requests.post('http://127.0.0.1/back_firstson1/public/api/updatechapter',
        #                   data={'name': self.name, 'chapter_content': self.storycontent, 'story_id': self.story_id, 'chapter_id': self.chap_id})
        # print "###################### " + r.text
        return list_story.text

    def processString(self, string):
        # print string.find("Chuong")
        start = len("Chuong")
        end = string.find(':')
        return string[start: end]


khanh = GetConentOfChap('https://truyenfull.vn/choc-tuc-vo-yeu-mua-mot-tang-mot-241019/chuong-1/').get_content()
print(khanh)