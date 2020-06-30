#!/usr/bin/env python3
import re
import csv
import operator
import sys

#This is Task 2, use try-except instead of not-in to initialise a new error or user record.
#part a: apply in the settings of dictionary in a dictionary (test0)
#test0: 
# if logUser not in perUser.keys(): 
#   perUser[logUser] = {} 
#   perUser[logUser]["INFO"] = 0 
#   perUser[logUser]["ERROR"] = 0 
# perUser[logUser][logType] += 1
#test2a: 
# if type == "INFO": 
#   try: 
#       userCounts[username]["INFO"] += 1 
#   except KeyError:
#       userCounts[username] = ["INFO", 1]

perUser = {}
errors = {}

logFile = "syslog.log"
file = open(logFile, "r")

errorFile = "error_message.csv"
userFile = "user_statistics.csv"

for log in file:
        result = re.search(r"ticky: ([A-Z]+) ([\w'#\[\]\s]*) \((.*)\)$", log)
        if result:
                logType = result.group(1)
                logMsg = result.group(2)
                logUser = result.group(3)

                if logUser not in perUser.keys():
                        perUser[logUser] = {}
                        perUser[logUser]["INFO"] = 0
                        perUser[logUser]["ERROR"] = 0
                perUser[logUser][logType] += 1

                if logType == "ERROR":
                        if logMsg not in errors.keys():
                                errors[logMsg] = 0
                        errors[logMsg] += 1

        sortedErrors = sorted(errors.items(), key = operator.itemgetter(1), reverse = True)
        sortedPerUser = sorted(perUser.items(), key = operator.itemgetter(0))

file.close()

with open(errorFile, "w") as em:
        emw = csv.writer(em)
        emw.writerow(["Error", "Count"])
        for error in sortedErrors:
                emw.writerow(error)

with open(userFile, "w") as us:
        us.write("Username,INFO,ERROR\n")
        for user in sortedPerUser:
                a,b = user
                us.write(str(a)+","+str(b["INFO"])+","+str(b["ERROR"])+"\n")