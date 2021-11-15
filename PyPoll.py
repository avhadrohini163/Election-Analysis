# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes
import csv

# Assign a variable for the file to load and the path.
file_to_load = "Resources/election_results.csv"
# Oen the election result and read the file.
election_data = open(file_to_load, "r")

# To do: perform analysis.
print(election_data)

# Close the file
election_data.close()

# using os.path.join

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election result and read the file.
with open(file_to_load) as election_data:
    # print the file object.
    print(election_data)

### Code to write into the file
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")
# Close the file
#outfile.close()
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World. ")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
    txt_file.write("\nCounties in the Election"
                   "\n------------------------------------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")



