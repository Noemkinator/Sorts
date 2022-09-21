# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 20:38:46 2022

@author: xzaji
"""
import tkinter as tk
from tkinter import filedialog, Text,ttk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from Sorts import *
import Sorts as srt

def plotdata():
    n= int(mystr.get())
    srt.start=tm.perf_counter_ns()
    #bubblesort(randarr(n))
    #insertsort(randarr(n))
    mergesort(randarr(n))
    quicksort(randarr(n),0,n-1)
    shellsort(randarr(n))
    radixsort(randarr(n))
    sorts()
    my_img=ImageTk.PhotoImage(Image.open('plots/plot.png').resize((1520,880)))
    my_label = tk.Label(image=my_img)
    my_label.place(relx=0.1,y=50)
root = tk.Tk()

mystr=tk.StringVar(root)

root.title("Sorting Algorithms")
try:
    root.iconbitmap("src/icon.ico")
except:
    pass
txtfld=tk.Entry(root, 
             text="This is Entry Widget", 
             textvariable=mystr,
             bd=5)

txtfld.place(x=10, y=10)

plot_button = tk.Button(root, command= plotdata, 
                        height = 2,
                        width = 20,
                        text = "Plot")

plot_button.place(x=150,y=0)
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes('-fullscreen', False)
root.state('zoomed')
root.mainloop()