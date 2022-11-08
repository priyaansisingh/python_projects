This document summarises the aim and work done on the added projects.

___________________________________________________________________________________________________________________________________________________________

1. GUI-BASED MARK SHEET GENERATOR

When the quiz is conducted on Google Forms, Google does not provide an option for computing -ve marking. It gives 0 marks for the wrong answer. It just 
gives a .csv file as output for post-processing. This project provides the facility to incorporate the negative marking system, such that we input the
.csv file, the positive marks on marking the right answer, and the negative marks on marking the wrong one in the GUI. It then generates roll 
number-wise mark sheets which can be mailed to the respective student. Along with that, a concise excel sheet is generated with the positive, and negative 
marks and the total marks of every student in it. 

This is achieved by using the libraries: STREAMLIT, OPENPYXL, and CSV. The facility of mailing the mark sheets is provided by using the EMAIL library.

The input file given in here is two files: the response file of students and their information file.
___________________________________________________________________________________________________________________________________________________________

2. GUI Based Transcript Generator

This project helps generate transcripts of the students, with information regarding all the subjects studies till date, their grades, the SPI of the 
semester, and the CPI.

The libraries used here are CSV, PANDAS, FPDF, and STREAMLIT.

The input files given here are the grades file (containing grades of all students in all subjects), name-roll number file, and subject information file.
___________________________________________________________________________________________________________________________________________________________

3. MARKSHEET GENERATOR

Here, we create a system that creates an Excel file of each student containing several semester-wise sheets which has information about the subjects 
and grades obtained by the student in that very semester. Also, an 'Overall' sheet is created which has the overall information about the SPI and CPI of 
the student.

The libraries used are CSV and OPENPYXL.

The input files given in here are two files: the response file of students and their information file.
