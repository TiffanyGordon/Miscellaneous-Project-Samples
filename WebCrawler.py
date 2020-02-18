import bs4
import requests
import urllib2



home = requests.get('https://www.depaul.edu')


def crawl(link):
#    visited.append(link)

    DPUhome = urllib2.urlopen('https://www.depaul.edu')
    content = bs4.BeautifulSoup(DPUhome.read(), 'html.parser')
    linklist = content.findAll('a', href=True)

    print(linklist)

#    for link in linklist:
#        print(link)

crawl('https://www.depaul.edu')
