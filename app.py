from tkinter import *
from apps.api_covid import Apis
from apps.frames_app import send_frame_infecteds, send_frame_recovereds, send_frame_deads

#######colors
c0 = "#000000"  # black
c1 = "#cc1d4e"  # red
c2 = "#feffff"  # white
c3 = "#0074eb"  # blue
c4 = "#435e5a"  # #435e5a
c5 = "#59b356"  # green
c6 = "#d9d9d9"  # grey
#######

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
             
        window = Tk()
        window.title('')
        window.resizable(width=FALSE, height=FALSE)
        window.geometry('835x360')
        window.configure(background=c6)

    def get_frames(self):
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
        
    def labelCountry(self):
        label_country = Label(select_frame, text="Select Country:", width=13, height=1, pady=7, padx=0, 
                            relief="flat", anchor=NW, font=("Ivy 10 bold"), background=c6, fg=c0)
        label_country.grid(row=0, column=0, pady=1, padx=13)

        country=["Global", "Brazil", "Portugal", "USA", "France", "Spain", 
                "China", "Japan", "Switzerland", "Germany", "Italy", "Belgium", "Angola"]

        sel = ttk.Combobox(select_frame, width=15, font=("Ivy 8 bold"))
        sel["value"]=(country)
        sel.grid(row=0, column=1, padx=0, pady=13)


window = Window() 

sel.bind("<<ComboboxSelected>>", selects)
window.mainloop()


        
