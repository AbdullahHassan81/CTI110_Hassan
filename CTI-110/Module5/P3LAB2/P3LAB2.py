#Abdullah Hassan
#CTI 110
#10/29/24
#P3LAB2
import random 

def main():
    print("Craps Game")
    print("roll from 1 to 6")
    #die1= int(input("First Die:"))
    #die2= int(input("Second Die:"))
    #random rolls
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    
    total = die1 + die2
    print("Roll:", die1, "+", die2,"is", total)

    # did we win or lose
    # 7 or 11 = win, 2 or 12 = loss, rest is to be contintued
    if total ==7:
              print ("You win!")
    elif total ==11:
             print("You win!")
    elif total ==2:
            print("You lose.")
    elif total ==12:
            print("You lose.")
    else:
        print("point was", total)
        print("To be continued...")

#start program
main()
