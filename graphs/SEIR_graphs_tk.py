import tkinter as tk 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graphs_gui(mainapp,l,h):

    # Création du cadre de graphiques
    grframe = tk.Frame(mainapp)
    grframe.configure(bg="#303030")
    grframe.grid(row=3,column=0, padx=(0.009*l,0),sticky="nsew")
    
    # Création du graphique 1
    fig = plt.Figure(figsize=(6.35, 2), dpi=125)
    #fig.set_size_inches(7.75, 3)
    fig.set_facecolor('#202020')
    ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom = 0.2,left=0.09, right=0.95, top=0.9)
    canvas = FigureCanvasTkAgg(fig, master=grframe)
    canvas.get_tk_widget().configure(highlightbackground="black", highlightthickness=1, highlightcolor="black")
    canvas.get_tk_widget().grid(row=0, column=0,columnspan=2,sticky="nsew")
    ax.set_facecolor('#202020')
    ax.set_xlim([0, 400])
    formatter = ticker.FuncFormatter(lambda y, pos: '{:.0f}M'.format(y/1000000))
    ax.yaxis.set_major_formatter(formatter)
    ax.grid(True, color='white', linewidth=0.5, linestyle='--')
    ax.spines[['top', 'left', 'right', 'bottom']].set_color('white')
    ax.tick_params(axis='both', colors='white')

    # Création du graphique 2

    fig2 = plt.Figure()
    fig2.set_size_inches(l/450, h/325)
    fig2.set_facecolor('#202020')
    ax2 = fig2.add_subplot(111)
    #fig.subplots_adjust(bottom = 0.000055*l,left=0.000035*l, right=1-0.00002*l, top=1-0.00004*l)
    canvas2 = FigureCanvasTkAgg(fig2, master=grframe)
    canvas2.get_tk_widget().configure(highlightbackground="black", highlightthickness=1, highlightcolor="black")
    canvas2.get_tk_widget().grid(row=2, column=0, pady=0.009*l,sticky="nsew")
    ax2.set_facecolor('#202020')
    ax2.set_xlim([0, 300])
    ax2.set_ylim([-2500, 70000])
    formatter = ticker.FuncFormatter(lambda y, pos: '{:.0f}k'.format(y/1000))
    ax2.yaxis.set_major_formatter(formatter)
    ax2.grid(True, color='white', linewidth=0.5, linestyle='--')
    ax2.spines[['top', 'left', 'right', 'bottom']].set_color('white')
    ax2.tick_params(axis='both', colors='white')

    # Création du graphique 3

    fig3 = plt.Figure()
    fig3.set_size_inches(l/450, h/325)
    fig3.set_facecolor('#202020')
    ax3 = fig3.add_subplot(111)
    #fig.subplots_adjust(bottom = 0.000055*l,left=0.000035*l, right=1-0.00002*l, top=1-0.00004*l)
    canvas3 = FigureCanvasTkAgg(fig3, master=grframe)
    canvas3.get_tk_widget().configure(highlightbackground="black", highlightthickness=1, highlightcolor="black")
    canvas3.get_tk_widget().grid(row=2, column=1,pady=0.009*l,padx=(10,0),sticky="nsew")
    ax3.set_facecolor('#202020')
    ax3.set_xlim([0, 300])
    ax3.set_ylim([-25000, 700000])
    formatter = ticker.FuncFormatter(lambda y, pos: '{:.0f}k'.format(y/1000))
    ax3.yaxis.set_major_formatter(formatter)
    ax3.grid(True, color='white', linewidth=0.5, linestyle='--')
    ax3.spines[['top', 'left', 'right', 'bottom']].set_color('white')
    ax3.tick_params(axis='both', colors='white')

    return [ax, ax2, ax3, canvas, canvas2, canvas3]