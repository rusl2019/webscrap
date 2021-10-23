import requests
from bs4 import BeautifulSoup


def scrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for data in soup.find_all("p"):
        data = data.get_text()
        print(data)


if __name__ == "__main__":
    url = [
        'https://news.detik.com/berita/d-5779394/eks-kapolsek-parigi-terduga-perkosa-anak-tersangka-akan-ajukan-banding',
        'https://news.detik.com/berita/d-5779394/eks-kapolsek-parigi-terduga-perkosa-anak-tersangka-akan-ajukan-banding/2'
    ]

    # url = 'https://sport.detik.com/raket/d-5779421/anthony-ginting-dan-jonatan-christie-mundur-dari-french-open-2021'
    # scrap(url)

    for i in url:
        scrap(i)
