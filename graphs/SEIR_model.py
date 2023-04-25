import matplotlib.pyplot as plt
import pandas as pd

α = 0.2 #rythme de passage de E à I1
γ1 = 0.133 #rythme de guerison des infections peu sevères
γ2 = 0.125 #rythme de guerison des infections moyennement sevères
γ3 = 0.125 #rythme de guerison des infections très sevères
p1 = 0.033 #taux de passage de I1 à I2
p2 = 0.042 #taux de passage de I2 à I3
μ = 0.05 #taux de passage de I3 à M

t = [0] #liste contenant les différentes valeurs de n
N = [70000000]
S = [N[0]-1] # population saine
E = [1] # nb infectés non infectieux
I1 = [0] # nb infections peu sevères
I2 = [0] #  nb infections moyennement sevères
I3 = [0] # nb infections très sevères
I=[0]
D = [0] #nb morts
Ddaily = [0]
R = [0] #nb retirés

# Taux de transmission à partir de I1, I2, I3
β1 = 0.5/N[0]
β2 = 0.1/N[0]
β3 = 0.1/N[0]

def newvalues(n):
    #data = pd.read_csv("data/data.csv")
    #α,γ1,γ2,γ3,p1,p2,μ=data[data.nom=='α']["valeur"],data[data.nom=='γ1']["valeur"],data[data.nom=='γ2']["valeur"],data[data.nom=='γ3']["valeur"],data[data.nom=='p1']["valeur"],data[data.nom=='p2']["valeur"],data[data.nom=='μ']["valeur"]
    S.append(S[n]-(β1*I1[n]+β2*I2[n]+β3*I3[n])*S[n])
    E.append(E[n]+(β1*I1[n]+β2*I2[n]+β3*I3[n])*S[n]-α*E[n])
    I1.append(I1[n]+α*E[n]-(γ1+p1)*I1[n])
    I2.append(I2[n]+p1*I1[n]-(γ2+p2)*I2[n])
    I3.append(I3[n]+p2*I2[n]-(γ3+μ)*I3[n])
    I.append(I1[n]+I2[n]+I3[n])
    D.append(D[n]+μ*I3[n])
    Ddaily.append(μ*I3[n])
    R.append(R[n]+γ1*I1[n]+γ2*I2[n]+γ3*I3[n])

def tracer():

    for n in range(300):
        newvalues(n)
        t.append(n+1)

    # Tracé des courbes
    plt.plot(t, S, 'r', label='S : population saine')
    plt.plot(t, E, 'g', label='E : nb infectés non infectieux')
    plt.plot(t, I1, 'b', label='I1 : nb infections peu sevères')
    plt.plot(t, I2, 'black', label='I2 : nb infections moyennement sevères')
    plt.plot(t, I3, 'pink', label='I3 :nb infections très sevères')
    plt.plot(t, R, 'y', label="R : nb retirés")
    plt.plot(t, D, 'm', label='N : population décédée')

    # Configuration de l'axe des ordonnées
    plt.ylim(0, 70000000)
    plt.ylabel('population')

    # Configuration de l'axe des abscisses
    plt.xlim(0, 300)
    plt.xlabel('temps')

    # Ajout d'une légende pour les courbes
    plt.legend()

    # Affichage du graphique
    plt.show()

tracer()