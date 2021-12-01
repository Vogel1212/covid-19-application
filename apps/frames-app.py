# from tkinter import *
# from tkinter import ttk

# #######colors
# # c0 = "#000000"  # black
# # c1 = "#cc1d4e"  # red
# # c2 = "#feffff"  # white
# # c3 = "#0074eb"  # blue
# # c4 = "#435e5a"  # #435e5a
# # c5 = "#59b356"  # green
# # c6 = "#d9d9d9"  # grey
# #######

# class FramesApp:
#     def __init__(self, window = Tk(),
#         c0="#000000",
#         c1="#cc1d4e",
#         c2="#feffff",
#         c3="#0074eb",
#         c4="#435e5a",
#         c5="#59b356",
#         c6="#d9d9d9"
#                  ):

#         window.title('')
#         window.resizable(width=FALSE, height=FALSE)
#         window.geometry('835x360')
#         window.configure(background=c6)

#         #red division frame
#         app_cov_frame= Frame(window, width=840, height=50, background=c1, relief="flat")
#         app_cov_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

#         #covid infected frame
#         send_frame_infected= Frame(window, width=220, height=100, background=c2, relief="flat")
#         send_frame_infected.grid(row=1, column=0, sticky=NW, pady=5, padx=5)

#         #covid retrieved frame
#         send_frame_recovered= Frame(window, width=220, height=100, background=c2, relief="flat")
#         send_frame_recovered.grid(row=1, column=1, sticky=NW, pady=5, padx=5)

#         #frame of dead by covid
#         send_frame_deaths= Frame(window, width=220, height=100, background=c2, relief="flat")
#         send_frame_deaths.grid(row=1, column=2, sticky=NW, pady=5, padx=5)

#         #red division frame
#         select_frame= Frame(window, width=840, height=50, background=c6, relief="flat")
#         select_frame.grid(row=2, column=0, columnspan=3, sticky=N, pady=10)

#         #labels for app_cov_frame
#         app_name = Label(app_cov_frame, text="COVID-19", width=20, height=1, pady=20,
#                          relief="flat", anchor=CENTER, font=("Helvetica 25 bold"), background=c1, fg=c0)

#         app_name.grid(row=0, column=0, pady=5)

#         #label for send_frame_infected
#         label_infected = Label(send_frame_infected, text="Infected", width=20, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 15 bold"), background=c2, fg=c0)
#         label_infected.grid(row=0, column=0, pady=1, padx=13)

#         label_infected = Label(send_frame_infected, text="5.126", width=12, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 25 bold"), background=c2, fg=c0)
#         label_infected.grid(row=1, column=0, pady=1)

#         send_forms = Label(send_frame_infected, text="Segunda-Feira 22/11/2021", width=25, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 11 bold"), background=c2, fg=c0)
#         send_forms.grid(row=2, column=0, pady=1)

#         send_forms = Label(send_frame_infected, text="Total de casos ativos de covid-19", width=33, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 8 bold"), background=c2, fg=c0)
#         send_forms.grid(row=3, column=0, pady=1, padx=13)

#         lin_blue = Label(send_frame_infected, text="", width=19, height=1, pady=1, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 1 bold"), background=c3, fg=c0)
#         lin_blue.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

#         #label for send_frame_recovered
#         label_recovered = Label(send_frame_recovered, text="Recovered", width=20, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 15 bold"), background=c2, fg=c0)
#         label_recovered.grid(row=0, column=0, pady=1, padx=13)

#         label_recovered = Label(send_frame_recovered, text="5.126", width=12, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 25 bold"), background=c2, fg=c0)
#         label_recovered.grid(row=1, column=0, pady=1)

#         send_forms = Label(send_frame_recovered, text="Segunda-Feira 22/11/2021", width=25, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 11 bold"), background=c2, fg=c0)
#         send_forms.grid(row=2, column=0, pady=1)

#         send_forms = Label(send_frame_recovered, text="Total de Recovered de covid-19", width=33, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 8 bold"), background=c2, fg=c0)
#         send_forms.grid(row=3, column=0, pady=1, padx=13)

#         lin_green = Label(send_frame_recovered, text="", width=19, height=1, pady=1, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 1 bold"), background=c5, fg=c0)
#         lin_green.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

#         #label for send_frame_dead
#         label_deaths = Label(send_frame_deaths, text="Deaths", width=20, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 15 bold"), background=c2, fg=c0)
#         label_deaths.grid(row=0, column=0, pady=1, padx=13)

#         label_deaths = Label(send_frame_deaths, text="5.126", width=12, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 25 bold"), background=c2, fg=c0)
#         label_deaths.grid(row=1, column=0, pady=1)

#         send_forms = Label(send_frame_deaths, text="Segunda-Feira 22/11/2021", width=25, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 11 bold"), background=c2, fg=c0)
#         send_forms.grid(row=2, column=0, pady=1)

#         send_forms = Label(send_frame_deaths, text="Total de Deaths de covid-19", width=33, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 8 bold"), background=c2, fg=c0)
#         send_forms.grid(row=3, column=0, pady=1, padx=13)

#         lin_green = Label(send_frame_deaths, text="", width=19, height=1, pady=1, padx=0, 
#                                relief="flat", anchor=NW, font=("Courier 1 bold"), background=c1, fg=c0)
#         lin_green.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)