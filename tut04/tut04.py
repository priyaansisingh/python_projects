import csv
import os
os.system('cls')

#creating roll number and subject lists
roll_list=set()
sub_list=set()

with open("regtable_old.csv", "r") as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(type(row))
        roll_list.add(row[0])
        sub_list.add(row[3])

print(type(reader))    
roll_list.remove("rollno")
sub_list.remove("subno")

count_roll=len(roll_list)
count_sub=len(sub_list)

roll_list=list(roll_list)
sub_list=list(sub_list)

#creating topline
topline="rollno,register_sem,subno,sub type"
top_list=list(topline.split(','))

'''
#----------TASK(1)----------
'''

#creating files w.r.t. roll numbers
for i in range(count_roll):
    with open("output_individual_roll\\" + roll_list[i] + ".csv", "w", newline="") as f:
        writer=csv.writer(f)
        writer.writerow(top_list)
        with open("regtable_old.csv", "r") as csvfile:
             reader=csv.reader(csvfile)
             for row in reader:
                 if row[0]==roll_list[i]:
                     writer.writerow([row[0], row[1], row[3], row[8]])

'''
#----------TASK(2)----------
'''

#creating files w.r.t. subjects
for i in range(count_sub):
    with open("output_by_subject\\" + sub_list[i] + ".csv", "w", newline="") as f:
        writer=csv.writer(f)
        writer.writerow(top_list)
        with open("regtable_old.csv", "r") as csvfile:
             reader=csv.reader(csvfile)
             for row in reader:
                 if row[3]==sub_list[i]:
                     writer.writerow([row[0], row[1], row[3], row[8]])