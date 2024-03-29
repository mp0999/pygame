import random

top_of_rang = input("Type a number: ")

if top_of_rang.isdigit():
    top_of_rang = int(top_of_rang)
    
    if top_of_rang <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_num = random.randint(0,top_of_rang)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == random_num:
        print("you got it!")
        break
    elif user_guess > random_num:
            print("you were above the number!")
    else:
        print("you were below the number!")
            
print(f"you got it in {guesses} guesses")
