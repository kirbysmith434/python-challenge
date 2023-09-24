import csv
import os

csvpath = "Resources/election_data.csv"
output_directory = "/Users/kirbysmith/Desktop/module3challenge/python_challenge/PyPoll/Analysis"  # Path to the analysis directory

# Create an output directory if there isnt one already
os.makedirs(output_directory, exist_ok=True)

# Define the output file path within the analysis directory
output_file = os.path.join(output_directory, "election_results.txt")

# Variables
total_votes = 0
candidates = {}
winner = None

# Opens CSV file
with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skips the header data
    # Loops through each row in the CSV file
    for row in reader:
        # Get the candidate information
        _, _, candidate = row
        total_votes += 1
        # count the votes
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1
    # Figure out who is the winner
    winner = max(candidates, key=candidates.get)

# Create and write results to the output file in the analysis directory
with open(output_file, 'w') as f:  
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        f.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")

# Display a message indicating the results have been saved
print(f"Election results have been saved to '{output_file}'")
