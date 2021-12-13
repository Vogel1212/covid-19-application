from tkinter import *
from tkinter import ttk

#import library
from PIL import Image

from requests import request
import string
import json
import datetime
import requests


#######colors
c0 = "#000000"  # black
c1 = "#cc1d4e"  # red
c2 = "#feffff"  # white
c3 = "#0074eb"  # blue
c4 = "#435e5a"  # #435e5a
c5 = "#59b356"  # green
c6 = "#d9d9d9"  # grey
#######

window = Tk()

window.title('')
window.resizable(width=FALSE, height=FALSE)
window.geometry('835x360')
window.configure(background=c6)
