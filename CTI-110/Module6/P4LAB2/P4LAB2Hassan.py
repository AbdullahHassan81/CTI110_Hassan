print("Test program")
count = 1
while count <=5:
    print("count is", count)
    count = count + 1
print("done")

#for number in [1,2,3,4,5]:
for number in range(1,6):
    print(number)
print("done")

#input validation
num =int(input("Type a number from 1 to 3:"))
while num < 1 or num > 3:
    print("Please try again")
    num  =int(input("Type a number from 1 to 3:"))
print("You entered:", num)


#P4LAB2
#Hassan
#11/14/24
#ask for a num higher than 0 
#display times table for that num
#from 1 to 12

def times_table():
    num = int(input("Enter an integer: "))
    while(num<0):
        print("No negative numbers")
        num = int(input("Enter an integer: "))
    print("You entered", num)
    #times table
    for num2 in range(1,13):
        answer = num * num2 
        print(num, "*", num2, "=", answer)
    

def main():
    times_table()
    again = input("Do you want to run again?")
    while (again == "yes"):
        times_table()
        again = input("Do you want to run again?")
    print("Goodbye!")

main()
