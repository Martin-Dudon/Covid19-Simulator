import tkinter as tk

def action(mainapp):
    #Création du bandeau supérieur
    actframe = tk.Frame(mainapp, background="white",width=60, height=2)
    # Ajouter du texte dans le cadre
    label = tk.Label(actframe, text="Simulation de la progression de l'épidémie de Covid-19 en fonction des mesures appliquées")
    actframe.grid(row=3,column=1,sticky="ns")

    label = tk.Label(actframe, width=60, height=2, text="Mon texte ici", bg="ivory", font=("Arial", 18), fg="red")
    label.grid(row=0, column=0,padx=20, pady=20)