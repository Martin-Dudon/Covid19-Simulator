import tkinter as tk
import gui_components.actions as a
from graphs.SEIR_model import newvalues, t, S, E0,E1, I, I0,I1, I2, I3, D, R,conta,testing

def stats(n,mainapp,l):
    #Création du bandeau supérieur
    stframe = tk.Frame(mainapp, background="#303030")
    stframe.grid(row=1,column=0, columnspan=2, sticky="ew")

    ######################################################################################################      
    cas = tk.Frame(stframe)
    cas.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    cas.grid(row=0, column=0,padx=0.009*l, pady=(0,0.009*l))
    
    total_cas = tk.Label(cas, text="Total des Cas", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="#F6C82B")
    total_cas.grid(row=0, column=0,padx=0.0195*l)
    total_casnb = tk.Label(cas, text=str(int(I[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"), fg="#F6C82B")
    total_casnb.grid(row=1, column=0)
    jr_cas = tk.Label(cas,text=f"{int(I[n+1]-I[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="#F6C82B")
    jr_cas.grid(row=2, column=0, pady=(0,0.006*l))
    
    ###################################################################################################### 
    contagieux = tk.Frame(stframe)
    contagieux.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    contagieux.grid(row=0, column=1,pady=(0,0.009*l))

    total_conta = tk.Label(contagieux,text=" Contagieux ", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="grey")
    total_conta.grid(row=0, column=0,padx=0.0195*l)
    total_contanb = tk.Label(contagieux, text=str(int(conta[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"), fg="grey")
    total_contanb.grid(row=1, column=0)
    jr_conta = tk.Label(contagieux,text=f"{int(conta[n+1]-conta[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="grey")
    jr_conta.grid(row=2, column=0, pady=(0,0.006*l))
    
    ###################################################################################################### 
    guerisons = tk.Frame(stframe)
    guerisons.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    guerisons.grid(row=0, column=2,padx=(0.009*l), pady=(0,0.009*l))

    total_gueri = tk.Label(guerisons, text=" Immunisés ", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="green")
    total_gueri.grid(row=0, column=0,padx=0.0195*l)
    total_guerinb = tk.Label(guerisons, text=str(int(R[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"), fg="green")
    total_guerinb.grid(row=1, column=0)
    jr_gueri = tk.Label(guerisons,text=f"{int(R[n+1]-R[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="green")
    jr_gueri.grid(row=2, column=0, pady=(0,0.006*l))

    ###################################################################################################### 
    hospitalisés = tk.Frame(stframe)
    hospitalisés.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    hospitalisés.grid(row=0, column=3,pady=(0,0.009*l))  

    total_hos= tk.Label(hospitalisés, text="Hospitalisés", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="orange")
    total_hos.grid(row=0, column=0,padx=0.0195*l)
    total_hosnb = tk.Label(hospitalisés, text=str(int(I2[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"), fg="orange")
    total_hosnb.grid(row=1, column=0)
    jr_hos = tk.Label(hospitalisés,text=f"{int(I2[n+1]-I2[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="orange")
    jr_hos.grid(row=2, column=0, pady=(0,0.006*l))

    ###################################################################################################### 
    rea = tk.Frame(stframe)  
    rea.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    rea.grid(row=0, column=4,padx=(0.009*l), pady=(0,0.009*l))

    total_rea= tk.Label(rea, text="Réanimation", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="red")
    total_rea.grid(row=0, column=0,padx=0.0195*l)
    total_reanb = tk.Label(rea, text=str(int(I3[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"), fg="red")
    total_reanb.grid(row=1, column=0)
    jr_rea = tk.Label(rea,text=f"{int(I3[n+1]-I3[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="red")
    jr_rea.grid(row=2, column=0, pady=(0,0.006*l))

    ###################################################################################################### 
    deces = tk.Frame(stframe)
    deces.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    deces.grid(row=0, column=5, pady=(0,0.009*l))

    total_dc= tk.Label(deces, text="    Décès    ", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="black")
    total_dc.grid(row=0, column=0,padx=0.0195*l)
    total_dcnb = tk.Label(deces, text=str(int(D[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"), fg="black")
    total_dcnb.grid(row=1, column=0)
    jr_dc = tk.Label(deces,text=f"{int(D[n+1]-D[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="black")
    jr_dc.grid(row=2, column=0, pady=(0,0.006*l))

    ###################################################################################################### 
    assymptomatiques = tk.Frame(stframe)
    assymptomatiques.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")
    assymptomatiques.grid(row=0, column=6,padx=(0.009*l), pady=(0,0.009*l))

    total_assy= tk.Label(assymptomatiques, text="Asymptomatiques", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="#2FC1DE")
    total_assy.grid(row=0, column=0,padx=0.005*l)
    total_assynb = tk.Label(assymptomatiques, text=str(int(I0[n])), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"), fg="#2FC1DE")
    total_assynb.grid(row=1, column=0)
    jr_assy = tk.Label(assymptomatiques,  text=f"{int(I0[n+1]-I0[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="#2FC1DE")
    jr_assy.grid(row=2, column=0, pady=(0,0.006*l))

    ###################################################################################################### 
    tests = tk.Frame(stframe)
    tests.configure(highlightbackground="black", highlightthickness=1, highlightcolor="black", bg="#202020")    
    tests.grid(row=0, column=7,padx=(0,0.009*l), pady=(0,0.009*l))

    total_test= tk.Label(tests, text="     Tests     ", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="purple")
    total_test.grid(row=0, column=0,padx=0.0195*l)
    total_testnb = tk.Label(tests, text=str(int(sum(testing))), bg="#202020", font=("Helvetica Neue",int(0.016*l),"bold"), fg="purple")
    total_testnb.grid(row=1, column=0)
    jr_test = tk.Label(tests,  text=f"{int(testing[n])} /jrs", bg="#202020", font=("Helvetica Neue", int(0.013*l),"bold"), fg="purple")
    jr_test.grid(row=2, column=0, pady=(0,0.006*l))