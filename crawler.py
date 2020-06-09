# -*- coding: utf-8 -*-
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup as BS


__all__ = ['Cnyes', 'Udn', 'Mirrormedia', 'Chinatimes', 'DomesticJudicial']
           # 'Coolloud', 'Ctee', 'MopsTwse', 'Hk01', 'Wealth']
           # 'Ebc', 'Mingpao', 'Bnext', 'NewsLtn', 'FinanceTechnews',
           # 'Fsc', 'Tvbs', 'Cw', 'Businesstoday', 'Sina',
           # 'Ettoday', 'OnCc', 'Technews', 'MoneyUdn', 'Yahoo',
           # 'Setn', 'Managertoday', 'Cna', 'EstateLtn', 'MLtn',
           # 'CccTechnews', 'Hbrtaiwan', 'EcLtn', 'Nownews', 'OlMingpao',
           # 'Nextmag', 'EntLtn', 'Storm', 'HouseEttoday']


class NewsCrawler(BaseModel):
    source: str
    hyperlink: str
    selector: dict

    @property
    def article(self):
        res = requests.get(self.hyperlink)
        root = BS(res.text, 'html.parser')
        with open('test.html', 'w') as f:
            f.write(res.text)
        title = root.select(self.selector['title'])[0].text
        meta = root.select(self.selector['meta'])[0].text
        figure = ''.join([x.text for x in root.select(self.selector['figure'])])
        content = ''.join([x.text for x in root.select(self.selector['content'])])
        return F'{title}\n\n{meta}\n\n{figure}\n\n{content}'


if '__main__' == __name__:
    pass
