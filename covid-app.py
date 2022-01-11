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


# API

respon = requests.get("https://covid19.mathdro.id/api")
info = respon
info = json.loads(info.text)

infected = (info["confirmed"]["value"])
recovered = (info["recovered"]["value"])
deaths = (info["deaths"]["value"])
day = (info["lastUpdate"])
day = datetime.datetime.strptime(day, "%Y-%m-%dT%H:%M:%S.000Z")
day = day.strftime("%c")

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

#box selection country
label_country = Label(select_frame, text="Select Country:", width=13, height=1, pady=7, padx=0, 
                       relief="flat", anchor=NW, font=("Ivy 10 bold"), background=c6, fg=c0)
label_country.grid(row=0, column=0, pady=1, padx=13)

country=["Global", "Brazil", "Portugal", "USA", "France", "Spain", 
         "China", "Japan", "Switzerland", "Germany", "Italy", "Belgium", "Angola"]

sel = ttk.Combobox(select_frame, width=15, font=("Ivy 8 bold"))
sel["value"]=(country)
sel.grid(row=0, column=1, padx=0, pady=13)

# API

def selects(eventObject):
    
    if sel.get() == "Global":
        respon = requests.get("https://covid19.mathdro.id/api")
        info = respon
        info = json.loads(info.text)

        infected = (info["confirmed"]["value"])
        recovered = (info["recovered"]["value"])
        deaths = (info["deaths"]["value"])
        day = (info["lastUpdate"])
        day = datetime.datetime.strptime(day, "%Y-%m-%dT%H:%M:%S.000Z")
        day = day.strftime("%c")
        
        label_infected.configure(text=infected)
        label_recovered.configure(text=recovered)
        label_deaths.configure(text=deaths)
    
    else:
        select_country = sel.get()
        respon = requests.get("https://covid19.mathdro.id/api/countries/{}".format(select_country))
        info = respon
        info = json.loads(info.text)

        infected = (info["confirmed"]["value"])
        recovered = (info["recovered"]["value"])
        deaths = (info["deaths"]["value"])
        day = (info["lastUpdate"])
        day = datetime.datetime.strptime(day, "%Y-%m-%dT%H:%M:%S.000Z")
        day = day.strftime("%c")
        
        label_infected.configure(text=infected)
        label_recovered.configure(text=recovered)
        label_deaths.configure(text=deaths)
        

sel.bind("<<ComboboxSelected>>", selects)

window.mainloop()

