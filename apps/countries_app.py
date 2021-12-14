

#box selection country
label_country = Label(select_frame, text="Select Country:", width=13, height=1, pady=7, padx=0, 
                       relief="flat", anchor=NW, font=("Ivy 10 bold"), background=c6, fg=c0)
label_country.grid(row=0, column=0, pady=1, padx=13)

country=["Global", "Brazil", "Portugal", "USA", "France", "Spain", 
         "China", "Japan", "Switzerland", "Germany", "Italy", "Belgium", "Angola"]

sel = ttk.Combobox(select_frame, width=15, font=("Ivy 8 bold"))
sel["value"]=(country)
sel.grid(row=0, column=1, padx=0, pady=13)