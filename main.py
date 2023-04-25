import tkinter as tk 
import gui_components.banner as bn
import gui_components.stats as st
import gui_components.actions as a
import graphs.actualisation as act

# Création de la fenêtre principale
mainapp = tk.Tk()  # Crée une instance de la classe Tk
mainapp.geometry("1920x1080+0+0") # Configure la géométrie de la fenêtre # Bloque le redimensionnement de la fenêtre
mainapp.title("SEIR model simulation") # Configure le titre de la fenêtre
mainapp['bg']="#282828" # Configure la couleur de fond de la fenêtre

bn.banner(mainapp)
st.stats(mainapp)
a.action(mainapp)

# Fonction pour actualiser l'affichage toutes les secondes

def actualisation(n=0):
    if n >= 300:
        return
    act.updategraph(n,mainapp)
    mainapp.after(500, actualisation, n+1)

actualisation()

# Boucle principale
mainapp.mainloop()