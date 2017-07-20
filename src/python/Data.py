import csv

# Author: Liam Lawrence
# Date: July 20, 2017
# Reads in our CSV file and sorts it

class Data:
    def __init__(self):
        # Three columns from our CSV file
        self.power = []
        self.azimuth = []
        self.elevation = []

    # Reads in a file and sorts the data into the proper lists
    def fromFile(self, filePath):
        data = Data()
        firstPass = True

        # Read in our file and start storing it in dataList
        with open(filePath, 'rt') as f:
            # Skips the header
            if firstPass:
                next(f)
                firstPass = False

            # Starts reading in the file
            reader = csv.reader(f)
            dataList = list(reader)

        # Places our values in the proper lists
        for i in range(len(dataList)):
            data.power.extend([dataList[i][0]])
            data.azimuth.extend([dataList[i][1]])
            data.elevation.extend([dataList[i][2]])

        return data