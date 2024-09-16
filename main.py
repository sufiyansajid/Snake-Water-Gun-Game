import random
'''''
1 for snake
-1 for water
0 for gun
'''''

computer = random.choice([-1,0,1])

youstr = input("enter ur choice: ")

youdict = {"s":1, "w":-1, "g":0}
reversedict = {1:"snake", -1:"water", 0:"gun"}

you = youdict[youstr]

# by now we have two variables computer and you

print(f"u choose {reversedict[you]} \ncomputer choose {reversedict[computer]}")

if(computer == you):
    print("its a draw!")

else:
    if(computer == -1 and you == 1):
        print("you win!")

    elif(computer == -1 and you == 0):
        print("you lose!")

    elif(computer == 1 and you == -1):
        print("you lose!")

    elif(computer == 1 and you == 0):
        print("you win!")

    elif(computer == 0 and you == -1):
        print("you win!")

    elif(computer == 0 and you == 1):
        print("you lose!")


    else:
        print("something went wrong!")

'''''
another logic for  this code is:

if((computer - you) == -1 or (computer - you) == 2):
    print("you lose!")

else:
    print("you win!")

'''''