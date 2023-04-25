from graphs.SEIR_model import newvalues, t, S, E, I, I1, I2, I3, D, R, Ddaily
import graphs.SEIR_graphs_tk as grph

g=["ax","ax2","ax3","canvas","canvas2","canvas3"]

# Création du canevas pour afficher le graphique
def updategraph(n,mainapp):
    g=grph.graphs_gui(mainapp)
    g[0].plot(t, S, 'blue', label='S : population saine')
    g[0].plot(t, I1, 'cyan', label='I1 : nb infections')
    g[0].plot(t, R, 'white', label="R : nb retirés")
    g[1].fill_between(t,Ddaily,color="red", label = "morts ")
    g[2].fill_between(t,I3,color="yellow", label = "hospitalisés")
    newvalues(n)
    g[4].draw()
    g[5].draw()
    g[3].draw()
    t.append(n)