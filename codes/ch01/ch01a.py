print("Welcome!") 
g = input("Guess the number: ") 
guess = int(g) 
if guess == 5: 
    print("You win!") 
else: 
    if guess > secret: 
        print("Too high") 
    else: 
        print("Too low") 
print("Game over!")
