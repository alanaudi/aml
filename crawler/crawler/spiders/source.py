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



# Dynamic class definition
class NewsSpider(Spider):
    def __init__(self, classtype):
        self._type = classtype
        self.name = classtype
        self.allowed_domains = []
        self.start_urls = []

    def parse(self, response):
        pass


def NewsFactory(name, argnames, BaseClass=NewsSpider):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            # here, the argnames variable is the one passed to the
            # ClassFactory call
            if key not in argnames:
                raise TypeError("Argument %s not valid for %s"
                    % (key, self.__class__.__name__))
            setattr(self, key, value)
        BaseClass.__init__(self, name)
    newclass = type(name, (BaseClass,),{"__init__": __init__})
    return newclass

if '__main__' == __name__:
    # ----------------------------------------
    c1 = NewsFactory.get_news_crawler('Cnyes')
    print(type(c1))
    # <class 'type'>
    print(type(c1()))
    # <class '__main__.Cnyes'>
    print(c1.name)
    # cnyes
    # ----------------------------------------
    c2 = interface('Cnyes')
    print(type(c2))
    # <class '__main__.Cnyes'>
    print(c2.name)
    # cnyes
    # ----------------------------------------
    # dynamic class definition
    c3 = ClassFactory('Nextmag', [])
    print(type(c3))
    instance = c3()
    print(instance)
    print(type(instance))
    print(instance.allowed_domains)
    print(instance.name)
