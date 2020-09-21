# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from picsart_spider.configs import *
from scrapy.http import HtmlResponse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class ChromeDownloaderMiddleware(object):

    def __init__(self,timeout=30, service_args=[]):
        options = webdriver.ChromeOptions()
        self.timeout = timeout
#         options.add_argument('--headless')  # 设置无界面
        if CHROME_PATH:
            options.binary_location = CHROME_PATH
        if CHROME_DRIVER_PATH:
            self.driver = webdriver.Chrome(chrome_options=options, executable_path=CHROME_DRIVER_PATH)  # 初始化Chrome驱动
        else:
            self.driver = webdriver.Chrome(chrome_options=options)  # 初始化Chrome驱动

        self.wait = WebDriverWait(self.driver, self.timeout)


    def __del__(self):
        self.driver.close()

    def process_request(self, request, spider):
        try:
            print('Chrome driver begin...')
            self.driver.get(request.url)  # 获取网页链接内容
            seeMoreDivSelector = '#pjax-container > div.search-result-container > div > div.load-more-btn-container > div'
            seeMoreDiv = self.driver.find_element_by_css_selector(seeMoreDivSelector)
            seeMoreDivDisplay = seeMoreDiv.is_displayed()
            while(seeMoreDivDisplay):
                sleep(5)
                seeMoreDivDisplay = seeMoreDiv.is_displayed()
                if(seeMoreDivDisplay):
                    submit = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#pjax-container > div.search-result-container > div > div.load-more-btn-container > div > a')))
                    submit.click()
                    print('seeMoreDivDisplay',seeMoreDivDisplay)

            return HtmlResponse(url=request.url, body=self.driver.page_source, request=request, encoding='utf-8',
                                status=200)  # 返回HTML数据
        except TimeoutException:
            return HtmlResponse(url=request.url, request=request, encoding='utf-8', status=500)
        finally:
            print('Chrome driver end...')
