from app import AppCovid
from frames_app import *

from tkinter import *
from tkinter import ttk

#import library
from PIL import Image

from requests import request
import string
import json
import datetime
import requests

def frames_cov(framesApp):
    #red division frame
    app_cov_frame= Frame(window, width=840, height=50, background=c1, relief="flat")
    app_cov_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

    #covid infected frame
    send_frame_infected= Frame(window, width=220, height=100, background=c2, relief="flat")
    send_frame_infected.grid(row=1, column=0, sticky=NW, pady=5, padx=5)

    #covid retrieved frame
    send_frame_recovered= Frame(window, width=220, height=100, background=c2, relief="flat")
    send_frame_recovered.grid(row=1, column=1, sticky=NW, pady=5, padx=5)

    #frame of dead by covid
    send_frame_deaths= Frame(window, width=220, height=100, background=c2, relief="flat")
    send_frame_deaths.grid(row=1, column=2, sticky=NW, pady=5, padx=5)

    #red division frame
    select_frame= Frame(window, width=840, height=50, background=c6, relief="flat")
    select_frame.grid(row=2, column=0, columnspan=3, sticky=N, pady=10)

    #labels for app_cov_frame

    img=Image.open("image/covidgreen.png")
    img=img.resize((60, 60))
    img=img.save("covidgreen1.png")
    imagecov= PhotoImage(file="covidgreen1.png")

    app_image = Label(app_cov_frame, image=imagecov, width=350, pady=20, anchor=NE,
            relief="flat", background=c1,)
    app_image.grid(row=0, column=0, pady=5)

    app_name = Label(app_cov_frame, text="COVID-19", width=20, height=1, pady=20,
                    relief="flat", anchor=NW, font=("Helvetica 25 bold"), background=c1, fg=c5)
    app_name.grid(row=0, column=1, pady=5)

    #label for send_frame_infected
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

    #label for send_frame_recovered
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

    #label for send_frame_dead
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


sel.bind("<<ComboboxSelected>>", selects)
window.mainloop()
