import pandas as pd
import os

#check the working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Load the election data
election_data = pd.read_csv('Resources/election_data.csv')

# Calculate the total number of votes cast
total_votes = election_data['Ballot ID'].count()

# Get a complete list of candidates who received votes
candidates = election_data['Candidate'].unique()

# Calculate total votes for each candidate
candidate_votes = election_data['Candidate'].value_counts()

# Calculate the percentage of votes each candidate won
candidate_percentage = (candidate_votes / total_votes) * 100

# Determine the winner of the election based on popular vote
winner = candidate_votes.idxmax()

# Prepare the results
output = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------",
    "Candidates and Votes:"
]

for candidate in candidates:
    output.append(f"{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_votes[candidate]} votes) ")

output.extend([
    "-------------------------",
    f"Winner: {winner}",
    "-------------------------"
])

# Print the results to the terminal
for line in output:
    print(line)

# Write results to a text file in the Analysis folder
output_path = os.path.join('Analysis', 'ByPoll_analysis_result.txt')

with open(output_path, 'w') as file:
    for line in output:
        file.write(line + '\n')

print(f"\nResults have been written to {output_path}")
