import requests
from bs4 import BeautifulSoup


def scrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('title')
    print(f"# {title.get_text()}\n")

    for data in soup.find_all("p"):
        data = data.get_text()
        print(f"{data}\n")


if __name__ == "__main__":

    file = open('input.in', 'r')
    lines = file.readlines()

    for url in lines:
        scrap(url.strip())