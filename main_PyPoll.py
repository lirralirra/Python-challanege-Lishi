import pandas as pd

# Load the election data
election_data = pd.read_csv('Resources/election_data.csv')

# Calculate the total number of votes cast
total_votes = election_data['Voter ID'].count()

# Get a complete list of candidates who received votes
candidates = election_data['Candidate'].unique()

# Calculate total votes for each candidate
candidate_votes = election_data['Candidate'].value_counts()

# Calculate the percentage of votes each candidate won
candidate_percentage = (candidate_votes / total_votes) * 100

# Determine the winner of the election based on popular vote
winner = candidate_votes.idxmax()

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print("Candidates and Votes:")
for candidate in candidates:
    print(f"{candidate}: {candidate_votes[candidate]} votes ({candidate_percentage[candidate]:.2f}%)")
print("-------------------------")
print(f"Winner: {winner}")