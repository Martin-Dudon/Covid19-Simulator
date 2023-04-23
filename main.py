import pygame
import threading
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

pygame.init()

# Obtenir les informations sur l'écran
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Créer une fenêtre Pygame à la taille de l'écran
WINDOW_SIZE=(screen_width, screen_height)
screen = pygame.display.set_mode(WINDOW_SIZE)

beta= 0.8
alpha= 0.75
gamma= 0.05
nu= 0.009
micro= 0.01

t = [0]
n=0
S = [0.999]
E = [0]
I = [0.001]
R= [0]
N= [1]

def newvalues(S, E, I, R, N,n):
    S.append(S[n]-beta*S[n]*I[n]+nu*N[n]-micro*S[n])
    E.append(E[n]+beta*S[n]*I[n]-alpha*E[n]-micro*E[n])
    I.append(I[n]+alpha*E[n]-gamma*I[n]-micro*I[n])
    R.append(R[n]+gamma*I[n]-micro*R[n])
    N.append(S[n+1]+E[n+1]+I[n+1]+R[n+1])
    return S, E, I, R, N

fig, ax = plt.subplots()

plt.ylim(0, 1.1)
plt.ylabel('population')

# Configuration de l'axe des abscisses
plt.xlim(0, 100)
plt.xlabel('temps')

# Fonction pour mettre à jour le graphique
def update_graph(n):
    # Décalage de la courbe vers la gauche
    newvalues(S,E,I,R,N,n)
    
    # Mise à jour de la courbe
    ax.plot(t, S, 'r', label='S : proportion de population saine')
    ax.plot(t, E, 'g', label='E :proportion de population infectée non infectieuse')
    ax.plot(t, I, 'b', label='I :proportion de population infectée et infectieuse')
    ax.plot(t, R, 'y', label="R :proportion de population retirée parce qu'immunisée")
    ax.plot(t, N, 'm', label='N : population rapportée à la population initiale')
    
    # Mise à jour du graphique
    canvas.draw()
    
    # Conversion du graphique en image Pygame
    graph_image = pygame.image.fromstring(canvas.tostring_rgb(), canvas.get_width_height(), "RGB")
    
    # Affichage de l'image Pygame sur la fenêtre
    screen.blit(graph_image, (0, 0))
    
    # Rafraîchissement de la fenêtre
    pygame.display.flip()

canvas = FigureCanvas(fig)

# Boucle principale de l'application Pygame
running = True
while running:
    # Gestion des événements Pygame
    t.append(n)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
    update_graph(n)
    time.sleep(2)
    # Incrémentation du compteur de frames
    n+=1
    
