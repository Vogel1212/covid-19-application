from app import Window
from apps.frames_app import *

# API Values

class Apis:
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
    