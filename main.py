import requests
from bs4 import BeautifulSoup
url = "https://www.nasa.gov/news/all-news/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
news = soup.find_all("div", {"class": "hds-content-item"})
file = open('news.csv', 'a', encoding='utf-8')
def parser():
    for n in news:
        print(n.find("div", {"class": "hds-content-item-inner"}).get_text().strip())
        file.write(n.find("div", {"class": "hds-content-item-inner"}).get_text().strip())
        file.write('\n')
parser()
