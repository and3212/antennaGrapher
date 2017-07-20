#!usr/bin/env python
import numpy as np
from Data import Data
from GraphManager import graph

offset = 100
filePath = "../../res/data.csv"

def elevationParser(angle, data):
    validData = Data()
    print(validData.power)
    print("Using the following data points")
    print("| dBm | Azimuth | Elevation |")
    print("----------------------")

    for i in range(len(data.elevation)):
        if int(data.elevation[i]) == angle:
            validData.power.extend([float(data.power[i]) + offset])
            validData.azimuth.extend([float(data.azimuth[i]) * np.pi / 180])
            # validData.elevation.extend([float(data.elevation[i]) * np.pi / 180])
            print("|" + str(float(data.power[i])) + " | " + str(float(data.azimuth[i])) + " | " + str(float(data.elevation[i])) + "|")
    print("----------------------")
    graph(validData.azimuth, validData.power, angle, offset, "Elevation")

def azimuthParser(angle, data):
    validData = Data()
    print("Using the following data points")
    print("| dBm | Azimuth | Elevation |")
    print("----------------------")

    for i in range(len(data.azimuth)):
        if int(data.azimuth[i]) == angle:
            validData.power.extend([float(data.power[i]) + offset])
            # validData.azimuth.extend([float(data.azimuth[i])])
            validData.elevation.extend([float(data.elevation[i]) * np.pi / 180])
            print("|" + str(float(data.power[i])) + " | " + str(float(data.azimuth[i])) + " | " + str(float(data.elevation[i])) + "|")
    print("----------------------")
    graph(validData.elevation, validData.power, angle, offset, "Azimuth")

def startMenu():
    data = Data()
    data = data.fromFile(filePath)
    response = input("Azimuth or Elevation scan [A/e] ")

    # Parse an Elevation from 0 - 75 degrees
    if response.lower() == "e": # If the response is an e or E
        angle = int(input("What angle would you like to scan [0/15/30/45/60/75] "))

        # Checks to see if anything is invalid
        if angle > 75 or angle % 15 != 0 or angle < 0:
            print("Invalid number, defaulting to 0")
            angle = 0
        # Parse the elevation
        elevationParser(angle, data)

        # Parse an Azimuth from -90 to 90
    else:
        angle = int(input("What angle would you like to scan [-90/-75/-60/-45/-30/-15/0/15/30/45/60/75/90] "))

        # Checks to see if anything is invalid
        if angle > 90 or angle % 15 != 0 or angle < -90:
            print("Invalid number, defaulting to 0")
            angle = 0
        # Parse the azimuth
        azimuthParser(angle, data)


startMenu()
