# PyPoll
import csv
import os

# insure that the Terminal's working directory is
#   ~/../Homework/python-challenge/PyPoll

# set up file interfaces
inputfile = 'election_data.csv'
outputfile = 'election_analysis.csv'
input_path = os.path.join('.', 'Resources', inputfile)
output_path = os.path.join('.', 'Output', outputfile)

# read the voting data
with open(input_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)   # discard header
    candidate_tally = {}           # a dictionary for the voting data for each candidate 
    vote_total = 0                 # the total number of votes cast

    # evaluate first vote (first row)
    first_row = next(csvreader)
    winner = first_row[2]          # the winner, which starts with the first vote
    candidate_tally[first_row[2]] = 1
    vote_total += 1

    # evaluate remaining rows
    for row in csvreader:
        voter_id = row[0]
        if voter_id != "":         # skip invalid row (no voter ID)
            county = row[1]        # the county in which the vote was cast
            candidate = row[2]     # the candidate for whom was voted 
            vote_total += 1
            if candidate in candidate_tally:
                # increment the tally for the candidate
                candidate_tally[candidate] += 1
            else:
                # add the candidate to the tally dictionary
                candidate_tally[candidate] = 1

# find the winner
for candidate in candidate_tally:
    if  candidate_tally[candidate] > candidate_tally[winner]:
        winner = candidate


# d(ouble)_print to both the terminal and to a writer (for csv file)
def d_print(text, writer):
    print(text)
    writer.writerow([text])


print("")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    d_print("Election Results", csvwriter)
    d_print("---------------------------------", csvwriter)
    d_print(f"Total Votes:  {vote_total}", csvwriter)
    d_print("---------------------------------", csvwriter)
    for candidate in candidate_tally:
        tally = candidate_tally[candidate]
        percentage = (tally/vote_total) * 100
        # percentage is displayed with two decimal points
        d_print(f"{candidate}: {percentage:.2f}%  ({tally})", csvwriter)
    d_print("---------------------------------", csvwriter)
    d_print(f"Winner is {winner}", csvwriter)
    d_print("---------------------------------", csvwriter)


print("")