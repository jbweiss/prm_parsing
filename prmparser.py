__author__ = 'joeweiss'


import glob
import csv

#Set path to .prm files in relation to where you are running the python file.
path = './'

#Open and parse all the .prm files
for inFile in glob.glob1(path, '*.prm'):
    print 'Parsing File: ' + inFile
    parsedId = 'ID'
    description = 'Description'
    newType = 'Type'
    newEvent = 'Event'
    count = 0

    print 'File',',',parsedId,',', description,',', newType,',', newEvent

    file = open(inFile)
    for line in file:
        line = line.rstrip()

        if line.startswith('id'):
            words = line.split()
            id = words[0].split('=')
            parsedId = id[1]

        if line.startswith('name'):
            words = line.split("=")
            description = words[1]

        if line.startswith('log'):
            words = line.split()
            type = words[0].split(':')
            newType = type[1]

        if line.startswith('log'):
            words = line.split()
            event = words[1].split(':')
            newEvent = event[1]
            if parsedId == parsedId: count += 1

        if parsedId == parsedId and count >= 1:
            #resultFile = open('output.txt', 'wb')
            #resultFile.writelines(inFile + ',' + parsedId + ','+ description + ',' + newType + ',' + newEvent + '\n')
            #resultFile.close()

            print inFile,',',parsedId,',', description,',', newType,',', newEvent
            count = 0










