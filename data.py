#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Standard import {{{
import ast
import csv
import itertools
import re
from typing import Iterator, List, Optional

# Third-party import
from pydantic import BaseModel, validator

# }}}

REPLACEMENT = ['www', 'com', 'tw', 'mg', 'gov', 'net', 'org', 'm', 'hk', 'news']
PATTERN = re.compile('|'.join([r'\b%s\b' % s for s in REPLACEMENT]))
REP = {k:'' for k in REPLACEMENT}


class Sample(BaseModel):
    """ Sample model

    Each sample:
        "01", "http://xxx.xxx", "xxx", "['foo', 'bar']"
    """

    news_ID: int
    hyperlink: str
    content: str
    name: Optional[List[str]]

    @property
    def source(self):
        return PATTERN.sub(lambda m: REP[re.escape(m.group(0))], self.host).strip('.')

    @property
    def host(self):
        host = re.search(r'https?://.*?/', self.hyperlink).group()
        host = re.findall(r'.*\/(.*)\/', host)[0]
        return host

    @validator('news_ID')
    def str2int(cls, s):
        return int(s)

    @validator('name', pre=True)
    def str2list(cls, s):
        """ Convert string representation of list to list of string

        Args:
            s (str): "['foo', 'bar']"

        Return:
            List[str]: ['foo', 'bar']
        """
        if not isinstance(s, str):
            raise ValueError('Name list format should be: \'["a", "b", ...]\'')
        return ast.literal_eval(s)


def get_sample(fname: str) -> Sample:
    """ Preprocess each row to Sample

    Args:
        filename (str): dataset/tbrain_train_final_0603.csv

    Yield:
        data.Sample
    """
    with open(fname, newline='') as f:
        for row in csv.DictReader(f):
            yield Sample(**row)


def get_chunk_sample(fname, chunksize=1000) -> Sample:
    """ Get a chunk of samples

    Args:
        fname (str): dataset/tbrain_train_final_0603.csv
        chunksize (int, optional): 1000

    Yield:
        data.Sample

    Examples:
        >>> for sample in itertools.islice(get_chunk_sample(fname), 3):
        ...     print(type(sample))
        <class 'data.Sample'>
        <class 'data.Sample'>
        <class 'data.Sample'>
    """

    it = iter(get_sample(fname))

    while True:
        chunk_it = itertools.islice(it, chunksize)
        try:
            n = next(chunk_it)
        except StopIteration:
            return
        yield from itertools.chain((n,), chunk_it)
