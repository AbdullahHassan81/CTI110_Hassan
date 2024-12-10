#P3HW2
#Abdullah Hassan
#11/19/24
#This program is going to identify employee things

name = (input("Enter employee's name: "))
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("-" * 35)



if hours >40:
    overtime_hrs = hours-40
    overtime_rate = pay_rate *1.5
    overtime_pay = overtime_hrs * overtime_rate
    reghour_pay = 40 * pay_rate
else:
    reghour_pay = hours * pay_rate
    overtime_pay = 0
    overtime_hrs = 0


gross_pay = reghour_pay + overtime_pay

print ("Employee Name: ", name)
print()

print("Hours Worked   Pay Rate   OverTime   OverTime Pay    RegHour Pay    Gross Pay")
print("-" * 78)
print(f'{hours}{pay_rate}')
print(f'{hours:<15.2f}{pay_rate:<10.5f}{overtime_hrs:<14f}{overtime_pay:10.6f}{reghour_pay:15f}{gross_pay:15f}')
##print("Hours Worked: ", hours)
##print("Pay Rate: ", pay_rate)
##print("OverTime: ", overtime_hrs)
##print("OverTime Pay: ", overtime_pay)
##print("RegHour Pay: $", reghour_pay)
##print("Gross Pay: $", gross_pay)

