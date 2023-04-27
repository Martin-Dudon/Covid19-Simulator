from graphs.SEIR_model import newvalues, t, S, E1, I, I1, I2, I3, Ddaily, R

g=["ax","ax2","ax3","canvas","canvas2","canvas3"]

# Création du canevas pour afficher le graphique
def updategraph(n,mainapp,l,h,g):
    g[0].plot(t, S, 'blue', label='S : population saine')
    g[0].plot(t, I1, 'cyan', label='I1 : nb infections')
    g[0].plot(t, R, 'white', label="R : nb retirés")
    if not g[0].legend_:
        g[0].legend(fontsize="5",facecolor='#303030',labelcolor="white")
    g[1].fill_between(t,Ddaily,color="red", label = "morts ")
    if not g[1].legend_:
        g[1].legend(fontsize="7",facecolor='#303030',labelcolor="white")
    g[2].fill_between(t,I3,color="yellow", label = "hospitalisés")
    if not g[2].legend_:
        g[2].legend(fontsize="7",facecolor='#303030',labelcolor="white")
    g[2].fill_between(t,I3,color="yellow", label = "hospitalisés")
    newvalues(n)
    g[4].draw()
    g[5].draw()
    g[3].draw()
    t.append(n)