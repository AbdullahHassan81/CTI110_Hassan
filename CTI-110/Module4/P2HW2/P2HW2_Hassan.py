#Abdullah Hassan
#CTI 110
#P2HW2-grading modules 
#10/29/24

#look at P2LAB2
Module1 = int(input("Enter grade for Module 1:"))
Module2 = int(input("Enter grade for Module 2:"))
Module3 = int(input("Enter grade for Module 3:"))
Module4 = int(input("Enter grade for Module 4:"))
Module5 = int(input("Enter grade for Module 5:"))
Module6 = int(input("Enter grade for Module 6:"))

print("------Results------")


Modules = [Module1, Module2, Module3, Module4, Module5, Module6]
print(Modules)
print("Lowest Grade:", min(Modules))
print("Highest Grade:", max(Modules))
print("Sum of Grade:", sum(Modules))
Average = sum(Modules)/len(Modules)
print("Average:", Average) 
