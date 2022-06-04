# -*- coding: cp1251 -*-
import requests
import vk_api
from bs4 import BeautifulSoup
Token ="ЗДЕСЬ ДОЛЖЕН БЫТЬ ВАШ ТОКЕН ВКОНТАКТЕ!!!"

def FamNameSearch():
    FamName = input ("Enter FamName > ")
    _FamName = FamName.split()
    Family = _FamName[0]
    Name = _FamName[1]
    URL = "https://www.google.com/search?q=inurl%3Avk.com"
    URL = URL+"+"+ Family+"+"+Name 
    URL_get = requests.get(URL)
    URL_get = BeautifulSoup(URL_get.text, "html.parser")
    URL_get = URL_get.find_all('a',href=True)

    for links in URL_get:
        if links['href'].find("https://vk.com/")!= -1:
            links = links['href'].replace('/url?q=','')
            result = links[:links.index("&")]
            print (result)

#
#Информация парсится иногда не вся, я не знаю в чем проблема, по идее во мне(
#Говнокод лютейший, возвращается оказывается list из одного элемента что сделало кучу проблем. В отдельную функцию выносить не буду, работает и спасибо
def ProfileInfo():
    profile = input ("Enter ID > ")
    vk_session = vk_api.VkApi(token=Token)
    vk_session = vk_session.get_api()
    info = vk_session.users.get(user_ids = profile, fields = {'is_closed', 'id','first_name','last_name','about','city','personal', 'nickname','career','activities','bdate','connections','country','domain','education','home_town','interests'})
    info = info[0] #fix
    first_name = info['first_name']
    last_name = info['last_name']
    is_closed = info['is_closed']

#Обработка на уровне как говорится
    try:
        bdate = info['bdate']
    except:
        bdate = "День рождения не указан"
    try:
        nickname = info ['nickname'] 
    except:
        nickname = "Никнейм не указан" 
    try:
        domain = info['domain']
    except:
        domain = "Домен не указан"
    try:
        connections = info['connections']
    except:
        connections = "Не указаны способы связи"
    try:
        about = info ['about']
    except:
        about = "Информация о себе не указана"
    try:
        city = info ['city']
    except:
        city = "Город не указан"
    try:
        country = info['country']
    except:
        country = "Страна не указана"
    try:
        home_town = info ['home_town']
    except:
        home_town = "Домашний адрес не указан"
    try:
        personal = info['personal']
    except:
        personal = "Жизненная позиция не указаана"
    try:
        activities = info ['activities']
    except:
        activities = "Деательность не указана"
    try:
        interests = info ['interests']
    except:
        interests = "Интересы не указаны"
    try:
        career = info ['career']
    except:
        career = "Карьера не указана"
    try:
        education = info['education']
    except:
        education = "Обучение не указано"
    try:
        university_name = info['university_name']
    except:
        university_name = "Университет не указан"
    
#Вывод на печать информации которую удалось получить
    print (f"""
    Профиль скрыт? -> {is_closed}
    {first_name} {last_name} ({bdate})
    {nickname} ({id})

    Информация для связи:
    -{connections}
    -{domain}

    О себе: {about}


    Данные местоположения:
    {city}
    {country}
    {home_town}


    Интересы и деятельность:
    -{personal}
    -{activities}
    -{interests}

    Работа/Учеба:
    -{career}
    -{education} 
    -{university_name}
    """)



