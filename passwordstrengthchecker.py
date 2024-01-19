
#minimum 8 characters 
#include symbols and uppercase/lower case, digits.

import re

def password_checker(password):
    password_len = len(password)
    for i in password:
        if i == " ":
            return "No spaces allowed"
    upper = bool(re.search("[A-Z]", password))
    lower = bool(re.search("[a-z]", password))
    digits = bool(re.search("[0-9]", password))
    symbols = bool(re.search("[! , @ # $ % ^ & * .]", password))
    if upper and lower and digits and symbols and password_len >=8:
        return "Strong password"
    else:
        return "Enter a strong password"
    

#Main

password = input("Enter your password to check the strength: ")
print(password_checker(password))