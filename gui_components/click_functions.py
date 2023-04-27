
lecture=True
redem=False
sp=1

def play():
    global lecture
    lecture=True

def pause():
    global lecture
    lecture=False

def speed():
    global sp
    sp+=1

def restart():
    global redem
    redem=True

