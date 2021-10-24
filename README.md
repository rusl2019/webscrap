# webscrap

Simple script for scraping website content using python3

## Prerequisites

* [requests](https://github.com/psf/requests)
```bash
python3 -m pip install --upgrade requests
```

* [https://www.crummy.com/software/BeautifulSoup](BeautifulSoup)
```bash
python3 -m pip install --upgrade beautifulsoup4 
```

## Usage

change variable `url` in python file with link or url website to be scrap

```python
url = [
    'https://example.com/news/title',
    'https://example.com/news/title/2'
]
```

then run 

```bash
python3 website.py > text.txt
```
