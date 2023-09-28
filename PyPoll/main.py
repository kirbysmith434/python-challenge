import csv
import os

# Variables
total_votes = 0
candidates = {}
winner = None


# Get the current working directory
current_directory = os.getcwd()

# Construct the relative path to the CSV file
csvpath = os.path.join("Resources", "election_data.csv")

# Define the relative path to the output directory within the analysis directory
output_directory = os.path.join("Analysis")

# Create an output directory if it doesn't exist already
os.makedirs(output_directory, exist_ok=True)

# Define the relative path to the output file within the analysis directory
output_file = os.path.join(output_directory, "election_results.txt")

# Rest of your code remains the same
# Opens CSV file
with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    # Loops through each row in the CSV file
    for row in reader:
         # Extracting the candidate information
        _, _, candidate = row
        total_votes += 1
        # Tallys up the votes
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1
# Determines the winner
winner = max(candidates, key=candidates.get)
# Displays the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Display a message indicating the results have been saved
print(f"Election results have been saved to '{output_file}'")
