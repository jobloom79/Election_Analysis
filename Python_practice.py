counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print (county + " has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print (f"{county} county has {voters} registered voters.")

candidates_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidates_votes:,} number of votes. "
    f" The total number of votes in the election was {total_votes:,}. "
    f" You received {candidates_votes / total_votes * 100:.2f}% of the total votes")

print(message_to_candidate)

for county, voters in counties_dict.items():
    print (f"{county} county has {voters:,} registered voters.")