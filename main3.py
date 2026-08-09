'''def find_max(num1,num2,num3):
    maximum = max(num1,num2,num3)
    return maximum



num1 = float(input("Enter the num1:"))
num2 = float(input("Enter the num2:"))
num3 = float(input("Enter the num3:"))
maximum = find_max(num1,num2,num3)
print(f"The Max of {num1},{num2},{num3} is :{maximum}")'''

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

