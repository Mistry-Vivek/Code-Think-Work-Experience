#Import CSV.
import csv

#Opening 
with open("2.csv","r") as csvFile:
    sum = 0
    reader = csv.reader(csvFile,delimiter='\t',)

    for columm in reader:
        print(columm)
        int_columm = map(int,columm)
        to_add = max(int_columm) - min(int_columm)
        print (to_add)

        sum += to_add
print(sum)
        

        
        
