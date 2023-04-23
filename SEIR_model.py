import matplotlib.pyplot as plt

beta= 0.8 
alpha= 0.75
gamma= 0.05
nu= 0.009
micro= 0.01


t = [i for i in range(101)]

S = [0.6]
E = [0.1]
I = [0.4]
R= [0]
N= [1.1]

def newvalues(S, E, I, R, N):
    S.append(S[n]-beta*S[n]*I[n]+nu*N[n]-micro*S[n])
    E.append(E[n]+beta*S[n]*I[n]-alpha*E[n]-micro*E[n])
    I.append(I[n]+alpha*E[n]-gamma*I[n]-micro*I[n])
    R.append(R[n]+gamma*I[n]-micro*R[n])
    N.append(S[n+1]+E[n+1]+I[n+1]+R[n+1])
    return S, E, I, R, N

for n in range(100):
    newvalues(S,E,I,R,N)

# Tracé des courbes
plt.plot(t, S, 'r', label='S : proportion de population saine')
plt.plot(t, E, 'g', label='E :proportion de population infectée non infectieuse')
plt.plot(t, I, 'b', label='I :proportion de population infectée et infectieuse')
plt.plot(t, R, 'y', label="R :proportion de population retirée parce qu'immunisée")
plt.plot(t, N, 'm', label='N : population rapportée à la population initiale')

# Configuration de l'axe des ordonnées
plt.ylim(0, 1.1)
plt.ylabel('population')

# Configuration de l'axe des abscisses
plt.xlim(0, 100)
plt.xlabel('temps')

# Ajout d'une légende pour les courbes
plt.legend()

# Affichage du graphique
plt.show()