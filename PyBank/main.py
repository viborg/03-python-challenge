# PyBank
import csv
import os

# insure that the Terminal's working directory is 
#   ~/../Homework/python-challenge/PyBank

# set up file interfaces
inputfile = 'budget_data.csv'
#inputfile = "test_file.csv"  # truncated version for testing
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

print("")
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months:  {month_count}")
print(f"Total:  ${net_total}")
# average change uses one less month in calculation
# average change is displayed with two decimal points
print(f"Average change:  {aggregate_change/(month_count-1):.2f}")
print(f"Greatest increase in profits:  {increase_date}  (${greatest_increase})")
print(f"Greatest decrease in profits:  {decrease_date}  (${greatest_decrease})")
print("")

# repeat print, but into a csv file
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow([f"Total Months:  {month_count}"])
    csvwriter.writerow([f"Total:  ${net_total}"])
    # average change uses one less month in calculation
    # average change is displayed with two decimal points
    csvwriter.writerow([f"Average change:  {aggregate_change/(month_count-1):.2f}"])
    csvwriter.writerow([f"Greatest increase in profits:  {increase_date}  (${greatest_increase})"])
    csvwriter.writerow([f"Greatest decrease in profits:  {decrease_date}  (${greatest_decrease})"])
