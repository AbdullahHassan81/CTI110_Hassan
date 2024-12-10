#CTI-110
#P1HW2
#Abdullah Hassan
#10/8/24

#This program does a travel budegt
#use float with only code that has to do with numbers 

"""
3.Ask user to enter thier bugdet 
ask user to enter destination
ask user for gas amount 
ask user for accomadtion amount
ask user food amount
add expenses
subtract expenses from budget
display results
"""

print("🚌" * 5, "Trip Calculator", "🚌" * 5)
budget = float(input("What is your travel budget? $"))
#Where they going
destination = input("Where are you going?")


#TODO: the rest 
Gas=float(input("How much do you think you will spend on gas?"))
Food=float(input("Approximately, how much do you need for food?"))

print("-----Travel Expenses-----")

Location=input("Location:")
Budget=float(input("Initial Budget:"))
Accomodation=float(input("Accomodation:"))
Food=float(input("Food:"))
Remainder=float(input("Remaining Balance:"))
