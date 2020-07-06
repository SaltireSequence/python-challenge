# Importing required functions.
import os
import csv
import sys

# Creating lists to store values of each column in .csv
VoterID = []

# Dictionary to contain candidate as the key and votes are value
Candidates = {}

# Total Votes Counter
TotalVotes = 0

# dict to hold percentage values for each candidate, dependant on percentage of votes received.
PercentageOfVotes = {}


WinnerCounter = 0

# Variable to hold winner
Winner = ""

# Using os function to navigate to path and .csv file
ElectionDataFile = os.path.join('Resources', 'election_data.csv')

# with statement to set .csv parameters (delimiter etc and open using csvreader.)
with open(ElectionDataFile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # for loop to iterate through the csv file
    for row in csvreader:
        # adding to the TotalVotes counter, to store the 'Total Votes'
        TotalVotes = TotalVotes + 1

        # as we iterate through the rows of the .csv file, below we store the values of row 2 (Candidate) in
        # the Candidates variable
        Candidate = row[2]

        # this if statement asks that if an existing candidate whilst iterating, then add to that candidates totals
        # otherwise add the candidate to the Candidates dictionary with one vote.
        if Candidate in Candidates:
            Candidates[Candidate] = Candidates[Candidate] + 1
        # else statement to add 1 vote to the candidate
        else:
            Candidates[Candidate] = 1
    # for loop that iterates through the Candidates dictionary, calculates the % of votes for each candidate, then saves
    # those values in the PercentageOfVotes dictionary.
    for key, value in Candidates.items():
        PercentageOfVotes[key] = round((value/TotalVotes)*100, 2)

    # for loop that iterates through the keys in my Candidates dictionary and identifies the winner / candidate with
    # the most votes.
    for key in Candidates.keys():
        if Candidates[key] > WinnerCounter:
            Winner = key
            WinnerCounter = Candidates[key]

# using length function to find the total votes, using column 0 values, which we saved in VoteID variable.
print("")
print("Election Results\n----------------------------")
print("Total Votes: " + (str(TotalVotes)))
print("----------------------------")

# I'm sure there is a more eloquent way to do this but, this for loop iterates through each key in my Candidates
# dictionary and prints the key, percentage
for key, value in Candidates.items():
    print(key + ": " + str(PercentageOfVotes[key]) + "% " + "(" + str(value) + ")")

# printing data separator
print("----------------------------")
# printing a string of the Winnger / Candidate value
print("Winner: " + str(Winner))

# creating and setting file to write the below to.
OutputFile = open("ElectionResults.txt", "wt")
OutputFile.write("Election Results\n")
# writing data separator to text file
OutputFile.write("----------------------------\n")
OutputFile.write("Total Votes: " + (str(TotalVotes)) + '\n')
# writing data separator
OutputFile.write("----------------------------\n")

# Same for loop as with printing, however writing to file.
for key, value in Candidates.items():
    OutputFile.write(key + ": " + str(PercentageOfVotes[key]) + "% " + "(" + str(value) + ")\n")
OutputFile.write("----------------------------\n")

# writing a string of the Winnger / Candidate value to text file
OutputFile.write("Winner: " + str(Winner))