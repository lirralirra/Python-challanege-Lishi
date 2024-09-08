import os
import csv

#check the working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Define the path to the CSV file
file_path = os.path.join('resources', 'budget_data.csv')

# define initialize variables
total_months = 0
net_total = 0
profit_losses = []
dates = []

# Read the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    print(f"Header: {header}") # check the header

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1]) # change profit/losses to profit_loss

        # Append data to lists
        dates.append(date)
        profit_losses.append(profit_loss)

        # Update total months and net total
        total_months += 1
        net_total += profit_loss

# Calculate changes in Profit/Losses
changes = [profit_losses[i] - profit_losses[i - 1] for i in range(1, len(profit_losses))]
average_change = sum(changes) / len(changes) if changes else 0

# Find greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = dates[changes.index(greatest_increase) + 1]  # +1 to get the corresponding date
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]  # +1 to get the corresponding date

# Write results to a text file in the Analysis folder
output_path = os.path.join('Analysis', 'ByBank_analysis_result.txt')

with open(output_path, 'w') as file:
    # Write the results to both console and file
    output = [
        "Financial Analysis",
        "----------------------------",
        f"Total Months: {total_months}",
        f"Total Profit/Losses: ${net_total}",
        f"Average Change: ${average_change:.2f}",
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})",
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
    ]

#print the results to the terminal
    for line in output:
        print(line)
        file.write(line + '\n')

print(f"\nResults have been written to {output_path}")