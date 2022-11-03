import os
os.system("cls") 

'''
#----------TASK-1----------
'''

#creating roll number list
roll_list=[]
with open("regtable_old.csv", "r") as f:
    for row in f:
        if row.split(',')[0] not in roll_list:
            roll_list.append(row.split(',')[0])
del roll_list[0]

#extracting required information
master_list=[]
with open("regtable_old.csv", "r") as f:
    for row in f:
        row_l=row.split(",")
        master_list.append([row_l[0], row_l[1], row_l[3], row_l[8]])
del master_list[0]

#making final list
rollr=[]
for roll in roll_list:
    rollc=[]
    for row in master_list:
        if(roll==row[0]):
            rollc.append(row)
    rollr.append(rollc)

#created header
topline="rollno,register_sem,subno,sub type\n"
top_list=list(topline.split(','))

#progressing to create individual files as per 'roll_list list
for i in range(len(roll_list)):
    with open("output_individual_roll\\" + roll_list[i] + ".csv", "w") as f:
        f.write(topline)
        for part in rollr[i]:
            part=','.join(part)
            f.writelines(part)  

'''
----------TASK-2----------
'''

#creating subject list
sub_list=[]
with open("regtable_old.csv", "r") as f:
    for row in f:
        if row.split(',')[3] not in sub_list:
            sub_list.append(row.split(',')[3])
del sub_list[0]

#making final list
subr=[]
for sub in sub_list:
    subc=[]
    for row in master_list:
        if(sub==row[2]):
            subc.append(row)
    subr.append(subc)

#progressing to create individual files as per 'sub_list' list
for i in range(len(sub_list)):
    with open("output_by_subject\\" + sub_list[i] + ".csv", "w") as f:
        f.write(topline)
        for part in subr[i]:
            part=','.join(part)
            f.writelines(part) 