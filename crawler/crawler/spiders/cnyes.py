from scrapy import Spider, Request

class Cnyes(Spider):
    name = 'Cnyes'
    allowed_domains = ['news.cnyes.com']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = 'https://news.cnyes.com/news/id/4352432'

    def start_requests(self):
        yield Request(self.url, callback=self.parse)

    def parse(self, response):
        """ Define general pattern """
        article = response.xpath('//*[@id="content"]/div/div/div[2]/main').extract_first()
        yield article

