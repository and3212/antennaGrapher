#!usr/bin/env python3
# Author: Liam Lawrence
# Date: July 20, 2017
# Graphs data from antennas

import Parser as P
from Data import Data

# Variables that can be changed
offset = 100                        # Variable offset, good if you're working with -dBm
file1_Title = "Radiation Path"      # Title for the first file's data
file2_Title = "Shielded Box"        # Title for the second file's data

file1 = "../../res/data.csv"        # The main data file
file2 = "../../res/data2.csv"       # The compared data file


def doubleMenu():
    data1 = Data()
    data2 = Data()
    data1 = data1.fromFile(file1)
    data2 = data2.fromFile(file2)
    response = input("Azimuth or Elevation scan [A/e] ")

    # Parse an Elevation from 0 - 75 degrees
    if response.lower() == "e":  # If the response is an e or E
        angle = int(input("What angle would you like to scan [0/15/30/45/60/75] "))

        # Checks to see if anything is invalid
        if angle > 75 or angle % 15 != 0 or angle < 0:
            print("Invalid number, defaulting to 0")
            angle = 0
        # Parse the elevation
        P.elevationCompare(angle, data1, data2, offset, file1_Title, file2_Title)

    # Parse an Azimuth from -90 to 90
    else:
        angle = int(input("What angle would you like to scan [-90/-75/-60/-45/-30/-15/0/15/30/45/60/75/90] "))

        # Checks to see if anything is invalid
        if angle > 90 or angle % 15 != 0 or angle < -90:
            print("Invalid number, defaulting to 0")
            angle = 0
        # Parse the azimuth
        P.azimuthCompare(angle, data1, data2, offset, file1_Title, file2_Title)

def singleMenu():
    data = Data()
    data = data.fromFile(file1)
    response = input("Azimuth or Elevation scan [A/e] ")

    # Parse an Elevation from 0 - 75 degrees
    if response.lower() == "e":  # If the response is an e or E
        angle = int(input("What angle would you like to scan [0/15/30/45/60/75] "))

        # Checks to see if anything is invalid
        if angle > 75 or angle % 15 != 0 or angle < 0:
            print("Invalid number, defaulting to 0")
            angle = 0
        # Parse the elevation
        P.elevationParser(angle, data, offset, file1_Title)

    # Parse an Azimuth from -90 to 90
    else:
        angle = int(input("What angle would you like to scan [-90/-75/-60/-45/-30/-15/0/15/30/45/60/75/90] "))

        # Checks to see if anything is invalid
        if angle > 90 or angle % 15 != 0 or angle < -90:
            print("Invalid number, defaulting to 0")
            angle = 0
        # Parse the azimuth
        P.azimuthParser(angle, data, offset, file1_Title)

# Main method
def startMenu():
    response = input("Would you like to compare data [y/N] ")
    if response.lower() == "y":
        doubleMenu()
    else:
        singleMenu()

# Runs the program
startMenu()
