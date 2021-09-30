# ---------------------------------

# File          : odd_even_count.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 30/09/2021
# Modified Date : 
# Description   : A program to count the total number of odd and even numbers when a maximum value is given as input
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

if __name__ == '__main__':

    max = int(input("Enter the maximum number : "))
    # taking the input for maximum number into max variable

    count_even = 0
    count_odd = 0
    #initialising counts for even and odd as 0

    print(max)
    for i in range (1, max+1):
        if (max % 2 == 0):
            count_even = count_even + 1
            max = max - 1
        elif (max % 2 != 0):
            count_odd = count_odd + 1
            max = max -1

    print("The number of even numbers is : {}".format(count_even))
    print("The number of odd numbers is : {}".format(count_odd))
    # printing the counts to the screen
