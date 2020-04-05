import urllib.request
from bs4 import BeautifulSoup
import re

class GetListChapter:
    def __init__(self, link):
        self.link = link
        self.page = ''
        # self.getListPages()


    def getListPages(self):
        listpage_arr = []
        self.content = urllib.request.urlopen(self.link).read()
        content = BeautifulSoup(self.content, 'html.parser')
        list_page = content.find('ul', {"class": "pagination-sm"})
        if list_page:
            list_page = list_page.findAll(title=True)
            for i in list_page:
                i = str(i)
                if i.__contains__('Cuối'):
                    self.page = self.get_page(i)
            if self.page == '':
                self.page = self.getPageNumber(list_page[len(list_page) - 2].get('href'))
        else:
            self.page = 0
        print("PAGE " + str(self.page))
        for i in range(1, int(self.page) + 1):
            tmp = "page-"
            if i == 1:
                tmp = ''
            else:
                tmp += str(i)
            link_page = self.link + tmp
            print('####### ' +link_page)
            listpage_arr.append(link_page)
        if len(listpage_arr) == 0:
            listpage_arr.append(self.link)
        return listpage_arr;

    def get_page(self, title):
        print(title)
        x = title.find("Trang")
        print(x)
        y = title.find("\">")
        print(y)
        return int(title[x + len("Trang"): y])

    def getPageNumber(self, text):
        text = re.search('\d+', text)
        return int(text.group(0))
