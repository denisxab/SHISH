import os
import random
import json
import tkinter
import tkinter.scrolledtext
import pyperclip


class Assistant:
    """docstring for Assistan"""

    def chek_d(self):
        if not 'key.json' in os.listdir():
            self.frame4.pack_forget()
            self.bat_clear.pack_forget()
            self.Windows.geometry('666x380')
            self.bat1['height'] = 10
            self.text0_1['height'] = 5
            self.text0_2['height'] = 5

        elif 'key.json' in os.listdir():
            self.bat1.pack_forget()
            self.frame0.pack_forget()
            self.text0_1.pack_forget()
            self.text0_2.pack_forget()
            self.frame4.pack(fill=tkinter.BOTH, expand=True)
            self.bat_clear.pack(fill=tkinter.BOTH)

    def pack(self):

        self.bat1.pack(fill=tkinter.BOTH)
        self.frame0.pack(fill=tkinter.BOTH)
        self.text0_1.pack(side='left',
                          fill=tkinter.BOTH,
                          expand=True,
                          padx=5,
                          pady=5)

        self.text0_2.pack(side='left', fill=tkinter.BOTH,
                          expand=True,
                          padx=5,
                          pady=5)

        self.frame4.pack(fill=tkinter.BOTH, expand=True)
        self.frame2_1.pack(side='left', fill=tkinter.BOTH, expand=True)
        self.bat2.pack(fill=tkinter.BOTH)
        self.text1.pack(fill=tkinter.BOTH, expand=True)
        self.frame1.pack(fill=tkinter.BOTH)
        self.bat2_1.pack(side='left', fill=tkinter.BOTH, expand=True,)
        self.bat2_2.pack(side='left', fill=tkinter.BOTH, expand=True,)
        self.frame3_1.pack(side='left', fill=tkinter.BOTH, expand=True)
        self.bat3.pack(fill=tkinter.BOTH)
        self.text2.pack(fill=tkinter.BOTH, expand=True)
        self.frame2.pack(fill=tkinter.BOTH)
        self.bat3_1.pack(side='left', fill=tkinter.BOTH, expand=True,)
        self.bat3_2.pack(side='left', fill=tkinter.BOTH, expand=True,)
        self.bat_clear.pack(fill=tkinter.BOTH)

    def pack_forget(self):
        self.bat1.pack_forget()
        self.frame0.pack_forget()
        self.text0_1.pack_forget()
        self.text0_2.pack_forget()
        self.frame4.pack_forget()
        self.frame2_1.pack_forget()
        self.bat2.pack_forget()
        self.text1.pack_forget()
        self.frame1.pack_forget()
        self.bat2_1.pack_forget()
        self.bat2_2.pack_forget()
        self.frame3_1.pack_forget()
        self.bat3.pack_forget()
        self.text2.pack_forget()
        self.frame2.pack_forget()
        self.bat3_1.pack_forget()
        self.bat3_2.pack_forget()
        self.bat_clear.pack_forget()

    def paste0(self):
        self.text1.insert(tkinter.INSERT, str(pyperclip.paste()))

    def copy0(self):
        pyperclip.copy(self.text1.get(1.0, 'end-1c'))

    def paste1(self):
        self.text2.insert(tkinter.INSERT, str(pyperclip.paste()))

    def copy1(self):
        pyperclip.copy(self.text2.get(1.0, 'end-1c'))

    def clear(self):
        self.text1.delete(1.0, tkinter.END)
        self.text2.delete(1.0, tkinter.END)
