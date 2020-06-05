# -*- coding: utf-8 -*-
from scrapy import Spider


class Cnyes(Spider):
    name = 'cnyes'
    allowed_domains = ['news.cnyes.com']
    start_urls = []

    def parse(self, response):
        pass


class Udn(Spider):
    name = 'udn'
    allowed_domains = ['udn.com']
    start_urls = []

    def parse(self, response):
        pass


class Mirrormedia(Spider):
    name = 'mirrormedia'
    allowed_domains = ['www.mirrormedia.mg']
    start_urls = []

    def parse(self, response):
        pass


class NewsFactory():
    @staticmethod
    def get_news_crawler(template):
        try:
            if template == 'Cnyes':
                return Cnyes()
            raise AssertionError(F'{template}() not found')
        except AssertionError as _e:
            print(_e)


if '__main__' == __name__:
    news_crawler = NewsFactory.get_news_crawler('Cnyes')
    news_crawler = NewsFactory.get_news_crawler('Ettoday')
