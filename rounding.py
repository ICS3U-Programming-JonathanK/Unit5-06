#!/usr/bin/env python3

# Created by : Jonathan Kene
# Created on : June 9 2021
# This program prints out your address, using default function parameters
# This program rounds a decimal to the number of a decimal places entered


def round_decimals(decimal_num, num_places):

    # function adds 1, by reference
    decimal_num[0] = decimal_num[0]*(10**num_places)
    decimal_num[0] = decimal_num[0] + 0.5
    decimal_num[0] = int(decimal_num[0])
    decimal_num[0] = decimal_num[0]/(10**num_places)


def main():
    # this function gets a number and calls the add_one function
    print("This program rounds a decimal "
          "to the number of a decimal places entered")
    user_decimal_num_string = input("Enter a decimal number: ")

    try:
        user_decimal_num_int = float(user_decimal_num_string)
        if (user_decimal_num_int <= 0):
            print("{} is not a "
                  "positive number". format(user_decimal_num_int))
    except ValueError:
        print("Please enter a valid number")
    else:
        user_num_places_string = input("Enter the number of decimal places: ")
        try:
            user_num_places_int = int(user_num_places_string)
            if (user_num_places_int <= 0):
                print("{} is not a "
                      "positive number". format(user_num_places_int))
        except ValueError:
            print("Please enter a valid number")
        else:
            decimal_num_list = []
            decimal_num_list.append(user_decimal_num_int)
            round_decimals(decimal_num_list, user_num_places_int)
            print("{} rounded to {} "
                  "decimals is: {}". format(user_decimal_num_int, user_num_places_int, decimal_num_list[0]))

if __name__ == "__main__":
    main()
