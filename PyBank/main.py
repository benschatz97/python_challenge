# -*- coding: UTF-8 -*-

import csv
import os

# constants
INPUT_PATH = os.path.join(r"PyBank\Resources\budget_data.csv") 
OUTPUT_PATH = os.path.join(r"C:\Users\bensc\Desktop\Class Folder\Assignments_Folder\python_challenge\PyBank\analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# # Add more variables to track other necessary financial data
# sum_profit_Loss = 0
# greatest_increase = 0
# greatest_decrease = 0
# Open and read the csv
with open(r"PyBank\Resources\budget_data.csv", "r", encoding='UTF-8') as financial_data:
    reader = csv.reader(financial_data)
    # Skip the header row
    header = next(reader)

    ###Extract first row to avoid appending to net_change_list
    ###Track the total and net change

    # Process each row of data
    for row in reader:

        # Track the total


        # Track the net change


        # Calculate the greatest increase in profits (month and amount)


        # Calculate the greatest decrease in losses (month and amount)



# Calculate the average net change across the months


# Generate the output summary


# Print the output


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
