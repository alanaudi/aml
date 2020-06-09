#!/usr/bin/env bash
if [ -d "dataset/raw/$1" ]; then
  echo "Delete files in dataset/raw/$1/"
  rm dataset/raw/$1/*.txt 2> /dev/null 
  rm log/$1.log 2> /dev/null 
else
  echo "Create folder dataset/raw/$1/"
  mkdir -p "dataset/raw/$1"
  touch "dataset/raw/$1/.gitkeep"
fi
