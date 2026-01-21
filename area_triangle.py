#!/usr/bin/env python3
# Author: Angelo Garcia
# Date: December 1, 2025
# Description: Calculates the area of a triangle given its base and height.


def calc_area(base, height):
    area = 0.5 * base * height
    print(f"The area of the triangle is {area} square centimeters.")


def main():
    while True:
        try:
            base = float(input("Enter the base of the triangle in centimeters: "))
            height = float(input("Enter the height of the triangle in centimeters: "))
            calc_area(base, height)
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter numeric values for base and height.")


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
