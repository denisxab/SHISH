import os
import random
import json
import tkinter 
import tkinter.scrolledtext
import pyperclip





def shi(bit=125,rand=5):

	try :
		bit = int(text0_1.get(1.0, 'end-1c'))
		rand = int(text0_2.get(1.0, 'end-1c'))
	except ValueError:
		bit = 125
		rand  = 5

	a = ['а','б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
	 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
	  'ф', 'х', 'ц', 'ч', 'ш', 'щ','ъ', 'ы', 'ь',
	  'э', 'ю', 'я','А', 'Б', 'В', 'Г','Д', 'Е',
	  'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 
	  'Н', 'О', 'П', 'Р', 'С', 'Т' ,'У', 'Ф', 'Х', 'Ц',
	  'Ч', 'Ш', 'Щ', 'Ъ', 'Ы','Ь', 'Э', 'Ю', 'Я',
	  ' ','1','2','3','4','5','6','7','8','9','0',
	  '&','?','\\','@','!','a','b','c','d','e','f',
	  'g','h','i','j','k','l','m','n','o','p','q','r',
	  's','t','u','v','w','x','y','z','A','B','C','D',
	  'E','F','G','H','I','J','K','L','M','N','O','P','Q',
	  'R','S','T','U','V','W','X','Y','Z',
	  ]

	l = {}

	for x in a:
		l[x]=[]
		for y in range(rand):
			l[x].append(random.getrandbits(bit))

	with open('key.json','w',encoding='utf-8') as file_j:
		json.dump(l,file_j,sort_keys=False,ensure_ascii=False)

	return l

def code():
	slo = text1.get(1.0, 'end-1c')
	with open('key.json','r',encoding='utf-8') as json_j:
		red = json.load(json_j)
		v = []
		for x in slo:
			if x in red:
				v.append(random.choice(red[x]))



	text2.delete(1.0, tkinter.END)
	text2.insert(tkinter.INSERT,str(v))
	return v

def incode():
	try:
		list_code = eval( text2.get(1.0, 'end-1c'))
	except SyntaxError:
		return


	with open('key.json','r',encoding='utf-8') as json_j:
		red = json.load(json_j)
		v = {}
		for x in red.items():
			for z in list_code:
				if z in x[1]:
					v[z]=x[0]

	zx = []
	for x in  list_code:
		if x in v:
			zx.append(v[x])

	text1.delete(1.0, tkinter.END)
	text1.insert(tkinter.INSERT,str(''.join(zx)))
	return zx

def paste0():
	text1.insert(tkinter.INSERT,str(pyperclip.paste()))

def copy0():
	pyperclip.copy(text1.get(1.0, 'end-1c'))


def paste1():
	text2.insert(tkinter.INSERT,str(pyperclip.paste()))

def copy1():
	pyperclip.copy(text2.get(1.0, 'end-1c'))



root1=tkinter.Tk()
root1.geometry('384x666')



bat1 = tkinter.Button(root1, width=10,text='Создать ключ',  command = shi,bg='#fffef0')
frame0 = tkinter.Frame(root1)
text0_1 = tkinter.Text(frame0,width=5, height=1,bg='#ffffff')
text0_2 = tkinter.Text(frame0,width=5, height=1,bg='#ffffff')

bat2 = tkinter.Button(root1, width=20,text='Закодирывать',command = code,bg='#fffef0')
text1 = tkinter.scrolledtext.ScrolledText(root1,width=35, height=1)

frame1 = tkinter.Frame(root1)
bat2_1 = tkinter.Button(frame1, width=20,text='COPY',command = copy0,bg='#fade55')
bat2_2 = tkinter.Button(frame1, width=20,text='PAST',command = paste0,bg='#c3f229')


bat3 = tkinter.Button(root1, width=20,text='Декодиорывать',command = incode,bg='#fffef0')
text2 = tkinter.scrolledtext.ScrolledText(root1,width=35, height=1)

frame2 = tkinter.Frame(root1)
bat3_1 = tkinter.Button(frame2, width=20,text='COPY',command = copy1,bg='#fade55')
bat3_2 = tkinter.Button(frame2, width=20,text='PAST',command = paste1,bg='#c3f229')

#_________________________________________________________________#
bat1.pack(fill=tkinter.BOTH)
frame0.pack(fill=tkinter.BOTH)
text0_1.pack(side='left',fill=tkinter.BOTH,expand=True,padx=5, pady=5)
text0_2.pack(side='left',fill=tkinter.BOTH,expand=True,padx=5, pady=5)


bat2.pack(fill=tkinter.BOTH,expand=True)
frame1.pack(fill=tkinter.BOTH)
bat2_1.pack(side='left',fill=tkinter.BOTH,expand=True,padx=5, pady=5)
bat2_2.pack(side='left',fill=tkinter.BOTH,expand=True,padx=5, pady=5)
text1.pack(fill=tkinter.BOTH,expand=True)


bat3.pack(fill=tkinter.BOTH,expand=True)
frame2.pack(fill=tkinter.BOTH)
bat3_1.pack(side='left',fill=tkinter.BOTH,expand=True,padx=5, pady=5)
bat3_2.pack(side='left',fill=tkinter.BOTH,expand=True,padx=5, pady=5)

text2.pack(fill=tkinter.BOTH,expand=True)
root1.mainloop()