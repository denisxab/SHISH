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

	a =[

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
		'', '\n', '\t','\\','//','/',

	 	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
	 	'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
	 	'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
	 	'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
	 	'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
	 	'Y', 'Z', 

	  ]


	l = {}

	for x in a:
		l[x]=[]
		for y in range(rand):
			l[x].append(random.getrandbits(bit))

	with open('key.json','w',encoding='utf-8') as file_j:
		json.dump(l,file_j,sort_keys=False,ensure_ascii=False)



	chek_d()
	return l

def code():
	slo = text1.get(1.0, 'end-1c')

	try:
		with open('key.json','r',encoding='utf-8') as json_j:
			red = json.load(json_j)
			v = []
			for x in slo:
				if x in red:
					v.append(random.choice(red[x]))
	except FileNotFoundError:
		text2.delete(1.0, tkinter.END)
		text2.insert(tkinter.INSERT,"NO FILE")
		text1.delete(1.0, tkinter.END)
		text1.insert(tkinter.INSERT,"NO FILE")
		return

	f = ''
	for x in v:
		f+='{}-'.format(x)



	text2.delete(1.0, tkinter.END)
	text2.insert(tkinter.INSERT,f)
	return v

def incode():
	try:
		list_code = []
		g = text2.get(1.0, 'end-1c').split('-')
		for x in g:
			try:
				list_code.append(int(x))
			except ValueError:
				continue

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

def clear():
	text1.delete(1.0, tkinter.END)
	text2.delete(1.0, tkinter.END)

def chek_d():
	if not 'key.json' in os.listdir():
		frame4.pack_forget()
		bat_clear.pack_forget()
		root1.geometry('666x380')
		bat1['height']=10
		text0_1['height']=5
		text0_2['height']=5

	if 'key.json' in os.listdir():
		bat1.pack_forget()
		frame0.pack_forget()
		text0_1.pack_forget()
		text0_2.pack_forget()
		frame4.pack(fill=tkinter.BOTH,expand=True)
		bat_clear.pack(fill=tkinter.BOTH)

root1=tkinter.Tk()
root1.geometry('666x380')

try:
	root1.iconbitmap('96.ico')
except:
	root1.iconbitmap()


bat1 = tkinter.Button(root1, width=5,text='Создать ключ',  command = shi,fg='#ffffff',bg='#4b5463')
frame0 = tkinter.Frame(root1)
text0_1 = tkinter.Text(frame0,width=5, height=1,bg='#ffffff')
text0_2 = tkinter.Text(frame0,width=5, height=1,bg='#ffffff')



frame4 = tkinter.Frame(root1)
frame2_1 = tkinter.Frame(frame4)
bat2 = tkinter.Button(frame2_1, width=5,height=5,text='Закодировать',command = code,fg='#ffffff',bg='#4b5463')
text1 = tkinter.scrolledtext.ScrolledText(frame2_1,width=10, height=11)
frame1 = tkinter.Frame(frame2_1)
bat2_1 = tkinter.Button(frame1, width=5,text='COPY',command = copy0,bg='#fade55')
bat2_2 = tkinter.Button(frame1, width=5,text='PAST',command = paste0,bg='#c3f229')


frame3_1 = tkinter.Frame(frame4)
bat3 = tkinter.Button(frame3_1, width=5,height=5,text='Декодировать',command = incode,fg='#ffffff',bg='#4b5463')
text2 = tkinter.scrolledtext.ScrolledText(frame3_1,width=10, height=11)
frame2 = tkinter.Frame(frame3_1)
bat3_1 = tkinter.Button(frame2, width=5,text='COPY',command = copy1,bg='#fade55')
bat3_2 = tkinter.Button(frame2, width=5,text='PAST',command = paste1,bg='#c3f229')

bat_clear = tkinter.Button(root1, width=5,height=3,text='X_X',command = clear,fg='#ffffff',bg='#4b5463')


#_________________________________________________________________#
bat1.pack(fill=tkinter.BOTH)
frame0.pack(fill=tkinter.BOTH)
text0_1.pack(side='left',fill=tkinter.BOTH,expand=True,padx=5, pady=5)
text0_2.pack(side='left',fill=tkinter.BOTH,expand=True,padx=5, pady=5)


frame4.pack(fill=tkinter.BOTH,expand=True)
frame2_1.pack(side='left',fill=tkinter.BOTH,expand=True)
bat2.pack(fill=tkinter.BOTH)
text1.pack(fill=tkinter.BOTH,expand=True)
frame1.pack(fill=tkinter.BOTH)
bat2_1.pack(side='left',fill=tkinter.BOTH,expand=True,)
bat2_2.pack(side='left',fill=tkinter.BOTH,expand=True,)


frame3_1.pack(side='left',fill=tkinter.BOTH,expand=True)
bat3.pack(fill=tkinter.BOTH)
text2.pack(fill=tkinter.BOTH,expand=True)
frame2.pack(fill=tkinter.BOTH)
bat3_1.pack(side='left',fill=tkinter.BOTH,expand=True,)
bat3_2.pack(side='left',fill=tkinter.BOTH,expand=True,)


bat_clear.pack(fill=tkinter.BOTH)


chek_d()
root1.mainloop()