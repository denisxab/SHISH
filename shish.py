import os
import random
import json
import tkinter
import tkinter.scrolledtext
import pyperclip
from assistant import Assistant

a = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
    'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
    'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
    'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё',
    'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П',
    'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',
    'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',

    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    ' ', '&', '?', '@', '!', ':',  '', '.', ',', "'",
    '"', '(', ')', '-', '+', '=', '_', '–', '#', ';',
    '', '\n', '\t', '\\', '//', '/',

    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z',
]


class Shish:
    """docstring for Shish"""

    def __init__(self):
        super(Shish, self).__init__()

        self.character_list = a
        self.bit = 10
        self.rand = 5

        self.Windows = tkinter.Tk()
        self.Windows.geometry('666x380')

        self.bat1 = tkinter.Button(self.Windows,
                                   width=5,
                                   text='Создать ключ',
                                   command=self.Formation_кey,
                                   fg='#ffffff',
                                   bg='#4b5463')
        self.frame0 = tkinter.Frame(self.Windows)
        self.text0_1 = tkinter.Text(
            self.frame0,
            width=5,
            height=1,
            bg='#ffffff')
        self.text0_2 = tkinter.Text(
            self.frame0,
            width=5,
            height=1,
            bg='#ffffff')
        self.frame4 = tkinter.Frame(self.Windows)
        self.frame2_1 = tkinter.Frame(self.frame4)
        self.bat2 = tkinter.Button(self.frame2_1,
                                   width=5,
                                   height=5,
                                   text='Закодировать',
                                   command=self.Encryption,
                                   fg='#ffffff',
                                   bg='#4b5463')

        self.text1 = tkinter.scrolledtext.ScrolledText(
            self.frame2_1,
            width=10,
            height=11)
        self.frame1 = tkinter.Frame(self.frame2_1)
        self.bat2_1 = tkinter.Button(
            self.frame1,
            width=5,
            text='COPY',
            command=lambda: Assistant.copy0(self),
            bg='#fade55')
        self.bat2_2 = tkinter.Button(
            self.frame1,
            width=5,
            text='PAST',
            command=lambda: Assistant.paste0(self),
            bg='#c3f229')
        self.frame3_1 = tkinter.Frame(self.frame4)
        self.bat3 = tkinter.Button(self.frame3_1,
                                   width=5,
                                   height=5,
                                   text='Декодировать',
                                   command=self.Decryption,
                                   fg='#ffffff',
                                   bg='#4b5463')

        self.text2 = tkinter.scrolledtext.ScrolledText(
            self.frame3_1,
            width=10,
            height=11)
        self.frame2 = tkinter.Frame(self.frame3_1)
        self.bat3_1 = tkinter.Button(
            self.frame2,
            width=5,
            text='COPY',
            command=lambda: Assistant.copy1(self),
            bg='#fade55')
        self.bat3_2 = tkinter.Button(
            self.frame2,
            width=5,
            text='PAST',
            command=lambda: Assistant.paste1(self),
            bg='#c3f229')

        self.bat_clear = tkinter.Button(
            self.Windows,
            width=5,
            height=3,
            text='X_X',
            command=lambda: Assistant.clear(self),
            fg='#ffffff',
            bg='#4b5463')

        Assistant.pack(self)

        Assistant.chek_d(self)

        self.Windows.mainloop()

    def Formation_кey(self):
        l = {}
        v = []
        for x in self.character_list:
            l[x] = []
            for y in range(self.rand):
                deb = random.getrandbits(self.bit)
                if not deb in v:
                    v.append(deb)
                else:
                    deb = random.getrandbits(125)
                    v.append(deb)
                l[x].append(deb)

        with open('key.json', 'w', encoding='utf-8') as file_j:
            json.dump(l, file_j, sort_keys=False, ensure_ascii=False)

        Assistant.chek_d(self)

    def Encryption(self):

        slo = self.text1.get(1.0, 'end-1c')

        try:
            with open('key.json', 'r', encoding='utf-8') as json_j:

                red = json.load(json_j)
                v = [random.choice(red[x]) for x in slo if x in red]
                f = ''.join(['{}-'.format(x) for x in v])

            self.text2.delete(1.0, tkinter.END)
            self.text2.insert(tkinter.INSERT, f)

        except FileNotFoundError:
            self.text2.delete(1.0, tkinter.END)
            self.text2.insert(tkinter.INSERT, "NO FILE")
            self.text1.delete(1.0, tkinter.END)
            self.text1.insert(tkinter.INSERT, "NO FILE")

    def Decryption(self):

        g = self.text2.get(1.0, 'end-1c').split('-')[:-1]
        list_code = [int(x) for x in g]

        with open('key.json', 'r', encoding='utf-8') as json_j:
            red = json.load(json_j)
            v = {z: x[0]for x in red.items() for z in list_code if z in x[1]}
            zx = [v[x] for x in list_code if x in v]

        self.text1.delete(1.0, tkinter.END)
        self.text1.insert(tkinter.INSERT, str(''.join(zx)))


if __name__ == '__main__':
    Shish()
