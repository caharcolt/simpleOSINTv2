# -*- coding: cp1251 -*-
from Menu import selection_processing

print ("""
|========================================|
|   ��������� ��� ��������� ����������   |
|   �� ���������� �����. -by caharcolt   |
|   *��� ��������*                       |
|========================================|

�������� ����������� ������:
1)���������
2)FaceBook
3)Instagram - NEED VPN!
""")

#������ ��������� ������ ������������
selection = input (" > ")
selection_processing.selection_process(selection)
