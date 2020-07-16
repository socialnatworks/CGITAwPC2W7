#!/usr/bin/env python3
import re
import csv
import operator
import sys

#This is Task 2, use try-except instead of not-in to initialise a new error or user record.
#part b: apply in the settings of list in a dictionary (test1)
#test1: 
# if logUser not in perUser.keys():
#       perUser[logUser] = [0,0]
#       if logType == "INFO":
#               perUser[logUser][0] += 1
#       elif logType == "ERROR":
#               perUser[logUser][1] += 1
#               if logMsg not in errors.keys():
#                       errors[logMsg] = 0
#               errors[logMsg] += 1

#test2b: 
# if type == "INFO": 
#   try: 
#       userCounts[username][0] += 1 
#   except KeyError:
#       userCounts[username][0] = 1

perUser = {}
errors = {}

logFile = "syslog.log"
file = open(logFile, "r")

errorFile = "error_message.csv"
userFile = "user_statistics.csv"

for log in file:
        result = re.search(r"(ERROR|INFO) ([\w'#\[\]\s]*) \((.*)\)$", log)
        if result:
                logType = result.group(1)
                logMsg = result.group(2)
                logUser = result.group(3)
                n = 0 if logType == "INFO" else 1

                try:
                        perUser[logUser][n] += 1
                except KeyError:
                        if logUser not in perUser:
                                perUser[logUser] = {}
                        perUser[logUser][n] = 1
                
                if logType == "ERROR":
                        try:
                                errors[logMsg] += 1
                        except KeyError:
                                errors[logMsg] = 1                       
     
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