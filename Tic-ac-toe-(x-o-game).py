import time
import random
win = False
displaylist = {'A': ['-', '-', '-'], 'B': ['-', '-', '-'], 'C': ['-', '-', '-']}
position=['A1','A2','A3','B1','B2','B3','C1','C2','C3']
winnerBasket = [['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3'],['A1','B2','C3'],['A3','B2','C1'],['A1','B1','C1'],['A2','B2','C2'],['A3','B3','C3']]
xBasket=[]
oBasket=[]

#just print game board for display to user
def prixo(b):
    for i in b:
        print(i,str(b[i]).replace('\'',' ').replace(",","|").replace("]","").replace("[",""))
        print("   ----------- ")
    print("    1   2   3")

#check place for X-O and return True or False if position took before
def checkExist(tab,x,y):
    if tab[x.upper()][int(o)-1] == "-":
        return True
    else:
        return False

print("""
Welcome to X-O Game
if you think you can defate me.
be my guest
I am O
You are X
Select Your table
""")
prixo(displaylist)#display empty Position at the start
#return new O position
def newOposition(position):
    l = position[random.randrange(0,len(position))]
    return l

#Check basket for find winner
def winner(checkList):
    for l in winnerBasket:
        o = []
        for n in l:
                if n in checkList:
                    o.append(n)
        if l == o:
            return True

try:
    #Game Main is here
    # get data from user
    # print X and O in position 
    for i in range(9):
        if win != True:
            x = input("Which? ")
            for x,o in x.split():
                if x.upper()+o in position:
                    if(checkExist(displaylist,x,o)):
                        xBasket.append(x.upper()+o)
                        displaylist[x.upper()][int(o)-1]="X"#add X to selected position
                        position.remove((x+o).upper())#Remove selected position from position list
                        prixo(displaylist)
                        if winner(xBasket):#check if X is winner
                            print("You Are A CHITTER")
                            win = True
                            break
                        print("It's my turn, Wait a secound")
                        time.sleep(1)
                        op = newOposition(position)
                        position.remove((op).upper())#Remove selected position from position list
                        oBasket.append(op[0].upper()+op[1])
                        displaylist[op[0].upper()][int(op[1])-1]="O"
                        prixo(displaylist)
                        if winner(oBasket):#Check if O is winner
                            win = True
                            print("HAHAHAHAHA ....LOOOOOSERRRR")
                            break
                        #select O by system
                    else:
                        print("______________________________________")
                        print('Are You Stupid?\n0_o\nPlease select empty place')
                else:
                    print("I think you are stupid\nYou cant see the big table?\n\n")
        else:
            break
except:
    print("\n")
    pass
