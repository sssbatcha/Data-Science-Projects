"""def is_leaf(year):
    return ((year%400 == 0) or (year%4 == 0 and year%100 != 0))


year = int(input("Enter the Input:"))
if is_leaf(year):
    print(f"{year} is a leap year")

else:
    print(f"{year} is a not leap year")"""

def find_max(num1,num2,num3):
    if (num1 > num2 and  num1>num3):
        maximum = num1
    elif (num2 > num1 and  num2 > num3):
        maximum = num2
    else:
        maximum = num3
    return maximum



num1 = float(input("Enter the num1:"))
num2 = float(input("Enter the num2:"))
num3 = float(input("Enter the num3:"))
maximum = find_max(num1,num2,num3)
print(f"The Max of {num1},{num2},{num3} is :{maximum}")
