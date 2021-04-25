#################### PLAN ##########################
# Leap Year determiner

# Takes in year from user

# Checks if divisible by 4 if not its not

# Checks if divisible by 100 if not it is

# Checks if divisible by 400 if not its not

# Ask if they would like to test another year

################# FUNCTIONS #########################


    
def whole_Number(x):
    # Means Whole number
    if (x - int(x) == 0):
        return True
    else:
        return False

###################### MAIN CODE #############################
while True:
    

    year = input("Enter the year you would like to test: ")

    # Main code
    while True:
        # Converts string year to an int
        year = int(year)
        # Checks if divisible by 4
        temp = year / 4.0
        if not whole_Number(temp):
            print("NOT A LEAP YEAR")
            break

        # Checks if divisible by 100
        temp = year / 100.0
        if not whole_Number(temp):
            print("LEAP YEAR")
            break
        # Checks if divisible by 400
        temp = year / 400.0
        if not whole_Number(temp):
            print("NOT A LEAP YEAR")
            break
    

    # Replay option
    user = input("Would you like to test again?(y/n): ")
    if user != "y":
        break
