import tkinter as tk 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graphs_gui(mainapp):

    # Création du cadre de graphiques
    grframe = tk.Frame(mainapp, background="white",width=60, height=2)
    grframe.grid(row=3,column=0)
    # Création du graphique 1
    fig = plt.Figure(figsize=(10, 3.5), dpi=125)
    fig.set_facecolor('#202020')
    ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom = 0.15,left=0.1, right=0.95)
    canvas = FigureCanvasTkAgg(fig, master=grframe)
    canvas.get_tk_widget().grid(row=0, column=0,columnspan=2, padx=10, pady=10,sticky="ns")
    ax.set_facecolor('#202020')
    ax.set_xlim([0, 300])
    formatter = ticker.FuncFormatter(lambda y, pos: '{:.0f}M'.format(y/1000000))
    ax.yaxis.set_major_formatter(formatter)
    ax.grid(True, color='white', linewidth=0.5, linestyle='--')
    ax.spines[['top', 'left', 'right', 'bottom']].set_color('white')
    ax.tick_params(axis='both', colors='white')

    # Création du graphique 2

    fig2 = plt.Figure(figsize=(5, 3), dpi=125)
    fig2.set_facecolor('#202020')
    ax2 = fig2.add_subplot(111)
    fig2.subplots_adjust(bottom = 0.15,left=0.08, right=0.95)
    canvas2 = FigureCanvasTkAgg(fig2, master=grframe)
    canvas2.get_tk_widget().grid(row=2, column=0, padx=7)
    ax2.set_facecolor('#202020')
    ax2.set_xlim([0, 300])
    ax2.set_ylim([-1000, 30000])
    formatter = ticker.FuncFormatter(lambda y, pos: '{:.0f}k'.format(y/1000))
    ax2.yaxis.set_major_formatter(formatter)
    ax2.grid(True, color='white', linewidth=0.5, linestyle='--')
    ax2.spines[['top', 'left', 'right', 'bottom']].set_color('white')
    ax2.tick_params(axis='both', colors='white')

    # Création du graphique 3

    fig3 = plt.Figure(figsize=(5, 3), dpi=125)
    fig3.set_facecolor('#202020')
    ax3 = fig3.add_subplot(111)
    fig3.subplots_adjust(bottom = 0.15, left=0.08, right=0.95)
    canvas3 = FigureCanvasTkAgg(fig3, master=grframe)
    canvas3.get_tk_widget().grid(row=2, column=1)
    ax3.set_facecolor('#202020')
    ax3.set_xlim([0, 300])
    ax3.set_ylim([-25000, 510000])
    formatter = ticker.FuncFormatter(lambda y, pos: '{:.0f}k'.format(y/1000))
    ax3.yaxis.set_major_formatter(formatter)
    ax3.grid(True, color='white', linewidth=0.5, linestyle='--')
    ax3.spines[['top', 'left', 'right', 'bottom']].set_color('white')
    ax3.tick_params(axis='both', colors='white')

    return [ax, ax2, ax3, canvas, canvas2, canvas3]