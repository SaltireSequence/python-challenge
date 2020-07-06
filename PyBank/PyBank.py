# Importing dependencies
import csv
import os
import sys

# Empty lists to store budget dates and profit loss information
BudgetDates = []
ProfitLoss = []
AverageMonthlyRevenueChange = []

# path for budget data file
BudgetDataFile = os.path.join('Resources', 'budget_data.csv')

with open(BudgetDataFile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    monthcounter = 0
    for row in csvreader:
        BudgetDates.append(row[0])
        ProfitLoss.append(row[1])
        monthcounter += 1

# The total number of months included in the dataset
TotalMonths = len(BudgetDates)

# The net total amount of "Profit/Losses" over the entire period
TotalProfitLoss = 0
x = 0
for x in range(TotalMonths):
    TotalProfitLoss = TotalProfitLoss + int(ProfitLoss[x])

# The average of the changes in "Profit/Losses" over the entire period.
# (Firstly, finding monthly change in revenue)
y = 0
z = 0
for y in range(0, TotalMonths):
    if y == 0:
        AverageMonthlyRevenueChange.append(0)
    else:
        AverageMonthlyRevenueChange.append(int(ProfitLoss[y])-int(ProfitLoss[z]))
        z += 1

# The average of the changes in "Profit/Losses" over the entire period.
# (Now finding the actual average monthly change in profit / loss)
TotalAverageChange = 0
mc = 0
for mc in range(TotalMonths):
    TotalAverageChange = TotalAverageChange + int(AverageMonthlyRevenueChange[mc])
    AverageMonthlyChange = float(TotalAverageChange/float(TotalMonths-1))

# The greatest increase in profits (date and amount) over the entire period
GreatInvRevChange = max(AverageMonthlyRevenueChange)
GreatestIndex = AverageMonthlyRevenueChange.index(GreatInvRevChange)
GreatestIncDate = BudgetDates[GreatestIndex]

# The greatest decrease in losses (date and amount) over the entire period
GreatDecRevChange = min(AverageMonthlyRevenueChange)
LowestIndex = AverageMonthlyRevenueChange.index(GreatDecRevChange)
GreatestDecDate = BudgetDates[LowestIndex]

# The first tranche of print statements, prints all the required analysis to the console.
print("Financial Analysis\n----------------------------")
print("Total Months:", str(TotalMonths))
print("Total:","$" + str(TotalProfitLoss))
# I had an issue where my string would be to 10-decimal places. Couldn't work out why, so just force-rounded it
# using the round() function
print("Average Change:", "$" + str(round(AverageMonthlyChange, 2)))
print("Greatest Increase in Profits:", (str(GreatestIncDate) + " ($" + str(GreatInvRevChange) + ")"))
print("Greatest Increase in Profits:", (str(GreatestDecDate) + " ($" + str(GreatDecRevChange) + ")"))

# The second tranche of print statements, redirects them to a text file, using the 'sys.stdout' function. It seemed
# a lot more elegant and less time consuming, than repeating
sys.stdout = open('budget_analysis.txt', 'wt')
print("Financial Analysis\n----------------------------")
print("Total Months:", str(TotalMonths))
print("Total:","$" + str(TotalProfitLoss))
# I had an issue where my string would be to 10-decimal places. Couldn't work out why, so just force-rounded it
# using the round() function
print("Average Change:", "$" + str(round(AverageMonthlyChange, 2)))
print("Greatest Increase in Profits:", (str(GreatestIncDate) + " ($" + str(GreatInvRevChange) + ")"))
print("Greatest Increase in Profits:", (str(GreatestDecDate) + " ($" + str(GreatDecRevChange) + ")"))











