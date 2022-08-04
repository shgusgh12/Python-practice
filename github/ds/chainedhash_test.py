from enum import Enum
from tkinter import Menu
from chainedhash import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프','종료' ])

def selectMenu() -> Menu:
    s = [f' ({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(':  '))
        if 1 <=  n <= len(Menu):
            return Menu(n)

hash= ChainedHash(13)