# -*- coding: UTF-8 -*-

import csv
import os

# constants
INPUT_PATH = os.path.join("Resources", "budget_data.csv") 
OUTPUT_PATH = os.path.join("analysis", "budget_analysis.txt")


# Define variables to track the financial data
total_months = 0
total_net = 0
monthly_change = []
greatest_increase = 0
greatest_decrease = 999999999999

# # Add more variables to track other necessary financial data

# Open and read the csv
with open(INPUT_PATH, "r", encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data)
    # Skip the header row
    header = next(reader)

    ###Extract first row to avoid appending to net_change_list
    second_row = next(reader)
    previous_net = int(second_row[1])
    total_net += int(second_row[1])
    ###Track the total and net change
    total_months +=1
    # Process each row of data
    for row in reader:
        # Track the total
        total_months +=1
        total_net += int(row[1])


        # Track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        monthly_change.append(net_change)




# Calculate the average net change across the months
average_net_change = sum(monthly_change)/len(monthly_change)
greatest_increase = max(monthly_change)
greatest_decrease = min(monthly_change)
# Generate the output summary
output_summary = (f"Financial Analysis\n" 
                  f"------------------\n"
                  f"Total months: {total_months}\n"
                  f"Total: ${total_net}\n"
                  f"Average Change ${average_net_change}\n"
                  f"Greatest Increase in Profits ${greatest_increase}\n"
                  f"Greatest Decrease in Profits ${greatest_decrease}\n"


)

# Print the output
print(output_summary)

# Write the results to a text file
with open(OUTPUT_PATH, "w") as txt_file:
    txt_file.write(output_summary)
