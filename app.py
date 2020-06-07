# Standard import
import itertools
import os
from pathlib import Path
import re

# Third-party import
import pandas as pd

# Local import
from data import Sample, get_sample
from crawler import NewsCrawler
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

# crawler {{{
for sample in itertools.islice(get_sample(csvfile), 1):
    config = {'selector': {
                  'title': '#content > div > div > div._2hZZ.theme-app.theme-newsdetail > main > div._uo1n > h1',
                  'meta': '#content > div > div > div._2hZZ.theme-app.theme-newsdetail > main > div._uo1n > div._1R6L',
                  'figure': '#content > div > div > div._2hZZ.theme-app.theme-newsdetail > main > div._1S0A > article > figure',
                  'content': '#content > div > div > div._2hZZ.theme-app.theme-newsdetail > main > div._1S0A > article > section._82F6 > div._1UuP',
                  },
              'source': sample.source,
              'hyperlink': sample.hyperlink}

    nc = NewsCrawler(**config)
    print(nc.article)
    # with open(F'{sample.news_ID}_{nc.source}.txt', 'w') as f:
    #     f.write(F'hyperlink: {nc.hyperlink}\n\n')
    #     f.write(nc.article)
# }}}
