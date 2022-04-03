#Add our Dependencies
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save a file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#Add the total vote counter
total_votes = 0

#3.5.2.1. Declare a new list candidate options 
candidate_options = []
#3.5.3.1. Declare a new dictionary.
candidate_votes = {}
#3.5.5.1 Declare winning variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:    
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Read the header row.
    headers = next(file_reader)
    #Print each row in the csv file
    for row in file_reader:
        #3.5.2.3. Increment total votes by 1 after for loop
        total_votes += 1
        #3.5.2.2. Print the candidates name from each list we iterate
        candidate_name = row[2]
        #3.5.2 the candidate list              
        if candidate_name not in candidate_options:
            #3.5.2.4. Add the candidate name to candidate options using the 
            #append() method
            candidate_options.append(candidate_name)
            #3.5.3. Begin trackign that candidates vote count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidates count.
        candidate_votes[candidate_name] +=1
        #Print the final vote count to the terminal.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes:{total_votes:,}\n" 
        f"------------------------------\n"
        )
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)

#3.5.4.1. iterate through candidate list
    for candidate_name in candidate_votes:
        #3.5.4.2. iterate through candidate votes
        votes = candidate_votes[candidate_name]
        #3.5.4.3. clculate percentage of the vote count
        vote_percentage = float(votes) / float(total_votes) * 100
        #print each candiate, vote count, and percentage
        
        #3.5.5.1 check if the first vote is greater than zero 
        if votes > (winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
        candidates_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidates_results)
        #Save the candidate results to our text file.
        txt_file.write(candidates_results)
    #3.5.4..4. print each and candidate and the percentage of votes
    #using f-string    
    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------\n"
    )
    print(winning_candidate_summary)
    #Save the winning candidate's result to the text file
    txt_file.write(winning_candidate_summary)