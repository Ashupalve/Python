import random
n = random.randint(1 , 100)
a= -1
guesses = 0 

while (a!= n):
    a = int(input("guess the number:"))
    if a<n :
        guesses +=1
        print("Guess Higher Number")
    else :
        guesses +=1
        print("Guess Lower Number")
print(f"You guessed Number corrctly in {guesses} atempts")