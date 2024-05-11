
import random

user = input("Enter 0 for Snake \nEnter 1 for Water \nEnter 2 for Gun \n:") 

computer = random.randint(0,2)

if(computer == 2):
    print("Computer picked Gun")

elif(computer == 1):
    print("Computer picked water")

else:
    print("Computer picked Snake")

matrix = [[0,1,-1],[-1,0,1],[1,-1,0]]

check = matrix[int(user)][int(computer)]

if(check == 1):
    print("You win!!!")

elif(check == 0):
    print("It's a Draw")

else:
    print("You Lose")
