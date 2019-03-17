import os
import csv
cand_total=0
total=0
votes=0
cnt=0
candidatesVotes={}
candidates=0
candidatesList=[]
data=[]
profit=[]
count=0
candidatesResults=''
maxvote=0
winner=0
outputFile="../resources/election_analysis.txt"
csv_path=os.path.join("..","resources","election_data.csv")
with open(csv_path,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        votes=votes  + 1
        candidates=row[2]
              
        if row[2] not in candidatesList:
            candidatesList.append(row[2])
            candidatesVotes[row[2]]=1
            
        else:
            candidatesVotes[row[2]]=candidatesVotes[row[2]] + 1
    
    print()
    print()
    print()
    print("Election Results")
    print("-------------------------------")
    print("Total Votes: "+ str(votes))
    print("-------------------------------")
    
 #Results
    for candidate in candidatesVotes:
        print(candidate+": "+str(round((candidatesVotes[candidate]/votes)*100)) +"%  ("+str(candidatesVotes[candidate])+")")
        candidatesResults+=(candidate+": "+str(round((candidatesVotes[candidate]/votes)*100)) +"%  ("+str(candidatesVotes[candidate])+")\n")
        if candidatesVotes[candidate] > maxvote:
            maxvote=candidatesVotes[candidate]
            winner=candidate
    print("-------------------------------")
    print ("Winner:"+ winner)
    print("-------------------------------")
    with open(outputFile,"w") as txtfile:
        txtfile.write("Election results\n")
        txtfile.write("-------------------------------\n")
        txtfile.write("Total Votes:  "+str(votes)+"\n")
        txtfile.write("-------------------------------\n")
        txtfile.write(candidatesResults)
        txtfile.write("-------------------------------\n")
        txtfile.write("Winner:"+ winner+"\n")
        txtfile.write("-------------------------------")