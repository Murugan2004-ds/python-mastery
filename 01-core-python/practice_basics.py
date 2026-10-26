# 1. Asks for the user's name and birth year with input().
# 2. Converts the birth year to a number and works out the age,using 2026 as the current year.
# 3. Prints one f-string sentence in this format: Hello MURUGAN, you are 22 years old. the name should be in uppercase.
# 4. Prints True or False for whether the person is an adult,meaning age 18 or more.

name = input("Enter your name: ")
birth_year = input("Enter your birth year: ")
current_year = 2026
age = current_year - int(birth_year) 
print(f"Hello {name.upper()}, you are {age} years old.")
print(age >=18)
