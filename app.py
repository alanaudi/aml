# Standard import
import itertools
import os
from pathlib import Path
import re
import yaml

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
csvfile = DATASET_DIR / list(filter(lambda x: x.endswith('csv'), os.listdir(DATASET_DIR)))[0]

# create simplified name, host name, hyperlink

host_name = set([sample.host for sample in get_sample(csvfile)])

def get_selector():
    with open('selector.yaml', 'r') as f:
        return yaml.load(f)

# patch = [1982,1983,1997, 2002, 2010, 2015, 2019, 2028, 2035, 2059, 2079, 2083, 2134, 2138, 2151, 2156, 2170]

# demo sample {{{
# print(F'Class Name\thostname\texample')
# for sample in itertools.islice(get_sample(csvfile), 3):
#     if sample.host in host_name:
#         print(F'{sample.source}\t{sample.host}\t{sample.hyperlink}')
#         host_name.remove(sample.host)
# }}}

# crawler {{{

for sample in get_sample(csvfile):
    if sample.source == 'Cnyes' and sample.news_ID > 2268:
        config = {'selector': get_selector()[sample.source],
                  'source': sample.source,
                  'hyperlink': sample.hyperlink}
        fname = F'{DATASET_DIR}/raw/{sample.source}/{sample.news_ID}.txt'
        try:
            nc = NewsCrawler(**config)
            with open(fname, 'w') as f:
                f.write(F'hyperlink: {nc.hyperlink}\n\n')
                f.write(nc.article)
                print(F'{fname}')
        except:
            print(F'{sample.news_ID}')

# }}}
print(len(list(filter(lambda x: x.source == 'Cnyes', list(get_sample(csvfile))))))
