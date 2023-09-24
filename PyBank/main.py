import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
total_months = 0
net_total = 0
average_change = 0
max_increase = 0
max_decrease = 0
previous_profit_loss = None
max_increase_date = ''
max_decrease_date = ''
total_change = 0

with open(csvpath) as csvfile:
    # csv reader specifies delimiter and variable that holds the contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of the data after the header
    for row in csvreader:
        date, profit_loss = row
        profit_loss = int(profit_loss)
        total_months += 1
        net_total += profit_loss
        if previous_profit_loss is not None:
            profit_loss_change = profit_loss - int(previous_profit_loss)
            total_change += profit_loss_change
            if profit_loss_change > max_increase:
                max_increase = profit_loss_change
                max_increase_date = date
            if profit_loss_change < max_decrease:
                max_decrease = profit_loss_change
                max_decrease_date = date
        previous_profit_loss = profit_loss

average_change = total_change / (total_months - 1)

# Print the financial analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# Create a text file at the specified absolute path to write the results
output_file = "/Users/kirbysmith/Desktop/module3challenge/python_challenge/PyBank/Analysis/financial_analysis.txt"

with open(output_file, "w") as f:
    # Write the results to the file
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${net_total}\n")
    f.write(f"Average Change: ${average_change:.2f}\n")
    f.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    f.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")

print(f"Financial analysis results have been saved to '{output_file}'")

