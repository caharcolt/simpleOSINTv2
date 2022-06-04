# -*- coding: cp1251 -*-
from Menu import selection_processing

print ("""
|========================================|
|   Программа для получение информации   |
|   из социальных сетей. -by caharcolt   |
|   *для реферата*                       |
|========================================|

Выберите направление поиска:
1)Вконтакте
2)FaceBook
3)Instagram - NEED VPN!
""")

#запуск обработки выбора пользователя
selection = input (" > ")
selection_processing.selection_process(selection)
