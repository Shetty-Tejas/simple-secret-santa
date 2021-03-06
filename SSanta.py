import numpy, re

try:
    fHandle = open(input("Enter the file with names of the people separated by a new line.\n-> "))
except:
    print("Error found! Exiting!")
    exit()

# Declaration
names = list()
secretSanta = list()

# Avoid duplication of names and keep names containing only english alphabets.
[names.append(x) for x in fHandle.read().splitlines() if x not in names and re.search("^[a-zA-Z]+ ?[a-zA-Z]+?$", x)] 
# random.shuffle has been deprecated since Python 3.9, hence using numpy to shuffle all the names.
numpy.random.shuffle(names)
# Total number of names stored in list
nameCount = len(names)
print("\nTotal number of people participating: " + str(nameCount) + "\n")

# A simple yet effective algorithm of assigning tuples of two people
# Here the already shuffled names will be run through a for loop.
# The person at index 0 will give a gift to the person at index 1 and so on.
# The person at the last index will give a gift to the person at index 0 to complete the gifting process.
for i in range(0, nameCount):
    if i == nameCount-1: (x, y) = (names[i], names[0])
    else: (x, y) = (names[i], names[i+1])
    secretSanta.append((x, y))

# Just a shuffle to make the results seem randomly arranged :P No need for this line though!
numpy.random.shuffle(secretSanta)

# Printing the values with some "style" XD
for item in secretSanta:
    x, y = item
    print(x + " will gift " + y)

