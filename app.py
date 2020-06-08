#!/usr/bin/env python3
# Standard import
import sys
import itertools
import glob
import os
from pathlib import Path
import re
import traceback
import yaml

# Third-party import
import pandas as pd
import click
from tabulate import tabulate
from easydict import EasyDict

# Local import
from data import Sample, get_sample
from crawler import NewsCrawler

# GLOBAL
ROOT = Path(os.getcwd())
DATASET_DIR = ROOT / 'dataset'
DOC_DIR = ROOT / 'doc'

# csv dataset
csvfile = DATASET_DIR / glob.glob(F'{str(DATASET_DIR)}/*.csv')[0]

# create simplified name, host name, hyperlink
host_name = set([sample.host for sample in get_sample(csvfile)])


def get_selector():
    with open('selector.yaml', 'r') as f:
        return yaml.load(f)

# patch = [1982,1983,1997, 2002, 2010, 2015, 2019, 2028, 2035, 2059, 2079, 2083, 2134, 2138, 2151, 2156, 2170]


# Global settings {{{
_global_options = [
    click.option('-s', '--source', 'source', default='Cnyes', help='Source name from 39 news source'),
]

def global_options(func):
    for option in reversed(_global_options):
        func = option(func)
    return func
# }}}

@click.group()
@global_options
def main(**kwargs):
    pass

@main.command()
@global_options
def crawl(**kwargs): # {{{
    # Print argument, parameter, option {{{
    print(tabulate(list(kwargs.items()), headers=['Name', 'Value'], tablefmt='orgtbl'))
    args = EasyDict(kwargs)
    # }}}

    for sample in get_sample(csvfile):
        if sample.source == 'Cnyes' and sample.news_ID == 231:
            config = {'selector': get_selector()[sample.source],
                      'source': sample.source,
                      'hyperlink': sample.hyperlink}
            fname = F'{DATASET_DIR}/{sample.news_ID}.txt'
            try:
                nc = NewsCrawler(**config)
                with open(fname, 'w') as f:
                    f.write(F'hyperlink: {nc.hyperlink}\n\n')
                    f.write(nc.article)
                    print(F'{fname}')
            except Exception as e:
                _type = e.__class__.__name__
                _detail = e.args[0]
                print(F'{sample.news_ID}')
                cl, exc, tb = sys.exc_info()
                last_call_stack = traceback.extract_tb(tb)[-1]
                _fname = last_call_stack[0]
                _line = last_call_stack[1]
                _func_name = last_call_stack[2]
                print(F'{_fname}: line {_line}, def {_func_name}() -> {_type}, {_detail}')
    # }}}


@main.command()
@global_options
def info(**kwargs): # {{{
    """Get data analysis (source.tsv)
    \f

    Output:
        doc/source.tsv
    """
    # Print argument, parameter, option {{{
    print(tabulate(list(kwargs.items()), headers=['Name', 'Value'], tablefmt='orgtbl'))
    args = EasyDict(kwargs)
    # }}}
    # create source infomation
    sort = []
    print(F'Amount\tClass Name\thostname\texample')
    for sample in get_sample(csvfile):
        if sample.host in host_name:
            # print(F'{sample.source}\t{sample.host}\t{sample.hyperlink}')
            nums = len(list(filter(lambda x: x.source == sample.source, get_sample(csvfile))))
            sort.append(F'{nums}\t{sample.source}\t{sample.host}\t{sample.hyperlink}')
            host_name.remove(sample.host)
    for e in sorted(sort, key=lambda x: x.split('\t')[1]):
        print(e)
    # }}}


if '__main__' == __name__:
    main()
