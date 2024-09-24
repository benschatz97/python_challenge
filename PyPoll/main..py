# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
INPUT_PATH = os.path.join("Resources", "election_data.csv")  
OUTPUT_PATH = os.path.join("analysis", "election_analysis.txt")  

# Initialize variables to track the election data
total_votes = 0 


# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}
candidates = []
# Winning Candidate and Winning Count Tracker
winning_votes = 0
winner=""

# Open the CSV file and process it
with open(INPUT_PATH, "r", encoding='UTF-8') as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes +=1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates: 
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] +=1

# Open a text file to save the output
with open(OUTPUT_PATH, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(total_votes)

    # Write the total vote count to the text file
    votes_output = (f"Election Results\n"
                    f"-----------------\n"
                    f"Total Votes:{total_votes}\n"
                    f"------------------\n")
    print(votes_output)
    txt_file.write(votes_output)
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidates:


        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        percentage_votes = float(votes)/float(total_votes) *100

        # Update the winning candidate if this one has more votes
        if votes > winning_votes:
            winning_votes = votes
            winner = candidate

        # Print and save each candidate's vote count and percentage
        candidate_output = f"{candidate}: {percentage_votes:.3f}% ({votes})\n" 
        print(candidate_output)
        txt_file.write(candidate_output)
    # Generate and print the winning candidate summary
    winner_output = (f"-----------------\n"
                    f"Winner: {winner}\n"
                    f"------------------")
    print(winner_output)
   
    # Save the winning candidate summary to the text file
    txt_file.write(winner_output)