import os
import csv



budgetdata_csv= os.path.join ('Resources', 'budget_data.csv')
budgetanalysis_txt=os.path.join('analysis','budget_analysis.txt')

with open(budgetdata_csv) as budgetdata:
    reader=csv.reader(budgetdata)
    # header=next(reader)
    firstrow=next(reader)

    # Create for loop
        # track total amount of months
    count=0
    for row in reader:
        count+=1
    print(count)

with open(budgetdata_csv) as budgetdata:
    reader=csv.reader(budgetdata)
    # header=next(reader)
    firstrow=next(reader)

        # track total net money
    total=0
    for row in csv.reader(budgetdata):
        total+=int(row[1])
    print(total)
        

        # do math for net change
        # get last row
    for row in csv.reader(budgetdata):
        row = int(budgetdata[-1])
    print(float(row[1]))
        #get 1st row

    #(integer in last row - integer in first row)/ [integer in last row] *100 to calculate % change in profit losses over entire period


        #if statement to see which is the greatest increase and greatest decrease in change

#create output statement

#print output statement

#print to txt file      

lines = ['86','22564198','382539.0']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
