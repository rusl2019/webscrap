# webscrap

Simple script for scraping website content using python3

## Prerequisites

* [requests](https://github.com/psf/requests)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup)

```bash
python3 -m pip install --upgrade requests beautifulsoup4
```

## Usage

change variable `url` in input file with link or url website to be scrap

```text
https://example.com/page/title
https://example.com/page/title/2
```

then run 

```bash
python3 website.py > news.md
```
