#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program calculates the area of a triangle with functions


def calculate_area(base_as_string, height_as_string):
    # calculate temperature

    # output
    try:
        height = int(height_as_string)
        base = int(base_as_string)
        area = (base * height) / 2
        print("\nThe area is {} m² ".format(area))
    except Exception:
        print("\nInavald, input")
    finally:
        print("\nDone")


def main():
    # This function gets input

    # input
    height_as_string = input("Enter the base (m): ")
    base_as_string = input("\nEnter the height (m): ")

    # call functions
    calculate_area(base_as_string, height_as_string)


if __name__ == "__main__":
    main()
