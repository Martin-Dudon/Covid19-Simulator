import tkinter as tk
import gui_components.actions as a
from graphs.SEIR_model import newvalues,I,I0,I2,I3,D,R,conta,testing

"""Cette fonction crée les cases contenant les statistiques"""

def stats(mainapp,l):
    #Création du bandeau supérieur
    stframe = tk.Frame(mainapp, background="#303030",width=1,height=1)
    stframe.grid(row=1,column=0, columnspan=2)

    # Création de la case affichant le nombre de cas
    cas = tk.Frame(stframe)
    cas.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    cas.grid(row=0, column=0,padx=0.009*l, pady=(0,0.009*l))
    
    # Création de la case affichant le nombre de contagieux
    contagieux = tk.Frame(stframe)
    contagieux.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    contagieux.grid(row=0, column=1,pady=(0,0.009*l))

    #Création de la case affichant le nombre de guerisons
    guerisons = tk.Frame(stframe)
    guerisons.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    guerisons.grid(row=0, column=2,padx=(0.009*l), pady=(0,0.009*l))

    #Création de la case affichant le nombre d'hospitalisés
    hospitalisés = tk.Frame(stframe)
    hospitalisés.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    hospitalisés.grid(row=0, column=3,pady=(0,0.009*l))  

    #Création de la case affichant le nombre de personnes en réanimation
    rea = tk.Frame(stframe)  
    rea.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    rea.grid(row=0, column=4,padx=(0.009*l), pady=(0,0.009*l))

    #Création de la case affichant le nombre de personnes décedés
    deces = tk.Frame(stframe)
    deces.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    deces.grid(row=0, column=5, pady=(0,0.009*l))

    #Création de la case affichant le nombre d'assymptomatiques
    assymptomatiques = tk.Frame(stframe)
    assymptomatiques.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    assymptomatiques.grid(row=0, column=6,padx=(0.009*l), pady=(0,0.009*l))

    #Création de la case affichant le nombre de tests par jour
    tests = tk.Frame(stframe)
    tests.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")    
    tests.grid(row=0, column=7,padx=(0,0.009*l), pady=(0,0.009*l))

    return [cas, contagieux, guerisons, hospitalisés, rea, deces, assymptomatiques, tests,stframe]

"""Cette fonction mets a jour les statistiques"""

def updatestats(n,l,U):
    total_cas = tk.Label(U[0], text="Total des Cas", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="blue")
    total_cas.grid(row=0, column=0,padx=0.0195*l)
    total_casnb = tk.Label(U[0], text=str(int(I[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"),width=int(0.01*l), fg="blue",)
    total_casnb.grid(row=1, column=0)
    jr_cas = tk.Label(U[0],text=f"{int(I[n+1]-I[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="blue")
    jr_cas.grid(row=2, column=0, pady=(0,0.006*l))

    total_conta = tk.Label(U[1],text="Contagieux", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="grey")
    total_conta.grid(row=0, column=0,padx=0.0195*l)
    total_contanb = tk.Label(U[1], text=str(int(conta[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"),width=int(0.01*l), fg="grey")
    total_contanb.grid(row=1, column=0)
    jr_conta = tk.Label(U[1],text=f"{int(conta[n+1]-conta[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="grey")
    jr_conta.grid(row=2, column=0, pady=(0,0.006*l))

    total_gueri = tk.Label(U[2], text="Immunisés", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="white")
    total_gueri.grid(row=0, column=0,padx=0.0195*l)
    total_guerinb = tk.Label(U[2], text=str(int(R[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"),width=int(0.01*l), fg="white")
    total_guerinb.grid(row=1, column=0)
    jr_gueri = tk.Label(U[2],text=f"{int(R[n+1]-R[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="white")
    jr_gueri.grid(row=2, column=0, pady=(0,0.006*l))

    total_hos= tk.Label(U[3], text="Hospitalisés", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="yellow")
    total_hos.grid(row=0, column=0,padx=0.0195*l)
    total_hosnb = tk.Label(U[3], text=str(int(I2[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"),width=int(0.01*l), fg="yellow")
    total_hosnb.grid(row=1, column=0)
    jr_hos = tk.Label(U[3],text=f"{int(I2[n+1]-I2[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="yellow")
    jr_hos.grid(row=2, column=0, pady=(0,0.006*l))

    total_rea= tk.Label(U[4], text="Réanimation", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="orange")
    total_rea.grid(row=0, column=0,padx=0.0195*l)
    total_reanb = tk.Label(U[4], text=str(int(I3[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"),width=int(0.01*l), fg="orange")
    total_reanb.grid(row=1, column=0)
    jr_rea = tk.Label(U[4],text=f"{int(I3[n+1]-I3[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="orange")
    jr_rea.grid(row=2, column=0, pady=(0,0.006*l))

    total_dc= tk.Label(U[5], text="Décès", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="red")
    total_dc.grid(row=0, column=0,padx=0.0195*l)
    total_dcnb = tk.Label(U[5], text=str(int(D[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"),width=int(0.01*l), fg="red")
    total_dcnb.grid(row=1, column=0)
    jr_dc = tk.Label(U[5],text=f"{int(D[n+1]-D[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="red")
    jr_dc.grid(row=2, column=0, pady=(0,0.006*l))

    total_assy= tk.Label(U[6], text="Asymptomatiques", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.014*l), fg="#2FC1DE")
    total_assy.grid(row=0, column=0,padx=0.005*l)
    total_assynb = tk.Label(U[6], text=str(int(I0[n])), bg="#202020", font=("Helvetica Neue",int(0.015*l),"bold"),width=int(0.01*l), fg="#2FC1DE")
    total_assynb.grid(row=1, column=0)
    jr_assy = tk.Label(U[6],  text=f"{int(I0[n+1]-I0[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="#2FC1DE")
    jr_assy.grid(row=2, column=0, pady=(0,0.006*l))

    total_test= tk.Label(U[7], text="Tests", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="purple")
    total_test.grid(row=0, column=0,padx=0.0195*l)
    total_testnb = tk.Label(U[7], text=str(int(sum(testing))), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"),width=int(0.01*l), fg="purple")
    total_testnb.grid(row=1, column=0)
    jr_test = tk.Label(U[7],  text=f"{int(testing[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"),width=int(0.01*l), fg="purple")
    jr_test.grid(row=2, column=0, pady=(0,0.006*l))

