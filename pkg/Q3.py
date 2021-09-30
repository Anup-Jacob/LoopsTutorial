# ---------------------------------

# File          : Q3.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 30/09/2021
# Modified Date : 
# Description   : Write a Python program that accepts a string and calculate the number of digits, upper case letters and lower case letters
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

'''pseudocode
get a string from the user
loop
strings handout and find

check if it is upper, lower; check if in ascii range or  check python string functions
check if it isdigit'''

if __name__ == '__main__':

    digitcount = 0
    uppercount = 0
    lowercount = 0

    CharArray = input("Enter the String to be checked : ")
    # Input is taken from the user

    print(CharArray)
    arr = list(CharArray)

    ArrLen = len(CharArray)

    print("Length of the String is : {}".format(ArrLen))
    # Displays the length of the String entered by the user

    for i in range (0,ArrLen):
        # print(arr[i].isdigit())
        if arr[i].isdigit() == True:
            digitcount = digitcount + 1
        elif arr[i].isupper() == True:
            uppercount = uppercount + 1
        elif arr[i].islower() == True:
            lowercount = lowercount + 1

    print("Total number of digits in the String entered : {}".format(digitcount))
    # Displays the total number of digits in the String input from the user

    print("Total number of uppercase letters in the String entered : {}".format(uppercount))
    # Displays the total number of upper case letters in the String input from the user

    print("Total number of lowercase letters in the String entered : {}".format(lowercount))
    # Displays the total number of lower case letters in the String input from the user

    print("Thank you for using my character check application!!")



