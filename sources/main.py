import tkinter as tk
from gui_components import banner as bn, stats as st, actions as a
from graphs import actualisation as act, SEIR_graphs_tk as grph

"""
On importe plusieurs modules nécessaires à l'interface utilisateur et à l'affichage de graphiques. 
On utilise les modules tkinter pour la création de la fenêtre, gui_components.banner pour la bannière de l'application, 
gui_components.stats pour l'affichage des statistiques, gui_components.actions pour les actions de l'utilisateur, 
graphs.actualisation pour la mise à jour des données, et graphs.SEIR_graphs_tk pour l'affichage des graphiques.
"""

mainapp = tk.Tk()  # Crée une instance nouvelle fenêtre
# Définit des coefficients de longueur et largeur pour le calcul des dimensions des widgets
l = 1000 
h =820 

mainapp.geometry(f"{1280}x{695}+0+0") # Configure les dimensions de la fenêtre
mainapp.title("SEIR model simulation") # Configure le titre de la fenêtre
mainapp['bg']="#303030" # Configure la couleur de fond de la fenêtre
def run_program(mainapp, l, h):

    """
    Exécute le programme principal avec les paramètres spécifiés.

    Args:
        mainapp: l'instance de l'application principale
        l: la liste de données pour l'application
        h: le dictionnaire de paramètres pour les graphiques

    Returns:
        None
    """

    
    banner = bn.banner(mainapp, l) # Affiche la bannière de l'interface graphique
    stats = st.stats(mainapp, l) # Affiche les cases où il y aura les statistiques
    a.action(mainapp, l) # Affiche les cases où il y aura les mesures sanitaires
    graphs = grph.graphs_gui(mainapp, l, h) # Affiche les repères des graphiques

    def actualisation(n=0, graphs=graphs, stats=stats, banner=banner):
        
        """
        Met à jour l'interface graphique et les statistiques.

        Args:
            n: le numéro de la mise à jour (par défaut : 0)
            graphs: les repères des graphiques
            stats: les cases où il y aura les statistiques
            banner: la bannière de l'interface graphique

        Returns:
            None
        """
        
        if n >= 400:
            return
        if bn.restart == "finish":
            n = 0
            graphs = grph.graphs_gui(mainapp, l, h)
        act.updategraph(n, mainapp, l, h, graphs)
        st.updatestats(n, l, stats)
        bn.compteur(banner, n, l)
        while not bn.lecture or not bn.restart:
            mainapp.update()
        mainapp.after(int(100 / bn.sp), actualisation, n + 1, graphs, stats, banner)

    actualisation()


run_program(mainapp,l,h)

mainapp.mainloop() # Boucle principale
