import random
def game(comp,you):
    if(comp==you):
        return None

    if(comp=='r'and you=='p'):
        return False
    elif(comp=='r'and you=='s'):
        return True

    if(comp=='p'and you=='s'):
        return False
    elif(comp=='p'and you=='r'):
        return True

    if(comp=='s'and you=='r'):
        return False
    elif(comp=='s'and you=='p'):
        return True

print("Welcome to The Game")
print("Rock ,Paper Scissor")
print("Computer: Please select :Rock(r),Paper(p), Scissor(s): ")
comp =random.randint(1,3)
print("Computer has picked from the option")
if(comp==1):
    comp='r'
elif(comp==2):
    comp='p'
elif(comp==3):
    comp='s'
you=input("Player: Please select :Rock(r),Paper(p), Scissor(s): ")

print('Computer has chosen:'+ comp)
print('You has chosen:'+ you)

    
a=game(comp,you)

if(a==None):
    print('Its a tie.')
if(a==False):
    print('You  Won!')
if(a==True):
    print('You Lose!')
