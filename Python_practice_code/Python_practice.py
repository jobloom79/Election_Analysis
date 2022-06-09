# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# if "El Paso" in counties:
#     print("El Paso is in th elist of counties.")
# else:
#     print("El Paso is not in the list of counties.")

# for county in counties:
    # print(county)

# numbers = [0,1,2,3,4]
# for num in numbers:
#     print(num)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

# counties_dict = {"Arapahoe":422829,"Denver": 463353, "Jefferson": 432438}


# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")
#     # print(county, voters)
#     # print the statement for registered voters in each county
#     print(county + " county has " + str(voters) + " registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters":422829},
#                 {"county":"Denver", "registered_voters":463353},
#                 {"county":"Jefferson", "registered_voters":432438}]
            
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# for i in range(len(voting_data)):
#     print(voting_data[i]["county"])
# for county_dict in voting_data:
#     print(county_dict["registered_voters"])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# message_to_candidate = (
#     f"You received {my_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {percentage_votes:.2f}% of the total votes. "
# )
# print(message_to_candidate)


# print(f"I received {[percentage_votes]}% of the total votes.")