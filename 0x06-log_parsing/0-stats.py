#!/usr/bin/python3
import sys


def formatPrint(size, myDict):
    print("File size: ", size)
    for key, value in statusDict.items():
        print("{}: {}".format(key, value))


if __name__ == "__main__":
    statusList = [200, 301, 400, 401, 403, 404, 405, 500]
    statusDict = {}
    size = 0
    i = 0
    try:
        for line in sys.stdin:
            i += 1
            lineList = line.split()
            statusCode = int(lineList[-2])
            size = size + int(lineList[-1])
            if statusCode in statusList:
                try:
                    statusDict[statusCode] += 1
                except KeyError:
                    statusDict[statusCode] = 1
            if i % 10 == 0:
                formatPrint(size, statusDict)
        formatPrint(size, statusDict)
    except KeyboardInterrupt:
        formatPrint(size, statusDict)
        raise
