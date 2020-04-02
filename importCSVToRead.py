import csv
from GetListChapter import GetListChapter
import os
import urllib.request
from bs4 import BeautifulSoup

class ImportCSVToRead:

    def __init__(self, file):
        self.file = file
        self.numberInEach = 10
        self.begin = self.numberInEach
        self.end = (self.begin + 1) * self.numberInEach

    def readCSV(self):
        with open(self.file) as csvfile:
            content = csv.reader(csvfile)
            i = self.begin
            content = list(content)
            for i in range(self.begin, self.end):
                row = content[i]
                row = str(row[0]).replace(" ", "")
                os.mkdir('tmp/'+ str(i) )
                print(row)

                response = urllib.request.urlopen(row)
                html = response.read()
                content = BeautifulSoup(html, 'html.parser')
                khan = GetListChapter(row)
                print('=================================================')
            # for row in content:
            #     if i <= self.end:
            #         row = str(row[0]).replace(" ", "")
            #         print(row)
            #         khan = GetListChapter(row)
            #         print('=================================================')
            #         i = i+1



khanh = ImportCSVToRead('listStory.csv').readCSV()
