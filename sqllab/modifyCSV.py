import csv
import math

def extractHeader(dict):

    header = []

    for row in dict[0]:
        header += [row]

    return header

if __name__ == "__main__":
    with open('earthquakeData.csv') as earthquakeData:
        extractedData = csv.DictReader(earthquakeData)

        print(extractHeader(extractedData));


## password for server access: pies967beach