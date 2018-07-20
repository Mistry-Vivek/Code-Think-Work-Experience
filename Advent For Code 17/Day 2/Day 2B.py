#Import CSV.
import csv

#Opening 
with open("2.csv","r") as csvFile:
    sum = 0
    reader = csv.reader(csvFile,delimiter='\t',)
    int_columm = 0
    
    for row in reader:
        print(row)
        list_num = []
        row_int = map(int,row)
        for value in row_int:
            for x in row_int:
                if not (value == x):               
                    if value % x == 0:
                        to_add = value/x
                        print("")
                        sum += (value/x)   
print(sum)
        

        
        

