# -*- coding: utf-8 -*-
from scrapy import Spider, Selector


__all__ = ['Cnyes', 'Udn', 'Mirrormedia', 'Chinatimes', 'DomesticJudicial']
           # 'Coolloud', 'Ctee', 'MopsTwse', 'Hk01', 'Wealth']
           # 'Ebc', 'Mingpao', 'Bnext', 'NewsLtn', 'FinanceTechnews',
           # 'Fsc', 'Tvbs', 'Cw', 'Businesstoday', 'Sina',
           # 'Ettoday', 'OnCc', 'Technews', 'MoneyUdn', 'Yahoo',
           # 'Setn', 'Managertoday', 'Cna', 'EstateLtn', 'MLtn',
           # 'CccTechnews', 'Hbrtaiwan', 'EcLtn', 'Nownews', 'OlMingpao',
           # 'Nextmag', 'EntLtn', 'Storm', 'HouseEttoday']


# Dynamic class definition
class NewsSpider(Spider):
    def __init__(self, name, **kwargs):
        self._type = name
        print('set type')
        self.name = name
        print('set name')
        # self.allowed_domains = []
        # self.start_urls = []
        print(kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def parse(self, response):
        """ Define general pattern """
        selector = Selector(text=response.text)
        article = selector.xpath().extract_first()
        yield article



def NewsFactory(name, kwargs, BaseClass=NewsSpider):
    def __init__(self):
        BaseClass.__init__(self, name, **kwargs)
    return type(name, (BaseClass,),{"__init__": __init__})


if '__main__' == __name__:
    crawler = NewsFactory('Nextmag', [])()
    print(type(c3))
    instance = c3()
    print(instance)
    print(type(instance))
    print(instance.allowed_domains)
    print(instance.name)
