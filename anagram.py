str1=input("Enter the first string:")
str2=input("Enter the second string:")  

is_anagram=sorted(str1)==sorted(str2)
if is_anagram:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")