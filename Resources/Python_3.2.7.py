counties_dict = {}
counties_dict["Arapahoe"] = 422829
# print(counties_dict)

counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

# print(counties_dict)

# Create the voting data list
# voting_data = []

# voting_data.append({"county":"Arapahoe","registered_voters":422829})
# voting_data.append({"county":"Denver","registered_voters":463353})
# voting_data.append({"county":"Jefferson","registered_voters":432438})

# voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
# voting_data.remove({"county":"Arapahoe","registered_voters":422829})
# voting_data.remove({"county":"Denver","registered_voters":463353})
# voting_data.append({"county":"Denver","registered_voters":463353})
# voting_data.append({"county":"Arapahoe","registered_voters":422829})

# print(voting_data)

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")


