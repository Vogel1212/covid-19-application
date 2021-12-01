# from tkinter import *
# from tkinter import ttk

# #######colors
# c0 = "#000000"  # black
# c1 = "#cc1d4e"  # red
# c2 = "#feffff"  # white
# c3 = "#0074eb"  # blue
# c4 = "#435e5a"  # #435e5a
# c5 = "#59b356"  # green
# c6 = "#d9d9d9"  # grey
# #######


# class CountriesApp:
#     def __init__(self, window = Tk()):
#         #box selection country
#         label_country = Label(select_frame, text="Select Country:", width=13, height=1, pady=7, padx=0, 
#                                relief="flat", anchor=NW, font=("Ivy 10 bold"), background=c6, fg=c0)
#         label_country.grid(row=0, column=0, pady=1, padx=13)

#         country=["Brazil", "Portugal", "USA", "France", "Spain", "China", "Japan", "Switzerland", "Germany", "Italy", "Belgium"]

#         sel = ttk.Combobox(select_frame, width=15, font=("Ivy 8 bold"))
#         sel["value"]=(country)
#         sel.grid(row=0, column=1, padx=0, pady=13)

#         window.mainloop()