#P2LAB1
#CTI 110
#Abdullah 
#10/10/24

#this program adds sales
#add sales tax


print("What are you buying?")
buying = input()
item_amount=int(input("How much do you want?"))
price = float(input("The cost is: $"))
total = item_amount * price
tax = total * .08


print("-" * 15)
print("the total is")
print(float(format(total, ".2f")))
print("+tax = ",format(total + tax, ".2f"))






