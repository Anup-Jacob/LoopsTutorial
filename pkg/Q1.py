# ---------------------------------

# File          : 
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  :  
# Modified Date : 
# Description   :
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

'''
    loop
    print statement
    if statement
        print statement
        #pass; break; continue; -test each seperately
    elif statement
        print statement
    print statement
print statement
'''

x = int(input("Enter the number : "))

print(x)
while (x < 10):
    print("Inside the While loop.\n")
    if (x == 1):
        print("Inside the if loop with value 1.")
        pass; #Solution: skips the elif and prints the else
    elif (x == 0):
        print("Inside the if loop with value 0.")
        continue; # Solution: takes the same input and continues
    else:
        print("value of x is other than 0 or 1. Please check the value : {}".format(x))
        break; # Solution: Breaks out of the loop with the next iteration
    x = x + 1
    print("Completed while loop")

print("Completed the code as a whole")