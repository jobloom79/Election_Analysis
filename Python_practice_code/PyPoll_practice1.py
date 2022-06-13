import csv
import os

# Assign a variable for the file to load and the path............
# file_to_load = 'Resources/election_results.csv'
# file_to_load = os.path.join("Resources","election_results.csv")
# election_data = open(file_to_load, 'r')
# with open(file_to_load) as election_data:
#     print(election_data)
# Create a filename variable to an indirect path to the file...........
file_to_save = os.path.join("analysis", "election_analysis.txt")
# using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # txt_file.write("Hello World!")
    txt_file.write(
        "Counties in the Election"
        "\n-------------------------" 
        "\nArapahoe\nDenver\nJefferson"
        )    
# using the open() function with the "w" mode we will write data to the file.....................
# open(file_to_save, "w")
# use the open statement to open the file as a text file.........................
# outfile = open(file_to_save, "w")
#write some data to the file............
# outfile.write("Hello World!")
# Close the file................
# outfile.close

# To do: perform analysis

    # Total number of votes cast
    # A complete list of candidates who received votes
    # Total number of votes each candidate received
    # Percentage of votes each candidate won
    # The winner of the election based on popular vote
#Close the file
# election_data.close()
# Assign a variable for the file to load and the path............
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#initialize vote counter
total_votes = 0

# using the with statement open the file as a text file.
with open (file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Print each row in the csv file.
    headers = next(file_reader)
    for row in file_reader:
        # the long way to add a couter is number = number + 1
        total_votes += 1
print(f"{total_votes:,}")

# To do: perform analysis

    # Total number of votes cast
    # A complete list of candidates who received votes
    # Total number of votes each candidate received
    # Percentage of votes each candidate won
    # The winner of the election based on popular vote
#Close the file
# election_data.close()

