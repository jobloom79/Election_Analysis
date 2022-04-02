# Overview of project
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

#Import the datetime class from the datetime module.
#import datetime
#Use the now() attribute on the datetime class to get the present time.
#now= datetime.datetime.now()
# Print the present line.
#print("The time right now is ", now)

#import csv
#dir(csv)
#import numbers

#file_to_load = 'Resources/election_results.csv'
#election_data = open(file_to_load, 'r')
#election_data.close()

# Open the election results and read the file
#with open(file_to_load) as election_data:
#   print(election_data)

import os
#file_to_load = os.path.join ("Resources","election_results.csv")
#with open(file_to_load) as election_data:
    #print(election_data)

#Create a filename variable to indirect path
#file_to_save = os.path.join("analysis","election_analysis.txt")
#Using the open function with w mode we will write data to the file
#open(file_to_save, "w")

#Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
#Write some data to the file
#outfile.write("Hello World")
#Close the file
#outfile.close()

#Create a variable to a direct or indirect path
file_to_save = os.path.join("analysis","election_analysis.txt")
#use the with statement and open the file as a text file.
with open(file_to_save, "w") as txt_file:
    #write some data to the file.
    txt_file.write("Hello again")
    
