import json
from difflib import get_close_matches
from tkinter import *

data=json.load(open("data.json"))

frame=Tk()
frame.geometry("660x300+550+350")
frame.title("Dictionary")
frame.call('wm', 'iconphoto', frame._w, PhotoImage(file='book.png'))

def ans(word):
	word=word.lower()
	if word in data:
		return data[word]

	elif word.title() in data:
		return data[word.title()]

	elif word.upper() in data:
		return data[word.upper()]
		
	elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
		msgask=Message(frame,text="Did you mean %s instead ?" % get_close_matches(word, data.keys(), cutoff=0.8)[0],width="650")
		msgask.place(y=60)
		var=IntVar()
		btnyes=Button(frame,text="YES",command=lambda:var.set(1))
		btnyes.place(x=10,y=80)
		btnno=Button(frame,text="NO",command=lambda:var.set(2))
		btnno.place(x=70,y=80)

		btnyes.wait_variable(var) and btnno.wait_variable(var)
		
		if var.get() == 1:
			return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
		elif var.get() == 2:
			return "The word doesn't exist. Please double check it."
	
	else:
		return "The word doesn't exist. Please double check it."

def showinfo():
	lblclear=Label(frame,text="",width="650",height="250")
	lblclear.place(y=60)
	word=entword.get()
	answer=ans(word)
	lblclear=Label(frame,text="",width="650",height="250")
	lblclear.place(y=60)
	if type(answer)==list:
		c=0
		for i in answer:
			msganswer=Message(frame,text=i,width="650")
			msganswer.place(y=60+c*20)
			c=c+1
	else:
		msganswer=Message(frame,text=answer,width="650")
		msganswer.place(y=60)
	entword.focus()


lblword=Label(frame,text="Enter the word")
lblword.grid(row=0,column=0)
entword=Entry(frame,bd=3)
entword.grid(row=0,column=1)
entword.focus()
btnword=Button(frame,text="Enter",command=showinfo)
btnword.grid(row=1,column=1)

frame.mainloop()