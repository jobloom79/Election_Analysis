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

#Add our Dependencies
from ast import NotIn
import csv
from operator import is_not
import os
from unicodedata import is_normalized
#dir(csv)
#import numbers

#file_to_load = 'Resources/election_results.csv'
#election_data = open(file_to_load, 'r')
#election_data.close()

# Open the election results and read the file
#with open(file_to_load) as election_data:
#   print(election_data)

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


# #use the with statement and open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    #write some data to the file.
    #txt_file.write("Hello again")
    #txt_file.write("Counties in the Election")
    #txt_file.write("\n---------------------------")
    #txt_file.write("\nArapahoe\nDenver\nJefferson")

#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save a file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#Add the total vote counter
total_votes = 0

#Open the election results and read the file
#with open(file_to_load) as election_data:

#3.5.2.1. Declare a new list candidate options 
candidate_options = []
#3.5.3.1. Declare a new dictionary.
candidate_votes = {}

with open(file_to_load) as election_data:    
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the csv file
    for row in file_reader:
        #3.5.2.2. Print the candidates name from each list we iterate
        candidate_name = row[2]
        #3.5.2.3. Increment total votes by 1 after for loop
        total_votes += 1

        if candidate_name not in candidate_options:
            #3.5.2.4. Add the candidate name to candidate options using the 
            #append() method
            candidate_options.append(candidate_name)
            #3.5.3. Begin trackign that candidates vote count.
            candidate_votes[candidate_name] = 0
            
#print the candidate list.
print(candidate_votes)
    
#file_to_test = os.path.join("analysis","election_test.txt")
#with open(file_to_test, "w") as txt_file:
    #txt_file.write("Hello for the 3rd time")

    
