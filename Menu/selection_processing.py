# -*- coding: cp1251 -*-
from InfoParser import VK
from InfoParser import FB
from InfoParser import INS
#
#����������� �� ������� ������
def selection_vk():
    print ("""
�������� ����� ������:
1)����� ������� � ����� �� ����� ���������
2)��������� ���������� � �������� �� id
""")
    selection = input (" > ")
    if (selection == '1'):
        VK.FamNameSearch()
    elif(selection == '2'):
        VK.ProfileInfo()

def selection_fb():
    print ("""
�������� ����� ������:
1)����� ������� � ����� �� ����� Facebook
2)��������� ���������� � �������� �� id
""")
    selection = input (" > ")
    if (selection == '1'):
        FB.FamNameSearch()
    if(selection =='2'):
        FB.get_profile()

def selection_inst():
    print ("""���������� �� �������� ���������""")
    INS.instagram_info()
#
#��������� ������ ������������
def selection_process(selection):
    if (selection == '1'):
        selection_vk()
#������ ��������, ��� �� �� ���
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
