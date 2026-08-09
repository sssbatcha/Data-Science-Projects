numbers = list(map(int, input("Enter numbers with space:").split()))
print(numbers)
#large=max(numbers)
large=numbers[0]
for i in numbers:
    if i>large:
        large=i
print(large)