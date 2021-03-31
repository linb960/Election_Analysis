# Add dependencies
import os
import csv
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize total vote counter
total_votes = 0
#Candidate options and votes
candidate_votes = {}
candidate_options = []
#Winning totals and candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header and move to the next row
    headers = next(file_reader)
    for row in file_reader:
        #Add the total votes
        total_votes += 1
        # Get the candidate name from each row
        candidate_name = row[2]
        #check to see if the candidate in not in the list of candidates and add
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #initialize the candidates votes
            candidate_votes[candidate_name] = 0
        #For each candidate found add a vote for them
        candidate_votes[candidate_name] += 1
for candidate_name in candidate_votes:
    #Retrieve the votes and the percentage and print the information
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 
    # find the winning vote count and the percentage
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
#Print the results to the terminal
winning_candidate_summary = (
    f"------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
)   
print(winning_candidate_summary)
