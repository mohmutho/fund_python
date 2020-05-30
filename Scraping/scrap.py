import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sorted_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['vote'])
def create_custom_hn(links, subtext):
  hn = []
  for index, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[index].select('.score')
    if len(vote):
      point = int(vote[0].getText().replace(' points', ' '))
      if point > 99:
        hn.append({'title': title, 'href': href, 'vote': point})
  return sorted_stories_by_votes(hn)
pprint.pprint(create_custom_hn(links, subtext))