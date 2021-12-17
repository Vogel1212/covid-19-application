from app import AppCovid
from frames_app import *

from apps.api_covid import Apis

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

class Frames:
        def __init__(self) -> None:
                label_infected = Label(send_frame_infected, text="Infected", width=20, height=1, pady=7, padx=0, 
                                relief="flat", anchor=NW, font=("Courier 15 bold"), background=c2, fg=c0)
                label_infected.grid(row=0, column=0, pady=1, padx=13)

                label_infected = Label(send_frame_infected, text=infected, width=12, height=1, pady=7, padx=0, 
                                relief="flat", anchor=NW, font=("Courier 25 bold"), background=c2, fg=c0)
                label_infected.grid(row=1, column=0, pady=1)

                send_forms = Label(send_frame_infected, text=str(day), width=25, height=1, pady=7, padx=0, 
                                relief="flat", anchor=NW, font=("Courier 11 bold"), background=c2, fg=c0)
                send_forms.grid(row=2, column=0, pady=1)

                send_forms = Label(send_frame_infected, text="Total active covid-19 cases", width=33, height=1, pady=7, padx=0, 
                                relief="flat", anchor=NW, font=("Courier 8 bold"), background=c2, fg=c0)
                send_forms.grid(row=3, column=0, pady=1, padx=13)

                lin_blue = Label(send_frame_infected, text="", width=19, height=1, pady=1, padx=0, 
                                relief="flat", anchor=NW, font=("Courier 1 bold"), background=c3, fg=c0)
                lin_blue.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)
        
        
def send_frame_recovered(recovereds):
        label_recovered = Label(send_frame_recovered, text="Recovered", width=20, height=1, pady=7, padx=0, 
                        relief="flat", anchor=NW, font=("Courier 15 bold"), background=c2, fg=c0)
        label_recovered.grid(row=0, column=0, pady=1, padx=13)

        label_recovered = Label(send_frame_recovered, text=recovered, width=12, height=1, pady=7, padx=0, 
                        relief="flat", anchor=NW, font=("Courier 25 bold"), background=c2, fg=c0)
        label_recovered.grid(row=1, column=0, pady=1)

        send_forms = Label(send_frame_recovered, text=str(day), width=25, height=1, pady=7, padx=0, 
                        relief="flat", anchor=NW, font=("Courier 11 bold"), background=c2, fg=c0)
        send_forms.grid(row=2, column=0, pady=1)

        send_forms = Label(send_frame_recovered, text="Total recovered covid-19 cases", width=33, height=1, pady=7, padx=0, 
                        relief="flat", anchor=NW, font=("Courier 8 bold"), background=c2, fg=c0)
        send_forms.grid(row=3, column=0, pady=1, padx=13)

        lin_green = Label(send_frame_recovered, text="", width=19, height=1, pady=1, padx=0, 
                        relief="flat", anchor=NW, font=("Courier 1 bold"), background=c5, fg=c0)
        lin_green.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)
        
def send_frame_deaths(deaths):
        label_deaths = Label(send_frame_deaths, text="Deaths", width=20, height=1, pady=7, padx=0, 
                        relief="flat", anchor=NW, font=("Courier 15 bold"), background=c2, fg=c0)
        label_deaths.grid(row=0, column=0, pady=1, padx=13)

        label_deaths = Label(send_frame_deaths, text=deaths, width=12, height=1, pady=7, padx=0, 
                        relief="flat", anchor=NW, font=("Courier 25 bold"), background=c2, fg=c0)
        label_deaths.grid(row=1, column=0, pady=1)

        send_forms = Label(send_frame_deaths, text=str(day), width=25, height=1, pady=7, padx=0, 
                        relief="flat", anchor=NW, font=("Courier 11 bold"), background=c2, fg=c0)
        send_forms.grid(row=2, column=0, pady=1)

        send_forms = Label(send_frame_deaths, text="Total de Deaths de covid-19", width=33, height=1, pady=7, padx=0, 
                        relief="flat", anchor=NW, font=("Courier 8 bold"), background=c2, fg=c0)
        send_forms.grid(row=3, column=0, pady=1, padx=13)

        lin_green = Label(send_frame_deaths, text="", width=19, height=1, pady=1, padx=0, 
                        relief="flat", anchor=NW, font=("Courier 1 bold"), background=c1, fg=c0)
        lin_green.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)