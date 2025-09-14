# 🔹 1. if Statement

# Used to check a condition.
# If the condition is True, the block of code runs.

x = 10

if x > 5:   # condition check
    print("x is greater than 5")



# 🔹 2. if ... else Statement
# else runs when the if condition is False.


x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


# 🔹 3. if ... elif ... else
# elif means else if.
# Used when we want to check multiple conditions.

x = 5

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")



# 🔹 4. Nested if
# You can put one if inside another. 

x = 15

if x > 0:
    if x % 2 == 0:
        print("x is a positive even number")
    else:
        print("x is a positive odd number")


age = 18
msg = "Adult" if age >= 18 else "Not Adult"
print(msg)




day = "Mon"

match day:
    case "Mon":
        print("Start of week")
    case "Sun":
        print("Weekend")
    case _:
        print("Normal day")



# vote condition
age = 20
citizenship = "Indian" 

if age >= 18:
         print("Eligible to vote")

         if citizenship == "Indian":
                print("Eligible to vote in India")
         else:
                print("Not eligible to vote in India")
else: 
     print("you are a minor.")



#  🔹 Example 3: Multiple Nesting    

username = "admin"
password = "1234"
role = "superadmin"

if username == "admin":
     if password == "1234":
          if role == "superadmin":
                print("Welcome superadmin!")
          else:
                print("Welcome admin!")
     else: 
          print("Incorrect password.")
else: 
     print("User not found.")



day = "Sunday"
holiday = True

if day == "Sunday" or holiday:
    print("You can relax today!")
else:
    print("You have to go to work.")




temperature = 40

if temperature > 40:
    print("It's too hot!")
elif temperature > 25 and temperature <= 40:
    print("It's a warm day.")
elif temperature >= 15 and temperature <= 25:
    print("It's a pleasant day.")
else:
    print("It's cold outside.")


person_age = 88

if person_age >= 18 and person_age <= 60:
     print("you can drive")
elif person_age < 18:
     print("you are a young.")
else:
     print("You can drive but drive carefully.")
