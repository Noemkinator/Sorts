# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 20:38:46 2022

@author: xzaji
"""
import tkinter as tk
from tkinter import filedialog, Text,ttk
from PIL import Image, ImageTk
import os
from Sorts import *
import Sorts as srt

def plotdata():
    n=int(input())
    srt.start=tm.perf_counter_ns()
    bubblesort(randarr(n))
    insertsort(randarr(n))
    mergesort(randarr(n))
    quicksort(randarr(n),0,n-1)
    shellsort(randarr(n))
    sorts()
    my_img=ImageTk.PhotoImage(Image.open('plots/plot.png').resize((1520,880)))
    my_label = tk.Label(image=my_img)
    my_label.pack()
    
root = tk.Tk()
root.title("Sorting Algorithms")
root.iconbitmap('src/icon.ico')
plot_button = tk.Button(root, command= plotdata, 
                        height = 2,
                        width = 20,
                        text = "Plot",
                        bg="#333533")

plot_button.pack()
root.mainloop()