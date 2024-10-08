# CTI 110
# P1LAB2-Receipt
# Hassan
# 10/1/24

print("P1LAB2")
# Today lets do a resturant
# that only sells biryani and kemma 

# declare our variables 
num_biryani = 0
num_keema = 0
biryani_cost = 17.99
kemma_cost = 14.99

print("Can i take your order")
# have to convet order into an integer so it works 
num_biryani = int(input("How many biryani's?"))

print("You ordered", num_biryani, "biryani")

num_kemma = int(input("How much kemma's?"))
print("You ordered", num_kemma, "keema's")

    # Adding up to total
biryani_total = num_biryani * biryani_cost
kemma_total = num_kemma * kemma_cost
meal_total = biryani_total + kemma_total

# print the recipet
#emojipedia for emojis
#format() lets us show 2 decimal places 
print("-" * 20)
print(num_biryani, "🍛 Biryani\t$", format(biryani_total, ".2f"))
print(num_kemma, "🍲 Kemma\t$", format(kemma_total, ".2f"))
print("-" * 20)
print("Total\t\t$", format(meal_total, ".2f"))
