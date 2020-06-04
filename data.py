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
        return re.search(r'https?://.*?/', self.hyperlink).group()

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
        return ast.literal_eval(s)


def get_sample(fname: str) -> Iterator[str]:
    """ Preprocess each row to Sample

    Args:
        filename (str): dataset/tbrain_train_final_0603.csv

    Yield:
        Sample
    """
    with open(fname, newline='') as f:
        for row in csv.DictReader(f):
            yield Sample(**row)


def get_chunk_sample(fname, chunksize=1000):
    """ Get a chunk of samples

    Args:
        fname (str): dataset/tbrain_train_final_0603.csv
        chunksize (int, optional): 1000

    Yield:
        Iterator

    Examples:
        >>> for i in get_chunk_sample(fname):
        ...     print(len(list(i)))
        1000
        1000
        1000
        1000
        1000
        23
    """

    it = iter(get_sample(fname))

    while True:
        chunk_it = itertools.islice(it, chunksize)
        try:
            n = next(chunk_it)
        except StopIteration:
            return
        yield from itertools.chain((n,), chunk_it)
