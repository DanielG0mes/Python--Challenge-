import csv

file_name = 'budget_data.csv'

total_months = 0
total_revenue = 0
revenue_change_list = []
previous_revenue = None
greatest_increase = ["", float("-inf")]
greatest_decrease = ["", float("inf")]

# Open CSV file in read mode
with open('budget_data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    # Skip header row
    print(csv_reader)



    next(csv_reader)
    
  # Loop through each row in the CSV file
    for row in csv_reader:
        print(row)
        # Increment total months count
        total_months += 1

        # Calculate total revenue
        total_revenue += int(row[1])  # Assuming the revenue column is at index 1

        # Calculate revenue change and update greatest increase/decrease
        if previous_revenue is not None:
            revenue_change = int(row[1]) - previous_revenue
            revenue_change_list.append(revenue_change)
            if revenue_change > greatest_increase[1]:
                greatest_increase = [row[0], revenue_change]
            if revenue_change < greatest_decrease[1]:
                greatest_decrease = [row[0], revenue_change]

        # Update previous revenue for the next iteration
        previous_revenue = int(row[1])

# Calculate average revenue change
revenue_average = sum(revenue_change_list) / len(revenue_change_list)

# Print results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${revenue_average:.2f}")
print(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})")

# write changes to csv
with open('newfile', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%d\n" % revenue_average)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))