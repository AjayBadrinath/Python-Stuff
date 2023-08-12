datafile = open('user.txt')
found = False
for line in datafile:
    if "dsa" in line:
        found = True
        break
print(found)
