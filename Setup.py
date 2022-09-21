from distutils.core import setup
import py2exe
import os
import matplotlib.pyplot as plt
from functools import wraps
import time as tm
import random as rnd
import tkinter as tk
from tkinter import filedialog, Text,ttk
from PIL import Image, ImageTk
import os
from Sorts import *
import Sorts as srt

setup(windows=[
    {
     "script":'App.py',
     "icon_resources":[(1,"src/icon.ico")]
     }
    ]
    )