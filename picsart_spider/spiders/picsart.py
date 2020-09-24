import scrapy
from urllib.parse import quote
from picsart_spider.items import PicsartItem
from scrapy import Request, Spider
import os
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlretrieve
import re
import time
from furl import furl


class PicsartSpider(scrapy.Spider):
    name = 'picsart'
    allowed_domains = ['www.picsart.com']
    base_url = 'https://picsart.com/search/stickers?q='
    file_path = '/Users/wecut145/Python/picsart_spider/downloadPics/'
    downloading_path = ''
    keyword = ''

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            # 创建文件夹
            self.downloading_path = self.file_path + keyword
            # folder = os.path.exists(self.downloading_path)
            # if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
            #     os.makedirs(self.downloading_path)            #makedirs 创建文件时如果路径不存在会创建这个路径

            url = self.base_url + quote(keyword)
            yield Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print('Begin parse', response.url)
        url = furl(response.url)
        keyword = url.args['q']
        soup = BeautifulSoup(response.body, 'html.parser')
        imgwarps = soup.find_all("div", class_="img-wrapper pa-ratio-1-1")
        for item in imgwarps:
            image_url = item.img.get('src')
            if (image_url != ''):
                image_url = image_url.replace('?type=webp&to=min&r=240', '?type=png&to=min&r=640')
                # 下载文件
                #                 self.fileDownload(image_url, self.file_path+keyword)
                # 收集文件路径
                self.writeImgUrlToTxt(image_url, keyword)

    def writeImgUrlToTxt(self, image_url, keyword):
        imageUrlTxtPath = self.file_path + 'imageUrlTxt'
        folder = os.path.exists(imageUrlTxtPath)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(imageUrlTxtPath)
        my_open = open(imageUrlTxtPath + "/" + keyword + '.txt', 'a')
        # 若文件不存在,创建，若存在，追加
        my_open.write(image_url + '\n')
        my_open.close()

    def fileDownload(self, image_url, download_path):
        file_name = os.path.basename(image_url);
        file_name = re.sub('\?.*', '', file_name)
        file_path = download_path + '/' + file_name
        if os.path.isfile(file_path):
            print('文件存在：', file_path)
        else:
            print('正在下载：', file_path)
            urllib.request.urlretrieve(image_url, file_path)
