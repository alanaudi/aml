import csv
import os
import json
from typing import List, Optional
from pydantic import BaseModel, Field, validator
import ast

csvfile = os.listdir('./dataset')[1]


class Sample(BaseModel):
    """Sample model

    Each sample:
        "01", "http://xxx.xxx", "xxx", "['foo', 'bar']"
    """

    news_ID: int
    hyperlink: str
    content: str
    name: Optional[List[str]]

    @validator('news_ID')
    def str2int(cls, s):
        """String to integer

        Args:
            s: "255"

        Return:
            int: 255
        """
        return int(s)

    @validator('name', pre=True)
    def str2list(cls, s):
        """Convert string representation of list to list of string

        Args:
            s (str): intput string -> "['a', 'b', 'c']"
        Return:
            (List[str]): ['foo', 'bar']
        """
        return ast.literal_eval(s)


with open(F'dataset/{csvfile}', newline='') as f:
    data = []
    for row in csv.DictReader(f):
        data.append(Sample(**row))
    print(data)
    print(len(data))
