import requests
from bs4 import BeautifulSoup

def searching_url():
    url = "https://www.detik.com/terpopuler"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    s = ""
    for article in soup.find_all("article"):
        s += f"{article}"

    soup = BeautifulSoup(s, 'html.parser')

    data = []
    for url in soup.find_all('a', href=True):
        data.append(url['href'])

    f = open("./input.in", 'w')
    for i in range(0,len(data),2):
        f.write(f"{data[i]}\n")
    f.close()

def scrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('title')

    f.write(f"# {title.get_text()}\n\n")
    for data in soup.find_all("p"):
        data = data.get_text()
        f.write(f"{data}\n\n")


if __name__ == "__main__":

    searching_url()
    file = open('input.in', 'r')
    lines = file.readlines()

    f = open("./news.md", 'w')
    for url in lines:
        scrap(url.strip())
    f.close()
