# P4HW1
# Hassana
# 12/12/24

print (float(input("How many scores do you want to enter?")))
Score = [1-5]
Score1 =(float(input("Enter Score #1: ")))
Score2 =(float(input("Enter Score #2: ")))
Score3 = (float(input("Enter Score #3: ")))

#look at P2HW2
#look at P3HW1
score = 0
if score <=-1:
    print('INVALID Score entered!!!!')
    print ("Score should be between 0 and 100")
    print (float(input("Enter score #3 again: ")))
Score4 =  (float(input("Enter score #4: ")))
Score5 = (float(input("Enter score #5: ")))
print("---------Results---------")

Scores = [Score1, Score2, Score3, Score4, Score5]
print(Scores)
print("Lowest Score:", min(Scores))
print("Modifed List:",(Score1, Score2, Score3, Score4, Score5))
average = sum(Scores)/len(Scores)
print("Average:", average)
if average >= 90:
    print('Your grade is: A')
elif average > 80:
    print('Your grade is: B')
elif average > 70:
    print('Your grade is: C')
elif average > 60:
    print('Your grade is: D')
elif average > 50:
    print('Your grade is: F')



