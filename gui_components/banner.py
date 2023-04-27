import tkinter as tk
import gui_components.click_functions as c

def banner(mainapp,l):

    #Création du bandeau cadre

    frame = tk.Frame(mainapp, background="#202020")
    frame.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black")
    frame.grid(row=0,column=0,columnspan=2,padx=0.009*l,pady=0.009*l,sticky=tk.W)# Ajouter du texte dans le cadre
    
    # Texte présentation
    label = tk.Label(frame, text="Simulation de la progression de l'épidémie de Covid-19 en fonction des mesures appliquées",font=("Helvetica Neue", int(0.014*l),"bold"), fg="white",bg="#202020")
    label.grid(row=0, column=1,padx=(0,0.11*l))
    
    # Logo Covid
    global img
    img = tk.PhotoImage(file="data/coronavirus.png")
    img = img.subsample(int(10000*1/l), int(10000*1/l))
    logocorona = tk.Label(frame, image=img, background="#202020")
    logocorona.grid(row=0,column=0, padx=0.009*l, pady=0.012*l)

    # Bouton Play
    play_button = tk.Label(frame, text="▶", font=("Play", int(0.012*l)), fg="white", bg="#202020",bd=1, relief="solid")
    play_button.grid(row=0, column=3, ipadx=0.009*l, ipady=0.007*l)
    play_button.bind("<Button-1>", lambda event: c.play())
    # Bouton Pause
    pause_button = tk.Label(frame, text="⏸", font=("Pause", int(0.012*l)),bg="#202020",bd=1, relief="solid")
    pause_button.grid(row=0, column=4, ipadx=0.009*l, ipady=0.007*l,padx=10)
    pause_button.bind("<Button-1>", lambda event: c.pause())
    # Bouton accelerer
    speed_button = tk.Label(frame, text="→", font=("Speed", int(0.012*l)), fg="white", bg="#202020",bd=1, relief="solid")
    speed_button.grid(row=0, column=5, ipadx=0.009*l, ipady=0.007*l)
    speed_button.bind("<Button-1>", lambda event: c.speed())
    return frame

def compteur(frame,n): 
    label2 = tk.Label(frame,width=7, text=f"Jour {n}",font=("Helvetica Neue", 17,"bold"), fg="grey",bg="#202020")
    label2.grid(row=0, column=2, padx=10)

    