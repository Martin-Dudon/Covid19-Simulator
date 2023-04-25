import matplotlib.pyplot as plt

ε = 1/4.2 # taux de fin de latence
σ = 1 #taux d’apparition des symptomes
γ1 = 1/17 #taux de guérison des infections légeres
γ2 = 1/20 # taux de guérison des infections sévères
R0 = 2.5 #taux de reproduction de base
p = 0.9 #proportion des infections ne nécessitant pas l'hospitalisation
α = 0.00888 #taux de mortalité des cas sévères
c = 0 #fraction du R0 diminuée par les politiques de contrôle
b = 0.2 #diminution de la transmission par l'hospitalisation
ν = 0.000001

t = [0] #liste contenant les différentes valeurs de n
S = [0.94] #proportion de la population Saine
E1 = [0.01] #proportion de la population légerement infectée non infectieuse
E2 = [0.01] #proportion de la population gravement infectée non infectieuse
A1 = [0.01] #proportion de la population légerement infectée asymptomatique
A2 = [0.01] #proportion de la population gravement infectée asymptomatique
I1 = [0.01] #proportion de la population légerement infectée infectieuse
I2 = [0.01] #proportion de la population gravement infectée infectieuse
M = [0] #proportion de la population décédée
R1 = [0] #proportion de la population légerement infectée retirée
R2 = [0] #proportion de la population gravement infectée retirée
N = [1] #population totale au jours n rapportée à la population initiale

β = 10#R0/S[0]*γ1*σ*(α+γ2)/((γ1+p*σ)*(α+γ2)+b*γ1*σ*(1-p)) #taux de transmission


def newvalues(n):
    λ=(β*(A1[n]+I1[n]+A2[n])+β*I2[n])*(1-c) #force d'infection
    S.append(S[n]-λ*S[n])
    E1.append(E1[n]*p*λ*S[n]-ε*E1[n]+p*ν)
    A1.append(A1[n]+ε*E1[n]-σ*A1[n])
    I1.append(I1[n]+σ*A1[n]-γ1*I1[n])
    R1.append(R1[n]+γ1*I1[n])

    E2.append(E2[n]*(1-p)*λ*S[n]-ε*E2[n]+(1-p)*ν)
    A2.append(A2[n]+ε*E2[n]-σ*A2[n])
    I2.append(I2[n]+σ*A2[n]-(γ2+α)*I2[n])
    R2.append(R2[n]+γ2*I2[n])
    M.append(M[n]+α*I2[n])


E=[]
A=[]
I=[]
R=[]


def tracer():
    for n in range(100):
        E.append(E1[n]+E2[n])
        A.append(A1[n]+A2[n])
        I.append(I1[n]+I2[n])
        R.append(R1[n]+R2[n])
        newvalues(n)
        t.append(n+1)

    E.append(E1[100]+E2[100])
    A.append(A1[100]+A2[100])
    I.append(I1[100]+I2[100])
    R.append(R1[100]+R2[100])

    
    # Tracé des courbes
    plt.plot(t, S, 'r', label='S : proportion de population saine')
    plt.plot(t, E, 'g', label='E :proportion de population infectée non infectieuse')
    plt.plot(t, A, 'b', label='A :proportion de population infectée asymptomatique et infectieuse')
    plt.plot(t, I, 'pink', label='I :proportion de population infectée symptomatique infectieuse')
    plt.plot(t, R, 'y', label="R :proportion de population retirée parce qu'immunisée")
    plt.plot(t, M, 'm', label='N : population décédée')

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

tracer()