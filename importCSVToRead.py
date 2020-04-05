import csv
from GetListChapter import GetListChapter
import logging
import os
import urllib.request
from bs4 import BeautifulSoup

class ImportCSVToRead:

    def __init__(self, file):
        self.file = file
        self.begin = 0
        self.numberInEach = 12878
        self.end = 12878

        # self.end = (self.begin + 1) * self.numberInEach

    def readCSV(self):
        logging.basicConfig(filename='myapp.log', level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(name)s %(message)s')
        logger = logging.getLogger(__name__)
        with open('list_page.csv', 'w', encoding ="utf-8",  newline='') as page_file:
            filewriter = csv.writer(page_file, delimiter='|', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            with open(self.file,  encoding="utf8") as csvfile:
                content = csv.reader(csvfile)
                i = self.begin
                content = list(content)
                for i in range(self.begin, len(content)):
                    try:
                        print(i)
                        row = content[i][0].split('|')
                        link = str(row[0]).replace(" ", "")
                        print("Link " +link)
                        khan = GetListChapter(link).getListPages()
                        print(type(khan))
                        filewriter.writerow(khan)
                        print('=================================================')

                    except:
                        logger.error("Err:::" + str(i))

khanh = ImportCSVToRead('listStory3.csv').readCSV()
