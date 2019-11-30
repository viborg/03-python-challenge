# PyBank
import csv
import os

# insure that the Terminal's working directory is 
#   ~/../Homework/python-challenge/PyBank

# set up file interfaces
inputfile = 'budget_data.csv'
outputfile = 'financial_analysis.csv'
input_path = os.path.join('.', 'Resources', inputfile)
output_path = os.path.join('.', 'Output', outputfile)

with open(input_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    month_list = []           # a list of the months that profits were recorded
    month_count = 0           # the running count of all months
    net_total = 0             # the running sum of all the profits/losses         
    previous_profit = 0       # the profit in the previus month
    change = 0                # the change in profits from the previous month
    aggregate_change = 0      # the running sum of all of the profit changes
    greatest_increase = 0     # greatest increase in profits
    greatest_decrease = 0     # greatest decrease in profits
    increase_date = ""        # date on which greatest increase occurred
    decrease_date = ""        # date on which greatest decrease occurred
 
    # evaluate first vote (first row)
    first_row = next(csvreader)
    date = first_row[0] 
    profit = int(first_row[1])
    if date != "":            # skip invalid row (no date)
        previous_profit = profit
        aggregate_change = 0
        month_count += 1

    # evaluate remaining rows
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
        if date != "":        # skip invalid row (no date)
            month_count += 1
            month = date.split("-")[0]
            if month not in month_list:
                month_list.append(month)
            net_total += profit
            change = profit - previous_profit
            previous_profit = profit
            aggregate_change += change
            if change > greatest_increase:
                greatest_increase = change
                increase_date = date
            if change < greatest_decrease:
                greatest_decrease = change
                decrease_date = date

# d(ouble)_print to both the terminal and to a writer (for csv file)
def d_print(text, writer):
    print(text)
    writer.writerow([text])

print('')

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    d_print("Financial Analysis", csvwriter)
    d_print("---------------------------------", csvwriter)
    d_print(f"Total Months:  {month_count}", csvwriter)
    d_print(f"Total:  ${net_total}", csvwriter)
    # average change uses one less month in calculation
    # average change is displayed with two decimal points
    d_print(f"Average change:  {aggregate_change/(month_count-1):.2f}", csvwriter)
    d_print(f"Greatest increase in profits:  {increase_date}  (${greatest_increase})",
        csvwriter)
    d_print(f"Greatest decrease in profits:  {decrease_date}  (${greatest_decrease})",
        csvwriter)

print('')