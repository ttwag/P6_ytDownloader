#!/bin/zsh

cd $HOME/P6_ytDownloader

source ./bin/activate
python3 ytDownloader.py $1 $2
deactivate
