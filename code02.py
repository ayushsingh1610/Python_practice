sal = int(input("Enter the salary = "))

hra = (10 * sal)/100
ta = (5 * sal)/100
da = (40*sal)/100

total_sal = sal + hra + ta + da

annual_sal = total_sal * 12

tax = 0
if(annual_sal<500000):
    tax=0
elif (annual_sal >= 500000):
    tax=10
    
print("\nMonthly salary = ",total_sal)
print("Annual salary = ", annual_sal)
print("Tax on salary = ", (annual_sal*tax)/100)
    