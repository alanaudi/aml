# Standard import
import itertools
import os
import pandas as pd
from pathlib import Path
import re

# Local import
from data import Sample, get_sample

# GLOBAL
ROOT = Path(os.getcwd())
DATASET_DIR = ROOT / 'dataset'
DOC_DIR = ROOT / 'doc'

# csv dataset
csvfile = DATASET_DIR / os.listdir(DATASET_DIR)[1]

# create simplified name, host name, hyperlink

host_name = set([sample.host for sample in get_sample(csvfile)])

for sample in get_sample(csvfile):
    if sample.host in host_name:
        print(F'{sample.source}\t{sample.host}\t{sample.hyperlink}')
        host_name.remove(sample.host)
