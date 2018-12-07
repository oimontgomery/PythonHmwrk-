import os
import csv 

voter_ID = []
candidates = []
solo_candidates = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0
winner = []

file_path = os.path.join("election_data.csv")

with open(file_path, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

def addcandidates(voter_ID,candidates,solo_candidates,OTooley,Khan,Li,Correy):
	for row in csvreader:
		voter_ID.append(row[0])
		candidates.append(row[2])
		if row[2] == "O'Tooley":
			OTooley.append(row[0])
		elif row[2] == "Khan":
			Khan.append(row[0])
		elif row[2] == "Li":
			Li.append(row[0])
		elif row[2] == "Correy":
			Correy.append(row[0])

	for candidate in candidates:
		if candidate not in solo_candidates:
			solo_candidates.append(candidate)

def getpercentages(winner,voter_ID,solo_candidates):
	otooleypercentage = winner.append(round(len(OTooley)/len(voter_ID) * 100))
	khanpercentage = winner.append(round(len(Khan)/len(voter_ID) * 100))
	lipercentage = winner.append(round(len(Li)/len(voter_ID) * 100))
	correypercentage = winner.append(round(len(Correy)/len(voter_ID) * 100))

def exportresults():
	output.write("Election Results"+"\n")
	output.write("Total Votes: " + str(len(voter_ID))+"\n")
	output.write("O'Tooley: " + str(winner[0])+"%"+"\n")
	output.write("Khan: " + str(winner[1])+"%"+"\n")
	output.write("Li: " + str(winner[2])+"%"+"\n")
	output.write("Correy: " + str(winner[3])+"%"+"\n")
	output.write("Winner: " + solo_candidates[winner.index(max(winner))]+"\n")


def printresults():
	print("Election Results")
	print("Total Votes: " + str(len(voter_ID)))
	print("O'Tooley: " + str(winner[0])+"%")
	print("Khan: " + str(winner[1])+"%")
	print("Li: " + str(winner[2])+"%")
	print("Correy: " + str(winner[3])+"%")
	print("Winner: " + solo_candidates[winner.index(max(winner))])


	addcandidates(voter_ID,candidates,solo_candidates,OTooley,Khan,Li,Correy)
	getpercentages(winner,voter_ID,solo_candidates)
	printresults()


output_path = os.path.join("Final_Pypoll_output.text")

with open(output_path, 'a') as output: 
	exportresults()