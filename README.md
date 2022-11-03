This document summarises the purpose and work done on the added projects.

_____________________________________________________________________________________________________________________________________________________________

1. ACADEMIC SUBJECT RECORD

The aim is to form files of two forms: a) of individual subjects containing the information of all the students enrolled in that course; b) of individual
students containing all of the subjects taken by him/her.

This is done by simply using file reading and writing tools.

The input file given here is 'regtable_old.csv' which contains all of the information of students and courses taken by them for a particular semester. This
information is used to make the above-mentioned files.
_____________________________________________________________________________________________________________________________________________________________

2. ACADEMIC SUBJECT RECORD WITH EXCEL RECORD

The aim is to form files of two forms: a) of individual subjects containing the information of all the students enrolled in that course; b) of individual
students containing all of the subjects taken by him/her.

This has been achieved by using the libraries: CSV and OPENPYXL, refraining from the use of PANDAS for this case.

The input file given here is 'regtable_old.csv' which contains all of the information of students and courses taken by them for a particular semester. This
information is used to make the above-mentioned files.
_____________________________________________________________________________________________________________________________________________________________

3. GUI-BASED MARK SHEET GENERATOR

When the quiz is conducted on Google Forms, Google does not provide an option for computing -ve marking. It gives 0 marks for the wrong answer. It just 
gives a .csv file as output for post-processing. This project provides the facility to incorporate the negative marking system, such that we input the
.csv file, the positive marks on correct marking the right answer, and the negative marks on marking the wrong one in the GUI. It then generates roll 
number-wise marksheets which can be mailed to the respective student. Along with that a concise excel sheet is generated with the positive, negative 
marks and total marks of every student in it. 

This is achieved by using the libraries: STREAMLIT, OPENPYXL and CSV. The facility of mailing the marksheets is provided by using the EMAIL library

The input file given in here are two files: the response file of students and their information file.
_____________________________________________________________________________________________________________________________________________________________

4. GUI Based Transcript Generator

