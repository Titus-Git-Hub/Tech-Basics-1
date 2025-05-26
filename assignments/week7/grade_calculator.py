#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# To handle this task, AI was used as a tool for assistance.

# This submission is probably not the final one; however, this is the state 
# I have currently achieved with the lessons learned and the help from ChatGPT.

# Improvement points: The clarity of the code; Using exception handling if the csv can't be found; 
# Handling no submission and spaces; removing the columns that have no content left at the end (besides the generated one from week 7-12); and more...

import csv
import random


def read_and_write():
    rows = []

    # Read the original CSV
    with open("Technical Basics I_2025 - Sheet1.csv", newline='') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            rows.append(row)
        
    # Removing irrelevant information
    columns_to_remove = ['Email', 'Link to your GitHub']
    fieldnames = [f for f in fieldnames if f not in columns_to_remove]
    for row in rows:
        for col in columns_to_remove:
            row.pop(col, None)

    # Weeks 1–5 from the CSV — not newly generated, only added to the list of columns
    week_columns = [f"week{week}" for week in range(1, 6)]

    # Weeks 7–12 newly generated, added to fieldnames and week_columns
    for week in range(7, 13):
        week_col = f"week{week}"
        week_columns.append(week_col)
        fieldnames.append(week_col)
        for row in rows:
            row[week_col] = random.randint(0, 3)

    # Add "Total Points" and "Average Points"
    fieldnames.append("Total Points")
    fieldnames.append("Average Points")

    # Calculation of Total & Average based on all weeks (1–5 + 7–12)
    for row in rows:
        scores = []
        for col in week_columns:
            val = row.get(col, '0')
            try:
                scores.append(int(val))
            except ValueError:
                scores.append(0)

        best_10 = sorted(scores, reverse=True)[:10]
        total_points = sum(best_10)
        average_points = round(sum(scores) / len(scores), 2)

        row["Total Points"] = total_points
        row["Average Points"] = average_points

    # Write to new CSV
    with open('Technical Basics I_2025 - Sheet1_new.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Print for checking
    print("Content of the new CSV file (with Total & Average Points): \n")
    for row in rows:
        print(row)
        
read_and_write()

