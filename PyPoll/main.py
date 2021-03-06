import os
import csv
import random

#get path of file
csvPath = input('What is the path of the input file you want to use? ex: election_data_1.csv ')

#set up variables
rowCount = 0
candidate = 'Bob'
candidateStringArray = []
dummy = 0
candidateDictionary = {}
Winner = 'Bob'
mostSoFar = 0
candidateCounter = 0

#open data file
with open(csvPath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) #skip the headers

    #get total votes, candidates
    for row in csvreader:
        rowCount = rowCount + 1
        candidate = str(row[2])
        if(candidate in candidateDictionary):
            candidateDictionary[candidate][0] = candidateDictionary[candidate][0] + 1 #increase vote count for candidate
        else:
            candidateDictionary[candidate] = [0,0] 
            candidateDictionary[candidate][0] = 1 #add the candidate to the array

    #get percentage of votes candidate won
    for x in candidateDictionary:
        candidateDictionary[x][1] = ( ((candidateDictionary[x][0])/rowCount)*100)

    #find winner
    for x in candidateDictionary:
        if(candidateDictionary[x][1] > mostSoFar):
            mostSoFar = candidateDictionary[x][1]
            winner = x
        else:
            dummy = 0
            #do nothing


#set up print statements
line1 = "Election Results"
line2 = "-------------------------"
line3 = "Total Votes: " + str(rowCount)
line4 = "-------------------------"
for x in candidateDictionary:
    candidateStringArray.append(x + ": " + str(candidateDictionary[x][1])+ "% (" + str(candidateDictionary[x][0]) + ")" )

line5 = "-------------------------"
line6 = "Winner: " + winner
line7 = "-------------------------"


print(line1)
print(line2)
print(line3)
print(line4)
for x in candidateStringArray:
    print(x)
print(line5)
print(line6)
print(line7)


#export to text file within current directory
outputPath = 'theresNoWayYouHaveaFileWithThisName' + str(random.randint(0,1000)) + '.txt'
f = open(outputPath,'w')
f.write(line1 + "\n")
f.write(line2 + "\n")
f.write(line3+ "\n")
f.write(line4+ "\n")
for x in candidateStringArray:
    f.write(x + "\n")
f.write(line5+ "\n")
f.write(line6+ "\n")
f.write(line7+ "\n")
f.close()

