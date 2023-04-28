import matplotlib.pyplot as plt
import pandas as pd
import gui_components.banner as bn


"""
Le graphique montre le nombre attendu de personnes infectées, guéries, sensibles ou décédées au fil du temps. 
Les individus infectés passent d'abord par une phase d'exposition/incubation où ils sont asymptomatiques et non infectieux, 
puis passent à une phase symptomatique et d'infection classée selon l'état clinique de l'infection (légère, sévère ou critique). 
La taille de la population, la condition initiale et les valeurs des paramètres utilisés pour simuler la propagation de l'infection peuvent être modifiées. 

Nous utilisons un modèle épidémiologique compartimental, basé sur le modèle SEIR classique, pour décrire la propagation et la progression clinique de COVID-19. 
Il est important de suivre les différents résultats cliniques de l'infection, étant donné qu'ils nécessitent différents niveaux de ressources de soins de santé 
et qu'ils peuvent être testés et isolés à des rythmes différents. Les personnes sensibles (S) qui sont infectés commencent dans une classe exposée E où 
ils sont asymptomatiques et ne transmettent pas l'infection. Le taux de progression du stade exposé E au stade infecté I où l'individu est symptomatique et infectieux,
se produit au taux α1. Les descriptions cliniques des différents stades de l'infection sont présentées ci-dessous. 

Les personnes infectées commencent par une infection légère (I1), dont ils se remettent, au taux γ1 
ou évoluent vers une infection sévère (I2), au taux p1. 
L'infection sévère se résout au taux γ2 ou évolue vers un stade critique (I3) au taux p2. 

Les individus atteints d'une infection critique se rétablissent au taux γ3 et meurent au taux μ. 
Les individus rétablis sont suivis par la classe R et sont supposés être protégés de la réinfection à vie. 
Les individus peuvent transmettre l'infection à n'importe quel stade, mais à des taux différents. Le taux de transmission au stade i est décrit par βi
Le modèle inclut égalemnt la possibilité d'une infection asymptomatique. Après avoir quitté la classe E une fraction f des individus développe une infection asymptomatique 
(entre dans la classe I0), tandis que la fraction restante 1-f développe une infection symptomatique (entre dans la classe I1). 
L'infection asymptomatique n'évolue jamais vers des stades plus graves. Le taux de guérison d'une infection asymptomatique est de γ0
Les individus infectés de manière asymptomatique peuvent transmettre la maladie à d'autres personnes à un taux β0
Le modèle inclut également la possibilité que les individus exposés qui n'ont pas encore développé de symptômes puissent encore transmettre le virus ("transmission présymptomatique"). 
Pour modéliser cela, nous divisons la classe E en deux classes distinctes, E0 (pas de symptômes ni de transmission) et E1 (pas de symptômes mais possibilité de transmission). 
Le taux de sortie de la classe E0 est α0 et celui de E1 est α1.

"""
t = [0] #liste contenant les différentes valeurs de n
N = [70000000] # population initale
S = [N[0]-1] # population sensible (que la maladie n'a pas encore atteint)
E0 = [1] # pas encore de symptomes et non infectieux
E1 = [0] # pas encore de symptomes mais infectieux
I0 = [0] #infection asymptomatique 
I1 = [0] # infections peu sevères
I2 = [0] #  infections moyennement sevères
I3 = [0] # infections très sevères
I=[0] # total infections
D = [0] # nb morts
Ddaily = [0] # 
R = [0] # nb retirés
conta=[0]
testing =[0]

# On importe le fichier csv contenant les valeurs des différents paramètres
data = pd.read_csv("src/graphs/data.csv",sep=";")

# La fonction newvalues calcule les valeurs au jour n

def newvalues(n):
    if bn.restart == "finish":
        for lst in [S, E0, E1, I0, I1, I2, I3, I, D, Ddaily, R, conta, testing,t]:
            lst.clear()
            if lst==E0:
                lst.append(1)
            elif lst == S:
                lst.append(N[0]-1)
            else :
                lst.append(0)
    βe,β0,β1,β2,β3,α0,α1,f,γ0,γ1,γ2,γ3,p1,p2,μ,test=data["val"].astype(float)
    S.append(S[n]-(βe*E1[n]+β0*I0[n]+β1*I1[n]+β2*I2[n]+β3*I3[n])*S[n])
    E0.append(E0[n]+(βe*E1[n]+β0*I0[n]+β1*I1[n]+β2*I2[n]+β3*I3[n])*S[n]-α0*E0[n])
    E1.append(E1[n]+α0*E0[n]-α1*E1[n])
    I0.append(I0[n]+f*α1*E1[n]-(γ0*I0[n]))
    I1.append(I1[n]+(1-f)*α1*E1[n]-(γ1+p1)*I1[n])
    I2.append(I2[n]+p1*I1[n]-(γ2+p2)*I2[n])
    I3.append(I3[n]+p2*I2[n]-(γ3+μ)*I3[n])
    I.append(I0[n]+I1[n]+I2[n]+I3[n]+E1[n]+E0[n])
    D.append(D[n]+μ*I3[n])
    Ddaily.append(μ*I3[n])
    R.append(R[n]+γ0*I0[n]+γ1*I1[n]+γ2*I2[n]+γ3*I3[n])
    conta.append(I0[n]+I1[n]+I2[n]+I3[n]+E1[n])
    testing.append(test)

# La fonction tracer ne servira pas dans le programme définitif, elle sert uniquement à tester le modèle SEIR 
# en réalisant un graphique matplotlib

def tracer():

    for n in range(300):
        newvalues(n)
        t.append(n+1)

    # Tracé des courbes
    plt.plot(t, S, 'r', label='S : population sensible')
    plt.plot(t, E0, 'cyan', label='E0 : pas encore de symptomes et non infectieux')
    plt.plot(t, E1, 'grey', label='E1 : pas encore de symptomes mais infectieux')
    plt.plot(t, I, 'purple', label='I : total des infections')
    plt.plot(t, I0, 'g', label='I0 : infection asymptomatique ')
    plt.plot(t, I1, 'b', label='I1 : infections peu sevères')
    plt.plot(t, I2, 'black', label='I2 : infections moyennement sevères')
    plt.plot(t, I3, 'pink', label='I3 : infections très sevères')
    plt.plot(t, R, 'y', label="R : retirés")
    plt.plot(t, D, 'm', label='D : population décédée')

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

#tracer()