''' 
1 for sanke
-1 for water
0 for gun
'''
import random
computer = random.choice([1,-1,0])
youstr = input("Enter Your Choice : ")
youDict = {"s": 1, 'w': -1, 'g': 0}
revDict = {1: "Sanake", -1: "Water", 0: "Gun"}

you = youDict[youstr]
print(f"You choose {revDict[you]}\n computer choose {revDict[computer]}")

if(computer == you):
    print("Its a Draw")
else:
    if(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 0 and you == 1):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You win!")
    else:
        print("Something went wrong!")


