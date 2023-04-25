import tkinter as tk

def banner(mainapp):
    #Création du bandeau supérieur
    frame = tk.Frame(mainapp, background="white",height=2)
    # Ajouter du texte dans le cadre
    label = tk.Label(frame, text="Simulation de la progression de l'épidémie de Covid-19 en fonction des mesures appliquées",font=("Arial", 18), fg="red",bg="ivory")
    frame.grid(row=0,column=0, columnspan=2, sticky="ew", ipadx=10, ipady=10)
    label.grid(row=0, column=0)


    # Bouton Play
    play_button = tk.Button(frame, text="▶", font=("Play", 25))
    play_button.grid(row=0, column=1)

    # Bouton Pause
    pause_button = tk.Button(frame, text="⏸", font=("Pause", 25))
    pause_button.grid(row=0, column=2,)

    # Bouton Reload
    reload_button = tk.Button(frame, text="⟳", font=("Reload", 40))
    reload_button.grid(row=0, column=3)
