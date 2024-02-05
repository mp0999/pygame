# Snake water or gun  & Rock paper scissors
import random

def game(comp, players):
    # If two values are equal, declare tie
    if comp == players:
        return None
    
    # Check all possibilities when computer chose 's', 'w', 'g'
    elif comp == 's':
        if players == 'w':
            return False
        elif players == 'g':
            return True
        
    elif comp == 'w':
        if players == 'g':
            return False
        elif players == 's':
            return True
        
    elif comp == 'g':
        if players == 's':
            return False
        elif players == 'w':
            return True

print("computer turn: Snake(s) Water(w) or Gun(g)?")
randNum = random.randint(1,3)
if randNum == 1:
    comp = 's'
elif randNum == 2:
    comp = 'w'
elif randNum == 3:
    comp = 'g'

players = input("Players turn: Snake(s) Water(w) or Gun(g)?") 
a = game(comp, players)

print(f"computer chose {comp}")
print(f"players chose {players}")

if a == None:
    print("The game is tie!")
elif a:
    print("you win yehh say Radhe radhe!")
else:
    print("computer win")