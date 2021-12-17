from apps.api_covid import Apis
from apps.countries_app import *
from apps.frames_app import send_frame_infecteds, send_frame_recovereds, send_frame_deads



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


sel.bind("<<ComboboxSelected>>", selects)
window.mainloop()


        
