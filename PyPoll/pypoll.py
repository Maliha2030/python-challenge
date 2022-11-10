import os
import csv



electiondata_csv= os.path.join ('Resources', 'election_data.csv')
electionanalysis_txt=os.path.join('analysis','election_analysis.txt')

with open(electiondata_csv) as electiondata:
    reader=csv.reader(electiondata)
    # header=next(reader)
    firstrow=next(reader)

    # Create for loop
        # track total amount of votes
    count=0
    for row in reader:
        count+=1
    print(count)





lines = ['86','22564198','382539.0']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')