import tkinter as tk
from tkinter import Message ,Text
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.font as font
from tkinter import filedialog
import tkinter.messagebox as tm
from tkinter import ttk
import time
import matplotlib.pyplot as plt
import CreateDataset as pre
import DTALG as dt
import SVMALG as svm
import XGBOOSTALG as xgb

fontScale=1
fontColor=(0,0,0)
cond=0

bgcolor="#d7837f"
fgcolor="white"

window = tk.Tk()
window.title("Twitter Sentiment Analysis")

 
window.geometry('1280x720')
window.configure(background=bgcolor)
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message1 = tk.Label(window, text="Twitter Sentiment Analysis by Shreyas K" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message1.place(x=100, y=10)

lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
lbl.place(x=10, y=200)

txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=300, y=215)




def browse():
	path=filedialog.askopenfilename()
	print(path)
	txt.delete(0, 'end')
	txt.insert('end',path)
	if path !="":
		print(path)
	else:
		tm.showinfo("Input error", "Select Dataset")	

	
def clear():
	txt.delete(0, 'end') 
	txt1.delete(0, 'end') 
	txt2.delete(0, 'end') 

def preprocess():
	pre.process()
	tm.showinfo("Input", "Preprocess Successfully Finished")


def dtprocess():
	sym=txt.get()
	if sym != "" :
		dt.process(sym)
		tm.showinfo("Input", "Decision Tree Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")

def svmprocess():
	sym=txt.get()
	if sym != "" :
		svm.process(sym)
		tm.showinfo("Input", "SVM Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")

def xgbprocess():
	sym=txt.get()
	if sym != "" :
		xgb.process(sym)
		tm.showinfo("Input", "XGBOOST Successfully Finished")
	else:
		tm.showinfo("Input error", "Select Dataset")

browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
browse.place(x=650, y=200)

pre1 = tk.Button(window, text="Preprocess", command=preprocess  ,fg=fgcolor  ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
pre1.place(x=10, y=600)

texta1 = tk.Button(window, text="Decision Tree", command=dtprocess  ,fg=fgcolor ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
texta1.place(x=200, y=600)

texta2 = tk.Button(window, text="SVM", command=svmprocess  ,fg=fgcolor ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
texta2.place(x=400, y=600)

texta3 = tk.Button(window, text="XGBOOST", command=xgbprocess  ,fg=fgcolor ,bg=bgcolor  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
texta3.place(x=600, y=600)



 
window.mainloop()
