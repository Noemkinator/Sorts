# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 20:38:46 2022

@author: xzaji
"""
import tkinter as tk
from tkinter import filedialog, Text
import os
from Sorts import *
global start

def plotdata():
    n=int(input())
    start=tm.perf_counter_ns()
    bubblesort(randarr(n))
    insertsort(randarr(n))
    mergesort(randarr(n))
    quicksort(randarr(n),0,n-1)
    shellsort(randarr(n))
    sorts()
    
root = tk.Tk()
root.title("Sorting Algorithms")
canvas = tk.Canvas(root, height=400, 
                   width=600, 
                   bg="#333533", 
                   bd=0)
plot_button = tk.Button(root, command= plotdata, 
                        height = 2,
                        width = 10,
                        text = "Plot",
                        bg="#333533")

plot_button.pack()
canvas.pack()
root.mainloop()