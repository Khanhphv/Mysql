import urllib.request
from bs4 import BeautifulSoup
import re
import csv

class GetListStory:
    def __init__(self, link):
        self.link = link
        page_content = urllib.request.urlopen(self.link)
        html = page_content.read()
        html_obj = BeautifulSoup(html, 'html.parser')
        html_page = html_obj.find('div', {"class": "pagination-container"}).find('ul', {'class': 'pagination-sm'})
        for i, link in enumerate(html_page.findAll(href=True)):
            if i == 6:
                self.numberpages = self.getPageNumber(link.get("title"))
        with open('listStory.csv', 'w',encoding="utf-8", newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(1, self.numberpages + 1):
                link = self.link + "/trang-" + str(i)
                self.getEachPage(link, filewriter)


    def getEachPage(self,link_page, filewriter):
        page_content = urllib.request.urlopen(link_page)
        html = page_content.read()
        html_obj = BeautifulSoup(html, 'html.parser')
        list_page = html_obj.find('div', {"id": "list-page"})
        list_story = list_page.find('div', {"class": "col-truyen-main"})
        list_link_story = list_story.findAll(href=True)
        for i, link in enumerate(list_link_story):
            if i % 2 == 0:
                page_content = urllib.request.urlopen(link.get('href'))
                html = page_content.read()
                html_obj = BeautifulSoup(html, 'html.parser')
                info = html_obj.find('div', {"class": "info"})
                for index, title in enumerate(info.findAll('div')):
                    if title.findAll(href=True):
                        if index == 0:
                            author = self.processString(title.find('a'))
                        if index == 1:
                            category = []
                            for c in title.findAll('a'):
                                category.append((self.processString(str(c))))

                category = ','.join(str(e) for e in category)
                name = html_obj.find('h3').text
                link = str(link.get('href'))


                print(link)
                print(name)
                print(category)
                print(author)


                filewriter.writerow(link)

    def processString(self, string):
        string = str(string)
        text = re.search('(\>.*?\<)', string)
        return text.group(0)[1: (len(text.group(0)) - 1)]

    def getPageNumber(self, text):
        text = re.search('\d+', text)
        return int(text.group(0))

khanh = GetListStory("https://truyenfull.vn/danh-sach/truyen-full/")
