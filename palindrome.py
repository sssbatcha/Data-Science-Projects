string = input("Enter the string:")
is_palindrome = string == string[::-1]
print(f"{string} is a palindrome" if is_palindrome else f"{string} is not a palindrome")