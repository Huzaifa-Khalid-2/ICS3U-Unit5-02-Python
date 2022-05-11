#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program calculates the area of a triangle with functions


def calculate_area(base_as_int, height_as_int):
    # calculate area

    # output
    area = (base * height) / 2
    print("\nThe area is {} m² ".format(area))


def main():
    # This function gets input

    # input
    height_as_string = input("Enter the base (m): ")
    base_as_string = input("\nEnter the height (m): ")


    try:
        height_as_int = int(height_as_string)
        base_as_int = int(base_as_string)
        # call functions
        calculate_area(base_int, height_int)
    except Exception:
        print("\nInavald, input")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()
