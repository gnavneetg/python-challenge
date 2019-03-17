import os
import csv
#Variables declarations 
count=0 #Month Counter
total=0 #Total Profit
max_month=0 # Month index with maxium profit
min_month=0 # Month index with minimum profit
profitChng=[] #List to store profit change
month=[]#Slice Months in a list
profit=[]#Slice Profit in a list
outputfile="budget_analysis.txt"
csv_path=os.path.join("..","resources","budget_data.csv")
with open(csv_path,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader) # skipping header from calculations
    first_row=False #Flag to pull starting Profit
    for row in csvreader:
        if first_row==False:
            first=row[1] #Capturing starting Profit
            first_row=True
        count=count + 1
        total += (float(row[1]))  #calculating total
        profit.append(int(row[1])) #Pulling profits in profit list
        month.append(row[0]) #Pulling monthyear in month list
    last_row=row[1] #Capturing Ending Profit
    total_month= count  # Total Months
    average=(int(last_row)-int(first))/(total_month -1) #Calculating Average
    for i in range(0,count): # Setting first element of profile change to zero
        if i==0 :
            profitChng.append(0)
        else:
            profitChng.append(profit[i] - profit[i-1]) #Calculating monthly profit change 
    max=max(profitChng) #Calculating greatest increase in Profit
    min=min(profitChng) #Calculating greatest decrease in Profit
    max_month=profitChng.index(max) #finding month index for greatest increase
    min_month=profitChng.index(min) #finding month index for greatest decrease
    month_max=month[max_month] #locating month with greatest increase
    month_min=month[min_month] #locating month with greatest decrease
    
#Printing on Terminal
    print("Financial Analysis")
    print("---------------------------")
    print ("Total Months: "+str(total_month))
    print("Total: $"+str(round(total)))
    print("Average  Change: $"+str(round(average,2)))
    print("Greatest Increase in Profits: "+ month_max+" ($"+ str(max)+")")
    print("Greatest Decrease in Profits: "+ month_min+" ($"+ str(min)+")")

# Printing in a Text File 
with open(outputfile,"w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write("Total Months: "+str(total_month)+"\n")
    txtfile.write("Total: $"+str(round(total))+"\n")
    txtfile.write("Average  Change: $"+str(round(average,2))+"\n")
    txtfile.write("Greatest Increase in Profits: "+ month_max+" ($"+ str(max)+")\n")    
    txtfile.write("Greatest Decrease in Profits: "+ month_min+" ($"+ str(min)+")\n")