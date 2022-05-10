#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that calculates circumference using constants

def main():

    # Input
    radius = int(input("Enter Radius of Circle in mm: "))

    # Process
    circumference = radius * constants.TAU

    # Output
    print("The circumference would be {0} mm.".format(circumference))

    print("\nDone.")


if __name__ == "__main__":
    main()
