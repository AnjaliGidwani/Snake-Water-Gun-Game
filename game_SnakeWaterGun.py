import random 
def gameWin(comp, you):
    if comp ==you:
        return None
    
    elif comp=='s':
        if you =='w':
            return False
        elif you =='g':
            return True
    
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
print("Comp turn: Snake(s) Water(w) Gun(g)? : ")
randNum = random.randint(1,3)
if randNum ==1:
    comp='s'

elif randNum==2:
    comp='w'

else:
    comp='g'

you = input("Your turn: Snake(s) Water(w) Gun(g)? : ")
a = gameWin(comp, you)
print(f"Computer choose {comp}")
print(f"you choose {you}")

if a==None:
    print("The game is a tie!")

elif a:
    print("You win!")

else:
    print("You lose!")