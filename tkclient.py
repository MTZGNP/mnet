import tkinter as tk
from tkinter import messagebox
import json
from time import sleep
import requests

##use the source code as much as you like without removing this comment block
##              _                        
##             | |                       
##    _ __ ___ | |_ ______ _ _ __  _ __  
##   | '_ ` _ \| __|_  / _` | '_ \| '_ \ 
##   | | | | | | |_ / / (_| | | | | |_) |
##   |_| |_| |_|\__/___\__, |_| |_| .__/ 
##                      __/ |     | |    
##                     |___/      |_|
##
##mutaz.shamaileh2005@gmail.com

ex=""
root =tk.Tk()
name=""
room="1"
pw="gnp"
nameLabel=tk.Label(root,text ="name ")
roomLabel=tk.Label(root,text ="room ")
pwLabel=tk.Label(root,text ="password ")
namePrev=tk.Label(root,text=name)
roomPrev=tk.Label(root,text=room)
nameBox=tk.Entry(root)
roomBox=tk.Entry(root)
pwBox=tk.Entry(root,show="*" )
roomBox.insert(0,room)
pwBox.insert(0,pw)
messageList= tk.Listbox(root)
messageBox=tk.Entry(root)
def update_loop():
	for mess in json.loads(requests.get(url="http://mtzgnp.pythonanywhere.com/get?room=%s" % room).text)[messageList.size():]:
		messageList.insert(tk.END,"%s : %s" % (mess["name"],mess["message"]))
	root.after(2000,update_loop)
def send():
	if name =="":
		messagebox.showerror("error","please enter name")
		return 1
	requests.get(url ="http://mtzgnp.pythonanywhere.com/post?room=%s&name=%s&message=%s" %(room,name,messageBox.get()))
def change():
	global name
	global room
	global pw
	if room !=roomBox.get() and roomBox.get() != "":
		room=roomBox.get()
		roomPrev["text"]=room
	if name != nameBox.get():
		name=nameBox.get()
		namePrev["text"]=name
	pw=pwBox.get()
changeButton=tk.Button(root,text="change",command=change)
sendButton=tk.Button(root,text="send",command=send)
nameLabel.grid(row=0)
nameBox.grid(row=0,column=1)
namePrev.grid(row=0,column=2)
roomLabel.grid(row=1)
roomBox.grid(row=1,column=1)
roomPrev.grid(row=1,column=2)
pwLabel.grid(row=2)
pwBox.grid(row=2,column=1)
changeButton.grid(row=2,column=2)
messageList.grid(row=3,columnspan=3)
messageBox.grid(row=4,columnspan=3)
sendButton.grid(row=4,column=2)
update_loop()
root.mainloop()
