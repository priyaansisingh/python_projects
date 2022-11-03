import os
import re
import csv
from openpyxl import Workbook
#from openpyxl.workbook import workbook
import pandas as pd

def feedback_not_submitted():
  ltp_mapping_feedback_type = {1: 'lecture', 2: 'tutorial', 3:'practical'}
  output_file_name = "course_feedback_remaining.xlsx" 

  registered='course_registered_by_all_students.csv'
  feedback='course_feedback_submitted_by_students.csv'
  course_master='course_master_dont_open_in_excel.csv'
  student='studentinfo.csv'

  not_filled=[]
  not_filled_info=[]

  with open(student, 'r') as f:
    student_r=csv.reader(f)
    student_list=list(student_r)

    student_list.pop(0)
    rolls_stud=[]
    for students in student_list:
      rolls_stud.append(students[1])

  with open(feedback, 'r') as f:
    feedback_r=csv.reader(f)
    feedback_list=list(feedback_r)
    feedback_list.pop(0)

  with open(course_master, 'r') as f:
    course_master_r=csv.reader(f)
    course_master_list=list(course_master_r) #0:subno, 1:subname, 2:ltp, 3:crd
    course_master_list.pop(0)
    ltp_list=[]
    for items in course_master_list:
      ltp=items[2].split('-')
      ltp_list.append([items[0], ltp])

  total=[]
  with open(registered, 'r') as f:
    registered_r=csv.reader(f)
    registered_list=list(registered_r)
    registered_list.pop(0)
    i=0
    #iterating through this list
    for reg in registered_list:
      re.sub(r'\s"\s', '', reg[0])
      re.sub(r'\s"\s', '', reg[3])
      total.append(reg[0])
      for rows in ltp_list:
        if reg[3]==rows[0]:
          des=rows[1]
          break #found the ltp
      flag=0
      for feed in feedback_list:
        feed[5]=feed[5].strip()
        feed[4]=feed[4].strip()
        feed[3]=feed[3].strip()
        if(feed[3]==reg[0]):
          flag=1

        if ((feed[4]==reg[3]) and (feed[3]==reg[0])):
          des[int(feed[5])-1]='0'

      if not (des[0]=='0' and des[1]=='0'and des[2]=='0'):
        if (reg[0] in rolls_stud):
          for stud in student_list:
            if reg[0]==stud[1]:
              not_filled_info.append([reg[0], reg[1], reg[2], reg[3], stud[0], stud[8], stud[9], stud[10]])
        else:
          not_filled_info.append([reg[0], reg[1], reg[2], reg[3], 'NA', 'NA', 'NA', 'NA'])
          
        not_filled.append([reg[0], reg[3]])
      if(flag==0):
        if (reg[0] in rolls_stud):
          for stud in student_list:
            if reg[0]==stud[1]:
              not_filled_info.append([reg[0], reg[1], reg[2], reg[3], stud[0], stud[8], stud[9], stud[10]])
        else:
          not_filled_info.append([reg[0], reg[1], reg[2], reg[3], 'NA', 'NA', 'NA', 'NA'])


  file=Workbook()
  work=file.active

  header=['rollno', 'register_sem', 'schedule_sem', 'subno', 'Name', 'email', 'aemail', 'contact']
  work['A1']=header[0]
  work['B1']=header[1]
  work['C1']=header[2]
  work['D1']=header[3]
  work['E1']=header[4]
  work['F1']=header[5]
  work['G1']=header[6]
  work['H1']=header[7]

  for rows in not_filled_info:
    work.append(rows)
  
  file.save(output_file_name)

feedback_not_submitted()