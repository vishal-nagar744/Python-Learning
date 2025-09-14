# word ka palindrome check

# Step 1: Input lo
word = input("Enter a word: ")

# Step 2: Reverse string banao
reversed_word = word[::-1]  # slicing method
# print(reversed_word)


# Step 3: Compare original aur reversed

if word == reversed_word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")



# numbers ka palindrome check

num = input("Enter a number: ")

if num == num[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")


