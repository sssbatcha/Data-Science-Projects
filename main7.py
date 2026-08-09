numbers= list(map(int, input("Enter numbers with space:").split()))
print(numbers)
mul=1
for i in numbers:
    mul=mul*i
print(mul)