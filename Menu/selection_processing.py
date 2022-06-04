# -*- coding: cp1251 -*-
from InfoParser import VK
from InfoParser import FB
from InfoParser import INS
#
#Переводилки на функции поиска
def selection_vk():
    print ("""
Выберите метод поиска:
1)Поиск фамилии и имени по всему ВКонтакте
2)Получение ифнормации о странице по id
""")
    selection = input (" > ")
    if (selection == '1'):
        VK.FamNameSearch()
    elif(selection == '2'):
        VK.ProfileInfo()

def selection_fb():
    print ("""
Выберите метод поиска:
1)Поиск фамилии и имени по всему Facebook
2)Получение ифнормации о странице по id
""")
    selection = input (" > ")
    if (selection == '1'):
        FB.FamNameSearch()
    if(selection =='2'):
        FB.get_profile()

def selection_inst():
    print ("""Информация об аккаунте инстаграм""")
    INS.instagram_info()
#
#Обработка выбора пользователя
def selection_process(selection):
    if (selection == '1'):
        selection_vk()
#Должно работать, код же не мой
    if (selection == '2'):
        selection_fb()
    if (selection == '3'):
        import subprocess
        cmd = 'python3 INS.py'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate() 
        #result = out.split('\n')
        #for lin in result:
        #    if not lin.startswith('#'):
         #       print(lin)
