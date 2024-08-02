import random
n = random.randint(1,100)
a = -1
guesses = 0
while n != a:
    guesses += 1
    a = int(input("Guess a number: "))
    if a > n:
        print("Lower number please")
    else:
        print("Higher number please")
print(f"You have guessed the number correctly in {guesses} attempt")
