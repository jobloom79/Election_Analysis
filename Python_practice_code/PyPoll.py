import csv
import os

# Assign a variable for the file to load and the path............
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# using the with statement open the file as a text file.
with open (file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print each row in the csv file.
    headers = next(file_reader)
    print(headers)
# To do: perform analysis

    # Total number of votes cast
    # A complete list of candidates who received votes
    # Total number of votes each candidate received
    # Percentage of votes each candidate won
    # The winner of the election based on popular vote
#Close the file
# election_data.close()

