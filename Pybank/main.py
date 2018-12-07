import os
import csv
 
net_budget_list = []
total_months = 0
number_months = []
total_net = 0 
avg_net = 0 
budget_change = 0 
prev_net = 0 
month_of_change = []


increase = ["", 0]
decrease = ["", 9999999999999999999]

csvpath = os.path.join("budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

def budgetdata(total_months,avg_net,increase,decrease):  
    for row in csvreader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        prev_net = int(row[1])
        budget_change = int(row[1]) - prev_net
        avg_net = (budget_change/total_months)
        net_budget_list = net_budget_list + [budget_change]
        month_of_change = month_of_change + [row[0]]
        if budget_change > increase[1]:
            increase[1] = row[0]
            increase[1] = net_change
        if budget_change < decrease[1]:
            decrease[1] = row[0]
            decrease[1] = budget_change

def printresults():
	print("Financial Analysis")
	print("Total months: " + str(len(total_months)))
	print("Total: " + str(len(total_net)))
	print("Average Change: " + str(len(avg_net)))
	print("Greatest Increase in Profits: " + str(len(increase)))
	print("Greatest Decrease in Profits: " + str(len(decrease)))


budgetdata(total_months,avg_net,increase,decrease)  
printresults()
output_path = os.path.join("Final_Pybank_output.text")

with open(output_path, 'a') as output: 
	exportresults()

