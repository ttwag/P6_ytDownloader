#!/bin/zsh

cd /Users/taowang/Desktop/Project/P6_ytDownloader

source ./bin/activate
python3 ytDownloader.py $1 $2
deactivate
