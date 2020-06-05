# -*- coding: utf-8 -*-
from scrapy import Spider


__all__ = ['Cnyes', 'Udn', 'Mirrormedia', 'Chinatimes', 'DomesticJudicial']
           # 'Coolloud', 'Ctee', 'MopsTwse', 'Hk01', 'Wealth']
           # 'Ebc', 'Mingpao', 'Bnext', 'NewsLtn', 'FinanceTechnews',
           # 'Fsc', 'Tvbs', 'Cw', 'Businesstoday', 'Sina',
           # 'Ettoday', 'OnCc', 'Technews', 'MoneyUdn', 'Yahoo',
           # 'Setn', 'Managertoday', 'Cna', 'EstateLtn', 'MLtn',
           # 'CccTechnews', 'Hbrtaiwan', 'EcLtn', 'Nownews', 'OlMingpao',
           # 'Nextmag', 'EntLtn', 'Storm', 'HouseEttoday']


# 1
class Cnyes(Spider):
    name = 'cnyes'
    allowed_domains = ['news.cnyes.com']
    start_urls = []

    def parse(self, response):
        pass


#2
class Udn(Spider):
    name = 'udn'
    allowed_domains = ['udn.com']
    start_urls = []

    def parse(self, response):
        pass


# 3
class Mirrormedia(Spider):
    name = 'mirrormedia'
    allowed_domains = ['www.mirrormedia.mg']
    start_urls = []

    def parse(self, response):
        pass


# 4
class Chinatimes(Spider):
    name = 'chinatimes'
    allowed_domains = ['www.chinatimes.com']
    start_urls = []

    def parse(self, response):
        pass


# 5
class DomesticJudicial(Spider):
    name = 'domestic.judicial'
    allowed_domains = ['domestic.judicial.gov.tw']
    start_urls = []

    def parse(self, response):
        pass

# 6
class Coolloud(Spider):
    name = 'coolloud'
    allowed_domains = ['www.coolloud.org.tw']
    start_urls = []

    def parse(self, response):
        pass


# 7
class Ctee(Spider):
    name = 'ctee'
    allowed_domains = ['m.ctee.com.tw']
    start_urls = []

    def parse(self, response):
        pass


# 8
class MopsTwse(Spider):
    name = 'mops.twse'
    allowed_domains = ['mops.twse.com.tw']
    start_urls = []

    def parse(self, response):
        pass


# 9
class Hk01(Spider):
    name = 'hk01'
    allowed_domains = ['www.hk01.com']
    start_urls = []

    def parse(self, response):
        pass


# 10
class Wealth(Spider):
    name = 'wealth'
    allowed_domains = ['www.wealth.com.tw']
    start_urls = []

    def parse(self, response):
        pass


class NewsFactory():
    @staticmethod
    def get_news_crawler(template):
        try:
            if template in __all__:
                return eval(template)
            raise AssertionError(F'{template}() not found')
        except AssertionError as _e:
            print(_e)


if '__main__' == __name__:
    news_crawler = NewsFactory.get_news_crawler('Cnyes')
