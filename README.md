# Election_Analysis

## Project Overview of Election Audit
A Colorado Board of Elections employee has requested a election audit of a recent local congressional election.  He has specified the information he would like to obtain from the raw data he is providing and it is as follows:

1. The total number of votes cast.
2. The counties that participated in the election with the percentage of votes cast in each county and the total number of votes cast in each county
3. The county that had the greatest voter turnout
4. The complete list of candidates who received votes.
5. The total number of votes each candidate received.
6. The percentage of votes each candidate won.
7. The winner of the election based on popular vote.

The [code for this project](https://github.com/linb960/Election_Analysis/blob/main/PyPoll_Challenge.py) was written in python.  To calculate total number of votes for candidates, counties and overall, counters are used.  The candidates and counties are stored in lists and the totals collected for the each county and each candidate is stored in a dictionary as key, value pairs.

## Resources
- Data Source: [election_results.csv](https://github.com/linb960/Election_Analysis/blob/main/Resources/election_results.csv).  This data consists of 369,712 rows of data, with the header row being __Ballot County Candidate__.  

## Election Audit Results
The Colorado Board of Elections employee wants to get the output in two forms.  One at the terminal and the other in a text file.  After running the python program the results can be seen in the two sections below:

### Terminal Output
![The terminal output for the results](https://github.com/linb960/Election_Analysis/blob/main/analysis/election_analysis_terminal.png)

### Text file Output
[The text file output for the results](https://github.com/linb960/Election_Analysis/blob/main/analysis/election_analysis.txt)

![Screenshot of output from textfile](https://github.com/linb960/Election_Analysis/blob/main/analysis/election_analysis_txt_screenshot.png)

## Election Audit Summary
To do the analysis of the set of data provided by the Colorado Board of Elections employee a primary loop was created to read each row of the data.  The collection of the data into lists and dictionaries made it easier to output the information for the results.  For example with a candidate:
```
if candidate_name not in candidate_options:
    # Add the candidate name to the candidate list.
    candidate_options.append(candidate_name)

    # And begin tracking that candidate's voter count.
    candidate_votes[candidate_name] = 0

# Add a vote to that candidate's count
candidate_votes[candidate_name] += 1
```
The code checks if the candidate exists in the list of candidate_options and adds the candidate to the list if not and then initializes the candidate_votes for the candidate in the dictionary.  Once the candidate information is initialized then each iteration of the loop adds one to the count for the candidate found.

This is the same for the county tabulations.  Once all the rows in the raw data is read the resulting information is output to the text file and the terminal.

### Make the code Reusable
This code could be reused on any set of voter data that has three columns of information, a ballot id number, a county and a candidate.  

But this code has it's limitations. 

#### Example #1
It's rare that an election has just one government vacancy to fill.  Most elections have several seats to fill and each seat might have several candidates.  For example a ballot may contain two or more seats on it. For example if there was a County Supervisor and a County Clerk each may have several people running for the seat. So in the csv file maybe the selections on the ballot represent the Supervisor in row 2 and the Clerk in row 3.  If this were the case the code would have to be modified as follows:
1. Add more lists and dictionaries, one for each seat.
```
# Candidate Options and candidate votes.
candidate_options.supervisor = []
candidate_votes.supervisor = {}
candidate_options.clerk = []
candidate_votes.clerk = {}
```
2. Add more variables representing the different seats:
```
 # Get the candidate name from each row.
 candidate_name_supervisor  = row[2]
 candidate_name_clerk = row[3]
```
3. Use more if statements.  One for each seat.
4. Track their vote counts
5. Display the data for the other seats in the county

By doing some of this refactoring of the code it can be used for elections where more than one seat is up for relection.  It also may be necessary if there were a lot of seats to use a dictionary or list with dictionaries within it.

#### Example #2
Another aspect of many elections is that there are candidates that are running from different parties.  In the example for the Counties in Colorada this may not be the case.  Yet, state election might have candidates running for the same race but from different parties.  There may be a Democrat, a Republican, an Independent running for Governor or Congress.  And while in a popular election the outcome is to find who got the most votes, it's important to be able to show the person's party.  The dataset could include another column for __Party__.  

Modifying the script:
```
# Make the candidate_options a dictionary instead of list the key is the name of the candidate and the value is the party
candidate_options = {}

# Get the candidate name and party from the 4th column
candidate_party = row[3]
```
Then during the loop when we're adding the candidate and initializing the votes we add the party
```
if candidate_name not in candidate_options:
    # Add the candidate name to the candidate_options dictionary as the key and the candidates party as the value.
    candidate_options[candidate_name] = candidate_party
    # And begin tracking that candidate's voter count.
    candidate_votes[candidate_name] = 0
```
Then in the output we can add the information about the candidate and their party
```
# Retrieve vote count and percentage
votes = candidate_votes.get(candidate_name)
party = candidate_options.get(candidate_name)
vote_percentage = float(votes) / float(total_votes) * 100
candidate_results = (f"{candidate_name} {party}: {vote_percentage:.1f}% ({votes:,})\n")


