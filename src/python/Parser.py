import numpy as np
from Data import Data
from GraphManager import graph
from GraphManager import compare

# Author: Liam Lawrence
# Date: July 27, 2017
# Parses through data and generates graphs based off of it

def elevationCompare(angle, data1, data2, offset):
    validData1 = Data()
    validData2 = Data()
    print("Using the following data points")
    print("| dBm | Azimuth | Elevation |")
    print("----------------------")

    # Finds the valid data and saves it
    for i in range(len(data1.elevation)):
        if int(data1.elevation[i]) == angle:
            validData1.power.extend([float(data1.power[i]) + offset])
            validData1.azimuth.extend([float(data1.azimuth[i]) * np.pi / 180])
            print("|" + str(float(data1.power[i])) + " | " + str(float(data1.azimuth[i])) + " | " + str(float(data1.elevation[i])) + "|")
    print("----------------------")
    for i in range(len(data2.elevation)):
        if int(data2.elevation[i]) == angle:
            validData2.power.extend([float(data2.power[i]) + offset])
            validData2.azimuth.extend([float(data2.azimuth[i]) * np.pi / 180])
            print("|" + str(float(data2.power[i])) + " | " + str(float(data2.azimuth[i])) + " | " + str(float(data2.elevation[i])) + "|")
    print("----------------------")
    compare(validData1.azimuth, validData2.azimuth, validData1.power, validData2.power, angle, offset, "Elevation")

def elevationParser(angle, data, offset):
    validData = Data()
    print("Using the following data points")
    print("| dBm | Azimuth | Elevation |")
    print("----------------------")

    # Finds the valid data and saves it
    for i in range(len(data.elevation)):
        if int(data.elevation[i]) == angle:
            validData.power.extend([float(data.power[i]) + offset])
            validData.azimuth.extend([float(data.azimuth[i]) * np.pi / 180])
            print("|" + str(float(data.power[i])) + " | " + str(float(data.azimuth[i])) + " | " + str(float(data.elevation[i])) + "|")
    print("----------------------")
    graph(validData.azimuth, validData.power, angle, offset, "Elevation")

def azimuthCompare(angle, data1, data2, offset):
    validData1 = Data()
    validData2 = Data()
    print("Using the following data points")
    print("| dBm | Azimuth | Elevation |")
    print("----------------------")

    # Finds the valid data and saves it
    for i in range(len(data1.azimuth)):
        if int(data1.azimuth[i]) == angle:
            validData1.power.extend([float(data1.power[i]) + offset])
            validData1.elevation.extend([float(data1.elevation[i]) * np.pi / 180])
            print("|" + str(float(data1.power[i])) + " | " + str(float(data1.azimuth[i])) + " | " + str(float(data1.elevation[i])) + "|")
    print("----------------------")
    for i in range(len(data2.azimuth)):
        if int(data2.azimuth[i]) == angle:
            validData2.power.extend([float(data2.power[i]) + offset])
            validData2.elevation.extend([float(data2.elevation[i]) * np.pi / 180])
            print("|" + str(float(data2.power[i])) + " | " + str(float(data2.azimuth[i])) + " | " + str(float(data2.elevation[i])) + "|")
    print("----------------------")
    compare(validData1.elevation, validData2.elevation, validData1.power, validData2.power, angle, offset, "Elevation")


def azimuthParser(angle, data, offset):
    validData = Data()
    print("Using the following data points")
    print("| dBm | Azimuth | Elevation |")
    print("----------------------")

    # Finds the valid data and saves it
    for i in range(len(data.azimuth)):
        if int(data.azimuth[i]) == angle:
            validData.power.extend([float(data.power[i]) + offset])
            validData.elevation.extend([float(data.elevation[i]) * np.pi / 180])
            print("|" + str(float(data.power[i])) + " | " + str(float(data.azimuth[i])) + " | " + str(float(data.elevation[i])) + "|")
    print("----------------------")
    graph(validData.elevation, validData.power, angle, offset, "Azimuth")
