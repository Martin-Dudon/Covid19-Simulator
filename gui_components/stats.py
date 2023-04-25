import tkinter as tk

def stats(mainapp):
    #Création du bandeau supérieur
    stframe = tk.Frame(mainapp, background="white",width=60, height=2)
    # Ajouter du texte dans le cadre
    label = tk.Label(stframe, text="Simulation de la progression de l'épidémie de Covid-19 en fonction des mesures appliquées")
    stframe.grid(row=1,column=0, columnspan=2)

    label = tk.Label(stframe, width=60, height=5, text="Mon texte ici", bg="ivory", font=("Arial", 18), fg="red")
    label.grid(row=0, column=0,padx=20, pady=20)