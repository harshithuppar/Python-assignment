import string  


def check_password_strength(password):

    #Length
    length = len(password)
    if length < 8:
        return False
    
    #Uppercase
    if not any (char.isupper() for char in password):
        return False
    
    #Lowercase
    if not any(char.islower() for char in password):
        return False
    
    #Numeric
    if not any (char.isdigit() for char in password):
        return False
    
    #Special Character
    spl_char = tuple(string.punctuation)
    if not any (char in spl_char for char in password):
         return False

    return True 


#User input
user_password = input("Enter your password: ")

#Converting into list
password = list(user_password)


#print output of function
if check_password_strength(user_password):
        
    print("Password is strong. Good job!")

else:

    print("Password does not meet the criteria. Please choose a stronger password.")
