import random
computer = random.choice([-1, 0, 1])
youstr = (input("Enter your choice"))
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

else:  
    if(computer ==-1 and you ==1):
        print("You win")
    elif(computer ==-1 and you==0):
        print("You lose")
    elif(computer ==1 and you ==-1):   
        print("You lose")
    elif(computer ==1 and you ==0):
        print("you win")
    elif(computer ==0 and you ==-1):
        print("You win")
    elif(computer ==0 and you ==1):
        print("You lose")
    else:
        print("somthing went wrong")                       