# -*- coding: cp1251 -*-
import requests
from facebook_scraper import get_profile
from bs4 import BeautifulSoup

def FamNameSearch():
    FamName = input ("Enter FamName > ")
    _FamName = FamName.split()  
    Family = _FamName[0]
    Name = _FamName[1]

    URL = "https://www.google.com/search?q=inurl%3Afacebook.com"
    URL = URL+"+"+ Family+"+"+Name 

    URL_get = requests.get(URL)
    URL_get = BeautifulSoup(URL_get.text, "html.parser")
    URL_get = URL_get.find_all('a',href=True)

    for links in URL_get:
        if ((links['href'].find("https://www.facebook.com/")!= -1) or (links['href'].find("https://m.facebook.com/")!= -1) or (links['href'].find("https://ru.facebook.com/")!= -1)):
            links = links['href'].replace('/url?q=','')
            result = links[:links.index("&")]
            print (result)


#Работает от силы один раз, у facebook сильная защита от парсинга
def ProfileInfo():
   
   profile = input ("Enter ID > ")
   print (get_profile(profile))
