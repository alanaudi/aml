#!/usr/bin/env bash
./clear.sh $1
python3 -W ignore app.py crawl -s $1 -l $2
cat log/$1.log
