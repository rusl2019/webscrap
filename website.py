import requests
from bs4 import BeautifulSoup

def searching_url():
    url = "https://www.detik.com/terpopuler"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    f = open("./index.html", 'w')
    for article in soup.find_all("article"):
        f.write(f"{article}")
    f.close()

    with open("./index.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    f = open("./index.html", 'w')
    for data in soup.find_all('a', href=True):
        f.write(f"{data['href']}\n")
    f.close()

def scrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('title')
    print(f"# {title.get_text()}\n")

    for data in soup.find_all("p"):
        data = data.get_text()
        print(f"{data}\n")


if __name__ == "__main__":

    # searching_url()
    file = open('input.in', 'r')
    lines = file.readlines()

    for url in lines:
        scrap(url.strip())
