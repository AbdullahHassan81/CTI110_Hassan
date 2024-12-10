#Abdullh Hassan
#10/17/24
#P2LAB2 - Lists
#CTI-110

# P1 - See P2HW2
numbers = [1, 2, 3, 4]
print(numbers)

# als the user ro enter four numbers
print("please enter 4 numbers (enter after each)")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

my_numbers = [num1, num2, num3, num4]
print("You entered these numbers:", my_numbers)
print("There are", len(my_numbers), "numbers.")
print("Smallest ", min(my_numbers))
print("Largerst ", max(my_numbers))
print("The total is: ", sum(my_numbers))
# average is total divided by number of items
average = sum(my_numbers) / len(my_numbers)
print("The average: ", average)

# Part2 - turtle graphics
# basic for loop
for number in my_numbers: 
    print(number)

#next, draw using for loops