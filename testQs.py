#Task 1 currently it's 
per_user = {"Amy": {"INFO": 3, "ERROR": 4}, "Joyce": {"INFO": 0, "ERROR":1}, "Grace": {"INFO": 1, "ERROR":1}}

#need to try
per_user = {"Amy": [3, 4], "Joyce": [0, 1], "Grace": [1, 1]}

"""completed"""

#Task 2 currently it's
                if logUser not in perUser.keys():
                        perUser[logUser] = {}
                        perUser[logUser]["INFO"] = 0
                        perUser[logUser]["ERROR"] = 0
                perUser[logUser][logType] += 1

#need to try
                if type == "INFO":
                        try:
                                userCounts[username]["INFO"] += 1
                        except KeyError:
                                userCounts[username] = ["INFO", 1]

#or 
                        try:
                                userCounts[username] = [type, +1]
                        except KeyError:
                                userCounts[username] = [type, 1]


#Task 3 currently it's
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

#need to try
errors.insert(0, ('Error', 'Count'))

f = open(errorfile, 'w')
for error in errors:
        a,b = error
        f.write(str(a)+','+str(b)+'\n')
f.close()

f = open(userfile, 'w')
f.write("Username,INFO,ERROR\n")
for stats in per_user:
        a, b = stats
        f.write(str(a)+','+str(b["INFO"])+','+str(b["ERROR"])+'\n')

#Task 4 currently it's
result = re.search(r"ticky: ([A-Z]+) ([\w'#\[\]\s]*) \((.*)\)$", log)

#need to try
result = re.search(r"(ERROR|INFO) ([\w'#\[\]\s]*) \(([\w\.]*)\)", line) 

"""completed"""