#!usr/bin/env python3
from Parser import *

# Variables that can be changed
offset = 100
filePath = "../../res/data.csv"
compareFile = "../../res/data2.csv"

def doubleMenu():
    data1 = Data()
    data2 = Data()
    data1 = data1.fromFile(filePath)
    data2 = data2.fromFile(compareFile)
    response = input("Azimuth or Elevation scan [A/e] ")

    # Parse an Elevation from 0 - 75 degrees
    if response.lower() == "e":  # If the response is an e or E
        angle = int(input("What angle would you like to scan [0/15/30/45/60/75] "))

        # Checks to see if anything is invalid
        if angle > 75 or angle % 15 != 0 or angle < 0:
            print("Invalid number, defaulting to 0")
            angle = 0
        # Parse the elevation
        elevationCompare(angle, data1, data2, offset)

    # Parse an Azimuth from -90 to 90
    else:
        angle = int(input("What angle would you like to scan [-90/-75/-60/-45/-30/-15/0/15/30/45/60/75/90] "))

        # Checks to see if anything is invalid
        if angle > 90 or angle % 15 != 0 or angle < -90:
            print("Invalid number, defaulting to 0")
            angle = 0
        # Parse the azimuth
        azimuthCompare(angle, data1, data2, offset)

def singleMenu():
    data = Data()
    data = data.fromFile(filePath)
    response = input("Azimuth or Elevation scan [A/e] ")

    # Parse an Elevation from 0 - 75 degrees
    if response.lower() == "e":  # If the response is an e or E
        angle = int(input("What angle would you like to scan [0/15/30/45/60/75] "))

        # Checks to see if anything is invalid
        if angle > 75 or angle % 15 != 0 or angle < 0:
            print("Invalid number, defaulting to 0")
            angle = 0
        # Parse the elevation
        elevationParser(angle, data, offset)

    # Parse an Azimuth from -90 to 90
    else:
        angle = int(input("What angle would you like to scan [-90/-75/-60/-45/-30/-15/0/15/30/45/60/75/90] "))

        # Checks to see if anything is invalid
        if angle > 90 or angle % 15 != 0 or angle < -90:
            print("Invalid number, defaulting to 0")
            angle = 0
        # Parse the azimuth
        azimuthParser(angle, data, offset)

# Main method
def startMenu():
    response = input("Would you like to compare data [N/y] ")
    if response.lower() == "y":
        singleMenu()
    else:
        doubleMenu()

# Runs the program
startMenu()
