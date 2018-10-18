from tkinter import *
counter=0

def count1():
	global counter
	counter+=1
	label.config(text=str(counter))
	label.after(1,count1)


def count2():
	global counter
	counter+=1
	label.config(text=str(counter))
	label.after(100,count2)


def count3():
	global counter
	counter+=1
	label.config(text=str(counter))
	label.after(1000,count3)

def stop():
	label.destroy()
	if v.get()==1:
		label1.config(text=str(float(counter/1000)),anchor=E)
	if v.get()==2:
		label1.config(text=str(counter/10),anchor=E)
	if v.get()==3:
		label1.config(text=str(counter),anchor=E)	
	label1.grid(row=0)

master=Tk()
master.title("Stop Watch")

label=Label(master,anchor=E)
label.grid(row=0)

label1=Label(master,anchor=E)

v=IntVar()

buttonA=Radiobutton(master,text='1mS',command=count1,width=6,variable=v,value=1,indicatoron=0)
buttonA.grid(row=1,column=0,ipadx=10,ipady=4)

buttonB=Radiobutton(master,text='100mS',command=count2,width=6,variable=v,value=2,indicatoron=0)
buttonB.grid(row=1,column=1,ipadx=10,ipady=4)

buttonC=Radiobutton(master,text='1S',command=count3,width=6,variable=v,value=3,indicatoron=0)
buttonC.grid(row=1,column=2,ipadx=10,ipady=4)

button1=Button(master,text="Quit",command=quit,width=6)
button1.grid(row=2,column=1)

button2=Button(master,text='Stop',width=6,command=stop)
button2.grid(row=2,column=0)

master.mainloop()

#with grid pack cannot be used
#pack used to show widgets on master
#after is called only once
