# -*- coding: cp1251 -*-
import requests
import vk_api
from bs4 import BeautifulSoup
Token ="����� ������ ���� ��� ����� ���������!!!"

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
#���������� �������� ������ �� ���, � �� ���� � ��� ��������, �� ���� �� ���(
#�������� ��������, ������������ ����������� list �� ������ �������� ��� ������� ���� �������. � ��������� ������� �������� �� ����, �������� � �������
def ProfileInfo():
    profile = input ("Enter ID > ")
    vk_session = vk_api.VkApi(token=Token)
    vk_session = vk_session.get_api()
    info = vk_session.users.get(user_ids = profile, fields = {'is_closed', 'id','first_name','last_name','about','city','personal', 'nickname','career','activities','bdate','connections','country','domain','education','home_town','interests'})
    info = info[0] #fix
    first_name = info['first_name']
    last_name = info['last_name']
    is_closed = info['is_closed']

#��������� �� ������ ��� ���������
    try:
        bdate = info['bdate']
    except:
        bdate = "���� �������� �� ������"
    try:
        nickname = info ['nickname'] 
    except:
        nickname = "������� �� ������" 
    try:
        domain = info['domain']
    except:
        domain = "����� �� ������"
    try:
        connections = info['connections']
    except:
        connections = "�� ������� ������� �����"
    try:
        about = info ['about']
    except:
        about = "���������� � ���� �� �������"
    try:
        city = info ['city']
    except:
        city = "����� �� ������"
    try:
        country = info['country']
    except:
        country = "������ �� �������"
    try:
        home_town = info ['home_town']
    except:
        home_town = "�������� ����� �� ������"
    try:
        personal = info['personal']
    except:
        personal = "��������� ������� �� ��������"
    try:
        activities = info ['activities']
    except:
        activities = "������������ �� �������"
    try:
        interests = info ['interests']
    except:
        interests = "�������� �� �������"
    try:
        career = info ['career']
    except:
        career = "������� �� �������"
    try:
        education = info['education']
    except:
        education = "�������� �� �������"
    try:
        university_name = info['university_name']
    except:
        university_name = "����������� �� ������"
    
#����� �� ������ ���������� ������� ������� ��������
    print (f"""
    ������� �����? -> {is_closed}
    {first_name} {last_name} ({bdate})
    {nickname} ({id})

    ���������� ��� �����:
    -{connections}
    -{domain}

    � ����: {about}


    ������ ��������������:
    {city}
    {country}
    {home_town}


    �������� � ������������:
    -{personal}
    -{activities}
    -{interests}

    ������/�����:
    -{career}
    -{education} 
    -{university_name}
    """)



