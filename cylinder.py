# Created by Ethan Prieur
# Created on May 2022
# This program calculates the volume of a cylinder

import math


def cylinder_volume(radius, height):
    # Calculates Grade Level

    volume = math.pi * height * (radius**2)

    return volume


def main():
    # This is the main function

    # Input
    radius_as_string = input("Enter the Radius: ")
    height_as_string = input("Enter the Height: ")
    print("")

    try:
        radius_as_float = float(radius_as_string)
        height_as_float = float(height_as_string)
        # Call Functions
        volume = cylinder_volume(radius_as_float, height_as_float)
        volume = round(volume, 2)
        # Output
        print("The volume of the cylinder is {0} cm³".format(volume))
    except Exception:
        print("Invalid Input, Try Again")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()
