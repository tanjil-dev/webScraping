import requests
import bs4

class WebScrapingService:
    res = requests.get('https://www.worldometers.info/coronavirus/country/bangladesh/')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    def getTallykhata():
        res = requests.get('https://www.worldometers.info/coronavirus/country/bangladesh/')
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        l = []
        content = soup.select('#newsdate2020-05-09 strong')
        for i in content:
            l.append(i.text)
        return l
    def getDate():
        l = []
        res = requests.get('https://www.worldometers.info/coronavirus/country/bangladesh/')
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        date = soup.select('.news_date h4')
        for i in date:
            l.append(i.text)
        return l