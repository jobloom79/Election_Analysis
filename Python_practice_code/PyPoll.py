import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# using the with statement open the file as a text file.
with open (file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the csv file.
    headers = next(file_reader)
    
    for row in file_reader:
        # the long way to add a couter is number = number + 1
        total_votes += 1
        # print the candidate name for each row
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #begin tracking the canddiates vote count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

with open (file_to_save, "w") as txt_file:

    election_results = (
    f"\nElection Results\n"
    f"--------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"--------------------------\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)
        
    for candidate_name in candidate_votes:
        #retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        votes_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count) and (votes_percentage > winning_percentage):
            # if true then set the winning_count = votes and winning_perceentage = votes_percentage.
            winning_count = votes
            winning_percentage = votes_percentage
            winning_candidate = candidate_name

        # print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
    
        winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"--------------------------\n"
        )
        
        candidate_results = (f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        
    txt_file.write(winning_candidate_summary)


 

        

        


