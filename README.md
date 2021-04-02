# Election_Analysis

## Project Overview of Election Audit
A Colorado Board of Elections employee has requested a election audit of a recent local congressional election.  He has specified the information he would like to obtain from the raw data it is as follows:

1. The total number of votes cast.
2. The counties that participated in the election with the percentage of votes cast in each county and the total number of votes cast in each county
3. The county that had the greatest voter turnout
4. The complete list of candidates who received votes.
5. The total number of votes each candidate received.
6. The percentage of votes each candidate won.
7. The winner of the election based on popular vote.

The [code for this project](https://github.com/linb960/Election_Analysis/blob/main/PyPoll_Challenge.py) was written in python.  To calculate total number of votes for candidates, counties and overall, counters are used.  The candidates and counties are stored in lists and the totals collected for the each county and each candidate is stored in dictionaries as key, value pairs.

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
To do the analysis of the set of data provided by the Colorado Board of Elections employee a primary loop was created to read each row of the data.  The collection of the data into the lists and the dictionaries made it easier to then output the information for the results.  For example with a candidate:
```
if candidate_name not in candidate_options:
    # Add the candidate name to the candidate list.
    candidate_options.append(candidate_name)

    # And begin tracking that candidate's voter count.
    candidate_votes[candidate_name] = 0

# Add a vote to that candidate's count
candidate_votes[candidate_name] += 1
```
We need to see if the candidate exists in the list of candidate_options and whether we have started tracking the number of votes they have in the candidate_votes dictionary.  Once we find the candidate then from then on when ever we come across the candidate in a row we add to the dictionary that has the candidates name as key another vote to the total.

This is the same for the county tabulations and the resulting information is what gets output to the text file and the terminal.

### Reusable Code
This code could be reused on any sets of data that has three columns of information, a ballot id number, a county (or maybe a city or state) and a candidate.  

But this code has it's limitations.  

An example for modifying the script comes when we realize that most elections have several candidates on a ballot at once.  For example there could be a section of the ballot for a County Supervisor, a County Clerk, a County Judge.  If this were the case the code would have to be modified as follows:
1. Add more lists and dictionaries, one for each seat.
2. Add more variables like this:
```
 # Get the candidate name from each row.
 candidate_name_supervisor  = row[2]
 candidate_name_clerk = row[3]
 candidate_name_judge = row[4]

```
3. Use more if statements like the one above to find the other candidates
4. Track their vote counts
5. Display the data for the other seats in the county


