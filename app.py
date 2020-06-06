# Standard import
import itertools
import os
from pathlib import Path
import re

# Third-party import
import pandas as pd
from scrapy import Spider
from scrapy.crawler import CrawlerProcess

# Local import
from data import Sample, get_sample
from crawler.crawler.spiders.source import NewsFactory
from crawler.crawler.spiders.cnyes import Cnyes

# GLOBAL
ROOT = Path(os.getcwd())
DATASET_DIR = ROOT / 'dataset'
DOC_DIR = ROOT / 'doc'

# csv dataset
csvfile = DATASET_DIR / os.listdir(DATASET_DIR)[1]

# create simplified name, host name, hyperlink

host_name = set([sample.host for sample in get_sample(csvfile)])

# demo sample {{{
# print(F'Class Name\thostname\texample')
# for sample in itertools.islice(get_sample(csvfile), 3):
#     if sample.host in host_name:
#         print(F'{sample.source}\t{sample.host}\t{sample.hyperlink}')
#         host_name.remove(sample.host)
# }}}


config = {
    'allowed_domains': ['apple.com'],
    'xpath': '//*[@id="content"]/div/div/div[2]/main',
    'start_urls': ['https://news.cnyes.com/news/id/4352432']}

NewsCrawler = NewsFactory('Cnyes', config)

process = CrawlerProcess()

process.crawl(NewsCrawler)
process.start()

