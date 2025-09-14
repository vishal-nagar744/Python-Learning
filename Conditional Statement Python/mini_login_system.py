# Mini Login System

# Predefined credentials
correct_username = "admin"
correct_password = "1234"

# User se input lena 
username = input("Enter your username: ")
password = input("Enter your password: ")

# check conditions
if username == correct_username and password == correct_password:
     print("Login successful!", username)
elif username == correct_username and password != correct_password:
     print("Incorrect password. Please try again.")
elif username != correct_username and password == correct_password:
     print("Incorrect username. Please try again.")
else: 
     print("Both username and password are incorrect. Please try again.")     