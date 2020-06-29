#!/usr/bin/env python3
import re
import csv
import operator
import sys

#This is Task 1, use a list instead of dictionary as value in the per_user dictionary.
#test0: per_user = {"Amy": {"INFO": 3, "ERROR": 4}, "Joyce": {"INFO": 0, "ERROR":1}, "Grace": {"INFO": 1, "ERROR":1}}
#test1: per_user = {"Amy": [3, 4], "Joyce": [0, 1], "Grace": [1, 1]}

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