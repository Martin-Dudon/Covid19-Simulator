import tkinter as tk    
import gui_components.banner as bn
import gui_components.stats as st
import gui_components.actions as a
import graphs.actualisation as act
import graphs.SEIR_graphs_tk as grph
import gui_components.click_functions as c

mainapp = tk.Tk()  # Crée une instance de la classe Tk
l = 1000#mainapp.winfo_screenwidth()#
h =820 #mainapp.winfo_screenheight()# 
print(l,h)

mainapp.geometry(f"{1280}x{700}+0+0") # Configure la géométrie de la fenêtre # Bloque le redimensionnement de la fenêtre
mainapp.title("SEIR model simulation") # Configure le titre de la fenêtre
mainapp['bg']="#303030" # Configure la couleur de fond de la fenêtre

frame=bn.banner(mainapp,l)
global U
U=st.stats(mainapp,l)
a.action(mainapp,l)

# Fonction pour actualiser l'affichage toutes les secondes

g=grph.graphs_gui(mainapp,l,h)

def actualisation(n=0):
    global U
    if n >= 400:
        return
    if c.redem == True:
        mainapp.destroy()
    act.updategraph(n,mainapp,l,h,g)
    st.updatestats(n,l,U)
    bn.compteur(frame,n,l)

    while c.lecture == False:
            mainapp.update() 
    mainapp.after(int(100/c.sp), actualisation, n+1)

actualisation()
# Boucle principale
mainapp.mainloop()
