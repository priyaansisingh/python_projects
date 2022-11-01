'''
The sample output submitted is corresponding to the provided sample input in the question document.

SAMPLE INPUT:
Enter the number of the web series that you wish to rename. 1/2/3: 2
Enter the Season Number Padding: 1
Enter the Episode Number Padding: 2

The code can be applied for other cases.
'''

import os
import re
import shutil

def regex_renamer():

	# Taking input from the user

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))
	
	drama=['Breaking Bad', 'Game of Thrones', 'Lucifer']

	# Making folders for renamed files

	try:
		os.mkdir('corrected_srt')
	except:
		pass

	'''New Folder only for the considered folder in wrong_srt will be made in corrected_srt and will remain'''
	try:
		os.mkdir('corrected_srt\\'+drama[int(webseries_num)-1])
	except:
		pass

	path_input=os.path.join(r'wrong_srt', drama[int(webseries_num)-1])
	path_output=os.path.join(r'corrected_srt', drama[int(webseries_num)-1])

	# Deleting if any file is there in corrected_srt
	if os.listdir(path_output):
		for files in os.listdir(path_output):
			os.remove(path_output+'\\'+files)

	# The renaming procedure

	for episodes in os.listdir(path_input):
		old_ep=episodes[:]

		# Removing the common-unwanted strings
		if re.search(' 720p.BRrip.Sujaidr', episodes) or re.search('.WEB.REPACK.MEMENTO.en', episodes) or re.search('.HDTV.CAKES.en', episodes):
			episodes=re.sub(' 720p.BRrip.Sujaidr|.WEB.REPACK.MEMENTO.en|.HDTV.CAKES.en', '', episodes)
		
		# For drama 1
		pattern_d1=re.compile(r's\d\de\d\d') 
		if re.findall(pattern_d1, episodes):
			view=re.findall(pattern_d1, episodes)
			season=view[0][1:3].zfill(season_padding)
			episode=view[0][4:].zfill(episode_padding)
			episodes=re.sub('s\d\de\d\d', '- Season '+season+' Episode '+episode, episodes)
			shutil.copyfile(path_input+'\\'+old_ep, path_output+'\\'+episodes)

		# For drama 2 & 3
		pattern_d23=re.compile(r'\dx\d\d') 
		if re.findall(pattern_d23, episodes):
			view=re.findall(pattern_d23, episodes)
			season=view[0][0].zfill(season_padding)
			episode=view[0][2:].zfill(episode_padding)
			episodes=re.sub('\dx\d\d', 'Season '+season+' Episode '+episode, episodes)
			shutil.copyfile(path_input+'\\'+old_ep, path_output+'\\'+episodes)

regex_renamer()
print('Process Sucessful!')