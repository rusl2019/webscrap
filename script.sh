#!/usr/bin/env bash

python3 main.py
pandoc -o news.epub title.txt news.md

