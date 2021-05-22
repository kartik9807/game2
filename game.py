# cricket game : task 

import random

print(
    "Rules : 1.first computer batting , you have to out computer\n 2.if you out computer you have to make runs that computer have made\n 3.if computer out you,you lose or else you won\n"
)
while(True):

        
    print(" : game start : ")

    sum1 = 0

    while (True):
        comp = random.randint(1, 10)
        n = int(input("Enter your number : "))

        if (n != comp):
            sum1 = (sum1 + comp)

        else:
            break

        print ("computer has taken number", comp)

        print("present score of Computer's is ", sum1)
    print ("computer out")

    print ("computer total score", sum1)
    
    print ("you have to make {} run".format(sum1 + 1))

    sum2 = 0
    flag = 0

    while (1):

        p = random.randint(1, 10)

        player = int(input("enter your number : "))

        if (player > 10):
            print("no.out of range")
            break

        if (player != p):
            sum2 = sum2 + player
        else:
            break

        print ("computer has taken number", p)

        print ("run of player : " + str(sum2))


        if (sum2 > sum1):
            # print ("computer has chosen {}".format(p))
            print("you won")
            flag = 1
            break
    if flag == 0:
        if(sum2 == sum1):
            
            
            print ("computer has chosen {}".format(p))
            print("tie")
            break

        print("Computer has chosen {}".format(p))

        print ("player need {} more runs to win".format(sum1+1-sum2))


        print ("computer won")

    print(" : game finished : ")
    

    n = input("Did you want to play the match again press(yes(y)) or press(no(n)) : ")

    if((n == "yes" or n == "y")):
        continue

    elif((n == "no" or n == "n")):
        print("Good bye , See you next time !")
        break

    else:
        print("Wrong input")
        break

# not needed

z = input("how was the game ? ")


print("you rated {}".format(z))


