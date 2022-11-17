from tkinter import *
import random

#windows, buttons, labels
m=0
m1=0
m2=0
m3=0
m4=0
mt=0
title=0

w=0
p1dcards=0
p2dcards=0
udcard=0
zone=0
lt0=0
lt1=0
lt2=0
lt3=0
fturnb=0
cancelb=0

vs=0
wl=0
w1im=0
vb1=0
vb2=0
vp=0

rs=0
rules=0
rs1=0
rsb1=0

#game
cards=['tiger','dragon','frog','rabbit','crab','elephant','goose','rooster','monkey','mantis','horse','ox','crane','boar','eel','cobra']
tigerm=[[1,0],[-2,0]]
dragonm=[[-1,-2],[-1,2],[1,-1],[1,1]]
frogm=[[-1,-1],[0,-2],[1,1]]
rabbitm=[[1,-1],[-1,1],[0,2]]
crabm=[[0,-2],[0,2],[-1,0]]
elephantm=[[0,-1],[-1,-1],[0,1],[-1,1]]
goosem=[[0,-1],[-1,-1],[0,1],[1,1]]
roosterm=[[0,-1],[1,-1],[0,1],[-1,1]]
monkeym=[[-1,-1],[-1,1],[1,-1],[1,1]]
mantism=[[1,0],[-1,-1],[-1,1]]
horsem=[[-1,0],[0,-1],[1,0]]
oxm=[[-1,0],[0,1],[1,0]]
cranem=[[-1,0],[1,-1],[1,1]]
boarm=[[0,-1],[0,1],[-1,0]]
eelm=[[-1,-1],[0,1],[1,-1]]
cobram=[[-1,1],[0,-1],[1,1]]
movements=[tigerm,dragonm,frogm,rabbitm,crabm,elephantm,goosem,roosterm,monkeym,mantism,horsem,oxm,cranem,boarm,eelm,cobram]

p1cards=0
p2cards=0
ucard=0
selcard=0
selcardp=0

selfig=0

turn=1

winner=0

botplay=0

#positions
p2p1=[0,0]
p2p2=[0,1]
p2p3=[0,3]
p2p4=[0,4]
p2k=[0,2]
p1p1=[4,0]
p1p2=[4,1]
p1p3=[4,3]
p1p4=[4,4]
p1k=[4,2]
board=0
figp=0
figpx=0
figpy=0

#pictures
king1=0
king2=0
pawn1=0
pawn2=0
empty=0
king1p=0
king2p=0
pawn1p=0
pawn2p=0
emptyp=0

tiger=0
dragon=0
frog=0
rabbit=0
crab=0
elephant=0
goose=0
rooster=0
monkey=0
mantis=0
horse=0
ox=0
crane=0
boar=0
eel=0
cobra=0

#checks
chcards=['tiger','dragon','frog','rabbit','crab','elephant','goose','rooster','monkey','mantis','horse','ox','crane','boar','eel','cobra']
phase=0

def resetvals():
    global w
    global p1dcards
    global p2dcards
    global udcard
    global zone
    global lt0
    global lt1
    global lt2
    global lt3
    global fturnb
    global cancelb
    global cards
    global movements
    global p1cards
    global p2cards
    global ucard
    global selcard
    global selcardp
    global selfig
    global turn
    global winner
    global p2p1
    global p2p2
    global p2p3
    global p2p4
    global p2k
    global p1p1
    global p1p2
    global p1p3
    global p1p4
    global p1k
    global board
    global figp
    global figpx
    global figpy
    global chcards
    global phase
    
    w=0
    p1dcards=0
    p2dcards=0
    udcard=0
    zone=0
    lt1=0
    lt2=0
    lt3=0
    fturnb=0
    cancelb=0

    cards=['tiger','dragon','frog','rabbit','crab','elephant','goose','rooster','monkey','mantis','horse','ox','crane','boar','eel','cobra']
    movements=[tigerm,dragonm,frogm,rabbitm,crabm,elephantm,goosem,roosterm,monkeym,mantism,horsem,oxm,cranem,boarm,eelm,cobram]

    p1cards=0
    p2cards=0
    ucard=0
    selcard=0
    selcardp=0

    selfig=0

    turn=1

    winner=0

    p2p1=[0,0]
    p2p2=[0,1]
    p2p3=[0,3]
    p2p4=[0,4]
    p2k=[0,2]
    p1p1=[4,0]
    p1p2=[4,1]
    p1p3=[4,3]
    p1p4=[4,4]
    p1k=[4,2]
    board=0
    figp=0
    figpx=0
    figpy=0

    chcards=['tiger','dragon','frog','rabbit','crab','elephant','goose','rooster','monkey','mantis','horse','ox','crane','boar','eel','cobra']
    phase=0
    

def boardclearing():
    global board
    for i in range(5):
        for j in range(5):
            
            if board[i][j]==',':
                board[i][j]='*'
            elif board[i][j].endswith(','):
                board[i][j]=board[i][j][0:-1]
            elif board[i][j].endswith('.'):
                board[i][j]=board[i][j][0:-1]

def supdate():
    global lt0
    global king1
    global king2
    global pawn1
    global pawn2
    global empty
    global king1p
    global king2p
    global pawn1p
    global pawn2p
    global emptyp
    global board
    global tiger
    global dragon
    global frog
    global rabbit
    global crab
    global elephant
    global goose
    global rooster
    global monkey
    global mantis
    global horse
    global ox
    global crane
    global boar
    global eel
    global cobra
    global chcards
    global p1cards
    global p2cards
    global ucard
    global p1dcards
    global p2dcards
    global udcard
    global phase
    global fturnb
    global turn

    king1=PhotoImage(file="king1.png")
    king2=PhotoImage(file="king2.png")
    pawn1=PhotoImage(file="pawn1.png")
    pawn2=PhotoImage(file="pawn2.png")
    empty=PhotoImage(file="empty.png")

    king1p=PhotoImage(file="king1p.png")
    king2p=PhotoImage(file="king2p.png")
    pawn1p=PhotoImage(file="pawn1p.png")
    pawn2p=PhotoImage(file="pawn2p.png")
    emptyp=PhotoImage(file="emptyp.png")

    tiger=PhotoImage(file="mtiger.png")
    dragon=PhotoImage(file="mdragon.png")
    frog=PhotoImage(file="mfrog.png")
    rabbit=PhotoImage(file="mrabbit.png")
    crab=PhotoImage(file="mcrab.png")
    elephant=PhotoImage(file="melephant.png")
    goose=PhotoImage(file="mgoose.png")
    rooster=PhotoImage(file="mrooster.png")
    monkey=PhotoImage(file="mmonkey.png")
    mantis=PhotoImage(file="mmantis.png")
    horse=PhotoImage(file="mhorse.png")
    ox=PhotoImage(file="mox.png")
    crane=PhotoImage(file="mcrane.png")
    boar=PhotoImage(file="mboar.png")
    eel=PhotoImage(file="meel.png")
    cobra=PhotoImage(file="mcobra.png")

    plist=[tiger,dragon,frog,rabbit,crab,elephant,goose,rooster,monkey,mantis,horse,ox,crane,boar,eel,cobra]
    
    for i in range(5):
        for j in range(5):
            
            if board[i][j]=='*':
                zone[i][j].config(image=empty,bg='#EFE4B0')

            elif board[i][j]==',':
                zone[i][j].config(image=emptyp,bg='#DCC450')

            elif board[i][j].endswith('.') or board[i][j].endswith(','):
                if board[i][j].startswith('p1'):
                    if board[i][j].startswith('p1k'):
                        zone[i][j].config(image=king1p,bg='#DCC450')
                    else:
                        zone[i][j].config(image=pawn1p,bg='#DCC450')
                        
                else:
                    if board[i][j].startswith('p2k'):
                        zone[i][j].config(image=king2p,bg='#DCC450')
                    else:
                        zone[i][j].config(image=pawn2p,bg='#DCC450')

            else:
                if board[i][j].startswith('p1'):
                    if board[i][j].startswith('p1k'):
                        if phase==1 and turn==1:
                            zone[i][j].config(image=king1p,bg='#DCC450')
                        else:
                            zone[i][j].config(image=king1,bg='#EFE4B0')
                    else:
                        if phase==1 and turn==1:
                            zone[i][j].config(image=pawn1p,bg='#DCC450')
                        else:
                            zone[i][j].config(image=pawn1,bg='#EFE4B0')
                        
                else:
                    if board[i][j].startswith('p2k'):
                        if phase==1 and turn==2:
                            zone[i][j].config(image=king2p,bg='#DCC450')
                        else:
                            zone[i][j].config(image=king2,bg='#EFE4B0')
                    else:
                        if phase==1 and turn==2:
                            zone[i][j].config(image=pawn2p,bg='#DCC450')
                        else:
                            zone[i][j].config(image=pawn2,bg='#EFE4B0')

    for i in range(2):
        p1dcards[i].config(image=plist[chcards.index(p1cards[i])])
        p2dcards[i].config(image=plist[chcards.index(p2cards[i])])

    udcard.config(image=plist[chcards.index(ucard)])

    if phase==3:
        fturnb.config(bg='#DCC450')
    else:
        fturnb.config(bg='#EFE4B0')

    if turn==1:
        for i in range(2):
                p1dcards[i].grid(row=9,column=1+2*i)
                p2dcards[i].grid(row=1,column=1+2*i)
        lt0.config(text="Red Player's Turn",fg='#880015')
    else:
        for i in range(2):
            p1dcards[i].grid(row=1,column=1+2*i)
            p2dcards[i].grid(row=9,column=1+2*i)
        lt0.config(text="Blue Player's Turn",fg='#7092BE')

def vcheck():
    global board
    global phase
    global vs
    global turn
    global winner

    v1=0
    v2=0

    a1=0
    a2=0
    
    for i in range(5):
        for j in range(5):
            if board[i][j]=='p1k':
                a1=1
                if i==0 and j==2 and turn==1:
                    v1=1
            elif board[i][j]=='p2k':
                a2=1
                if i==0 and j==2 and turn==2:
                    v2=1

    if a2==0 or v1==1:
        phase=4
        winner='p1'
        vscreen()

    elif a1==0 or v2==1:
        phase=4
        winner='p2'
        vscreen()

def cancel(event):
    global phase
    global selcard
    global selcardp
    global selfig
    
    if phase!=3:
        selcard=0
        selcardp=0
        selfig=0

        boardclearing()
        phase=0
    
    supdate()
                
def cselect(event):
    global w
    global p1dcards
    global p2dcards
    global udcard
    global zone
    global lt0
    global lt1
    global lt2
    global lt3
    global cards
    global p1p1
    global p1p2
    global p1p3
    global p1p4
    global p1k
    global p2p1
    global p2p2
    global p2p3
    global p2p4
    global p2k
    global board
    global cancelb
    global fturnb
    global p1cards
    global p2cards
    global ucard
    global phase
    global selcard
    global selcardp
    global turn
    
    if phase==0:
        info=event.widget.grid_info()
        row=info["row"]
        column=info["column"]
        if row==9:
            phase=1
            if column==1:
                if turn==1:
                    selcard=p1cards[0]
                else:
                    selcard=p2cards[0]
                selcardp=0
            else:
                if turn==1:
                    selcard=p1cards[1]
                else:
                    selcard=p2cards[1]
                selcardp=1
            
    supdate()

def move(event):
    global w
    global p1dcards
    global p2dcards
    global udcard
    global zone
    global lt0
    global lt1
    global lt2
    global lt3
    global cards
    global p1p1
    global p1p2
    global p1p3
    global p1p4
    global p1k
    global p2p1
    global p2p2
    global p2p3
    global p2p4
    global p2k
    global board
    global cancelb
    global fturnb
    global p1cards
    global p2cards
    global ucard
    global phase
    global selcard
    global selcardp
    global selfig
    global chcards
    global movements
    global figp
    global figpx
    global figpy
    global turn

    if phase==1:
        info=event.widget.grid_info()
        row=info["row"]
        row-=3
        column=info["column"]

        if turn==1:

            figp=1
        
            if board[row][column]=='p1p1':
                board[row][column]='p1p1.'
                figp='p1p1.'
            elif board[row][column]=='p1p2':
                board[row][column]='p1p2.'
                figp='p1p2.'
            elif board[row][column]=='p1p3':
                board[row][column]='p1p3.'
                figp='p1p3.'
            elif board[row][column]=='p1p4':
                board[row][column]='p1p4.'
                figp='p1p4.'
            elif board[row][column]=='p1k':
                board[row][column]='p1k.'
                figp='p1k.'
            else:
                figp=0

            if figp!=0:

                figpx=row
                figpy=column
                
                phase=2

                mcoor=chcards.index(selcard)
                
                for i in range(len(movements[mcoor])):
                    mcoorx=row+movements[mcoor][i][0]
                    mcoory=column+movements[mcoor][i][1]
                    if mcoorx<5 and mcoorx>=0 and mcoory<5 and mcoory>=0:
                        if board[mcoorx][mcoory]=='*':
                            board[mcoorx][mcoory]=','
                        elif board[mcoorx][mcoory]=='p2p1':
                            board[mcoorx][mcoory]='p2p1,'
                        elif board[mcoorx][mcoory]=='p2p2':
                            board[mcoorx][mcoory]='p2p2,'
                        elif board[mcoorx][mcoory]=='p2p3':
                            board[mcoorx][mcoory]='p2p3,'
                        elif board[mcoorx][mcoory]=='p2p4':
                            board[mcoorx][mcoory]='p2p4,'
                        elif board[mcoorx][mcoory]=='p2k':
                            board[mcoorx][mcoory]='p2k,'
                
                supdate()

        else:

            figp=1
        
            if board[row][column]=='p2p1':
                board[row][column]='p2p1.'
                figp='p2p1.'
            elif board[row][column]=='p2p2':
                board[row][column]='p2p2.'
                figp='p2p2.'
            elif board[row][column]=='p2p3':
                board[row][column]='p2p3.'
                figp='p2p3.'
            elif board[row][column]=='p2p4':
                board[row][column]='p2p4.'
                figp='p2p4.'
            elif board[row][column]=='p2k':
                board[row][column]='p2k.'
                figp='p2k.'
            else:
                figp=0

            if figp!=0:

                figpx=row
                figpy=column
                
                phase=2

                mcoor=chcards.index(selcard)
                
                for i in range(len(movements[mcoor])):
                    mcoorx=row+movements[mcoor][i][0]
                    mcoory=column+movements[mcoor][i][1]
                    if mcoorx<5 and mcoorx>=0 and mcoory<5 and mcoory>=0:
                        if board[mcoorx][mcoory]=='*':
                            board[mcoorx][mcoory]=','
                        elif board[mcoorx][mcoory]=='p1p1':
                            board[mcoorx][mcoory]='p1p1,'
                        elif board[mcoorx][mcoory]=='p1p2':
                            board[mcoorx][mcoory]='p1p2,'
                        elif board[mcoorx][mcoory]=='p1p3':
                            board[mcoorx][mcoory]='p1p3,'
                        elif board[mcoorx][mcoory]=='p1p4':
                            board[mcoorx][mcoory]='p1p4,'
                        elif board[mcoorx][mcoory]=='p1k':
                            board[mcoorx][mcoory]='p1k,'
                
                supdate()

    elif phase==2:
        info=event.widget.grid_info()
        row=info["row"]
        row-=3
        column=info["column"]
        done=0

        if board[row][column].endswith(','):
            board[figpx][figpy]='*'
            board[row][column]=figp
            done=1
            
        if done==1:
            phase=3

            a=ucard
            ucard=selcard

            if turn==1:
                p1cards[selcardp]=a

            else:
                p2cards[selcardp]=a
            
            boardclearing()
            
            supdate()

            vcheck()

def nextturnb(event):
    nextturn()

def nextturn():
    global phase
    global board
    global p1dcards
    global p2dcards
    global turn
    global botplay
    
    if phase==3:
        
        phase=0

        for i in range(3):
            for j in range(5):
                if i!=2 or j<=2:
                    a=board[i][j]
                    board[i][j]=board[4-i][4-j]
                    board[4-i][4-j]=a

        if turn==1:
            turn=2
        else:
            turn=1
        
        supdate()

        if botplay==1 and turn==2:
            botturn()

def botturn():
    #print('hello')
    global p2cards
    global board
    global selcard
    global movements
    global chcards
    global ucard
    global phase
    global selcardp

    options=[]
    optionxs=[]
    optionys=[]
    optioncards=[]
    optioncardsb=[]

    for h in range(2):

        selcard=p2cards[h]

        figures=[]
        figxs=[]
        figys=[]
    
        for i in range(5):
            for j in range(5):
                if board[i][j].startswith('p2'):
                    figures.append(board[i][j])
                    figxs.append(i)
                    figys.append(j)

        for w in range(len(figures)):
            fig=figures[w]
            figx=figxs[w]
            figy=figys[w]

            mcoor=chcards.index(selcard)
                
            for i in range(len(movements[mcoor])):
                mcoorx=figx+movements[mcoor][i][0]
                mcoory=figy+movements[mcoor][i][1]
                if mcoorx<5 and mcoorx>=0 and mcoory<5 and mcoory>=0:
                    if board[mcoorx][mcoory]=='*':
                        board[mcoorx][mcoory]=','
                    elif board[mcoorx][mcoory]=='p1p1':
                        board[mcoorx][mcoory]='p1p1,'
                    elif board[mcoorx][mcoory]=='p1p2':
                        board[mcoorx][mcoory]='p1p2,'
                    elif board[mcoorx][mcoory]=='p1p3':
                        board[mcoorx][mcoory]='p1p3,'
                    elif board[mcoorx][mcoory]=='p1p4':
                        board[mcoorx][mcoory]='p1p4,'
                    elif board[mcoorx][mcoory]=='p1k':
                        board[mcoorx][mcoory]='p1k,'

            for i in range(5):
                for j in range(5):
                    if board[i][j].endswith(','):
                        options.append(board[i][j])
                        optionxs.append(i)
                        optionys.append(j)
                        optioncards.append(selcard)
                        optioncardsb.append(h)

    optwin=0
    opttake=[]

    optpick='a'
    optionpick=0

    for i in range(len(options)):
        if options[i]=='p1k,':
            optpick=i
        elif options[i].startswith('p2'):
            opttake.append(i)

    if optpick!='a':
        optionpick=optpick
    elif len(opttake)!=0:
        optionpick=opttake[random.randint(0,len(opttake)-1)]
    else:
        optionpick=random.randint(0,len(options)-1)

    board[optionxs[optionpick]][optionys[optionpick]]=fig
    board[figx][figy]='*'

    selcard=optioncards[optionpick]
    selcardp=optioncardsb[optionpick]
    
    a=ucard
    ucard=selcard
    p2cards[selcardp]=a

    phase=3

    boardclearing()
            
    supdate()

    vcheck()
    
    nextturn()
    

def pscreen():
    global m
    global m1
    global m2
    global m3
    global m4
    global w
    global p1dcards
    global p2dcards
    global udcard
    global zone
    global lt0
    global lt1
    global lt2
    global lt3
    global cards
    global p1p1
    global p1p2
    global p1p3
    global p1p4
    global p1k
    global p2p1
    global p2p2
    global p2p3
    global p2p4
    global p2k
    global board
    global cancelb
    global fturnb
    global p1cards
    global p2cards
    global ucard

    p1cards=[]
    p2cards=[]
    for i in range(2):
        a=cards.pop(random.randint(0,len(cards)-1))
        p1cards.append(a)
        a=cards.pop(random.randint(0,len(cards)-1))
        p2cards.append(a)
    ucard=cards.pop(random.randint(0,len(cards)-1))
    
    board=[]
    for i in range(5):
        board.append([])
        for j in range(5):
            board[i].append('*')

    board[p1p1[0]][p1p1[1]]='p1p1'
    board[p1p2[0]][p1p2[1]]='p1p2'
    board[p1k[0]][p1k[1]]='p1k'
    board[p1p3[0]][p1p3[1]]='p1p3'
    board[p1p4[0]][p1p4[1]]='p1p4'
    board[p2p1[0]][p2p1[1]]='p2p1'
    board[p2p2[0]][p2p2[1]]='p2p2'
    board[p2k[0]][p2k[1]]='p2k'
    board[p2p3[0]][p2p3[1]]='p2p3'
    board[p2p4[0]][p2p4[1]]='p2p4'
    
    m.destroy()
    w=Tk()
    w.title('Onitama')
    w.config(bg='#EFE4B0')

    lt0=Label(w,text="Red Player's Turn",fg='#880015',bg='#EFE4B0',font=(16))
    lt0.grid(row=0,column=1,columnspan=3,ipady=8)
    
    p2dcards=[]
    for i in range(2):
        p2dcards.append(Button(w))
        p2dcards[i].config(bg='#EFE4B0')
        p2dcards[i].bind('<Button>',cselect)
        p2dcards[i].grid(row=1,column=1+2*i)

    lt1=Label(w,text='',bg='#EFE4B0')
    lt1.grid(row=2)
        
    zone=[]
    for i in range(5):
        zone.append([])
        for j in range(5):
            zone[i].append(Button(w))
            zone[i][j].config(bg='#EFE4B0')
            zone[i][j].bind('<Button>',move)
            zone[i][j].grid(row=i+3,column=j)

    lt2=Label(w,text='',bg='#EFE4B0')
    lt2.grid(row=8)
     
    p1dcards=[]
    for i in range(2):
        p1dcards.append(Button(w))
        p1dcards[i].config(bg='#EFE4B0')
        p1dcards[i].bind('<Button>',cselect)
        p1dcards[i].grid(row=9,column=1+2*i)

    lt3=Label(w,text='',bg='#EFE4B0')
    lt3.grid(row=5,column=5)

    udcard=Button(w)
    udcard.config(bg='#EFE4B0')
    udcard.grid(row=5,column=6)

    fturnb=Button(w,text='Next Turn')
    cancelb=Button(w,text='Cancel')
    fturnb.config(bg='#EFE4B0',height=1,width=9)
    cancelb.config(bg='#EFE4B0',height=1,width=9)
    fturnb.bind('<Button>',nextturnb)
    cancelb.bind('<Button>',cancel)
    fturnb.grid(row=10,column=5)
    cancelb.grid(row=11,column=5)

    supdate()

def cpscreen(event):
    pscreen()

def spscreen(event):
    global botplay
    botplay=1
    pscreen()

def q(event):
    exit(0)

def playa(event):
    global vs
    global w
    global m

    vs.destroy()
    w.destroy()

    m=Tk()

    resetvals()

    pscreen()

def mmenu(event):
    global vs
    global w
    global m
    global botplay

    botplay=0

    vs.destroy()
    w.destroy()

    resetvals()
    mscreen()

def vscreen():
    global vs
    global winner
    global wl
    global w1im
    global vb1
    global vb2

    vs=Toplevel()
    vs.title('Onitama')
    vs.config(bg='#EFE4B0')

    '''
    if winner=='p1':
        wl=Label(vs,text='Red player wins',bg='#EFE4B0',fg='#880015',font=30)
    else:
        wl=Label(vs,text='Blue player wins',bg='#EFE4B0',fg='#7092BE',font=30)
        
    wl.grid(row=0)
    '''

    if winner=='p1':
        w1im=PhotoImage(file='redpwins.png')
    else:
        w1im=PhotoImage(file='bluepwins.png')

    w1=Label(vs,image=w1im,bg='#EFE4B0')

    w1.grid(row=0)
    
    vb1=Button(vs,text='Play Again',bg='#EFE4B0',height=1,width=10)
    vb2=Button(vs,text='Main Menu',bg='#EFE4B0',height=1,width=10)

    vb1.bind('<Button>',playa)
    vb2.bind('<Button>',mmenu)
    
    vb1.grid(row=1)
    vb2.grid(row=2)

def back(event):
    rs.destroy()
    mscreen()

def rscreen(event):
    global m
    global rs
    global rules
    global rs1
    global rsb1

    m.destroy()

    rs=Tk()
    rs.title('Onitama')
    rs.config(bg='#EFE4B0')

    rules=PhotoImage(file='rules.png')
    rs1=Label(rs,image=rules,bg='#EFE4B0')
    rs1.grid(row=0)

    rsb1=Button(rs,text='Back',bg='#EFE4B0')
    rsb1.bind('<Button>',back)
    rsb1.grid(row=1)

def mscreen():
    global m
    global m1
    global m2
    global m3
    global m4
    global mt
    global w
    global p1dcards
    global p2dcards
    global ucard
    global zone
    global lt1
    global lt2
    global lt3
    global cards
    global p1p1
    global p1p2
    global p1p3
    global p1p4
    global p1k
    global p2p1
    global p2p2
    global p2p3
    global p2p4
    global p2k
    global board
    global title
    
    m=Tk()
    m.title('Onitama')
    m.config(bg='#EFE4B0')

    title=PhotoImage(file='title.png')
    
    mt=Label(m,image=title,bg='#EFE4B0')
    mt.grid(row=1,column=1,rowspan=4)
    
    m1=Button(m,text='Singleplayer',bg='#EFE4B0',height=2,width=14)
    m2=Button(m,text='Multiplayer',bg='#EFE4B0',height=2,width=14)
    m3=Button(m,text='How To Play',bg='#EFE4B0',height=2,width=14)
    m4=Button(m,text='Exit',bg='#EFE4B0',height=2,width=14)
    m1.bind('<Button>',spscreen)
    m2.bind('<Button>',cpscreen)
    m3.bind('<Button>',rscreen)
    m4.bind('<Button>',q)
    m1.grid(row=1,column=0)
    m2.grid(row=2,column=0)
    m3.grid(row=3,column=0)
    m4.grid(row=4,column=0)

mscreen()
