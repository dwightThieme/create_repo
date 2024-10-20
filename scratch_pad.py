# import os
# import csv

# print("\n\n")

# for a in range(32):
#     print(
#         f"{a:3}    {a:06b}    {63^a:06b}    "
#         f"{63^a:3}    {~a:4}    {~a:07b}    "
#         f"{~a+1:4}    {(63^a)+1:3}    {((63^a)+1)%64:06b}"
#     )

# print("\n\n")


# # import math
# # def isPrime(n):
# #     answer = True
# #     count = 2
# #     print(f"The count is {count}")
# #     while count < n:
# #         answer = [False, True][math.ceil(math.fabs(math.sin(n % count)))]
# #         print(f"The answer is {answer}")
# #         count = [count + 1, n][~answer]
# #         print(f"The count is {count}")
# #     return answer
# # k = 5
# # print(f"The statement '{k} is prime' is {isPrime(k)}")


# # from statistics import mean as avg
# # import os
# # import csv

# # base_path = r"C:\Users\dwigh"
# # repo_path = r"Desktop\Repositories\python-challenge\PyBank"
# # resource_path = r"Resources\budget_data.csv"
# # input_path = os.path.join(base_path, repo_path, resource_path)
# # input_path = input_path.replace("\\", "/")

# # print(f"\n\ninput path -> {input_path}\n\n")

# # with open(input_path, newline="") as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=",")
# #     next(csv_reader)
# #     csv_data = list(csv_reader)

# # rec_num = len(csv_data)
# # months = [record[0] for record in csv_data]
# # amts = [int(record[1]) for record in csv_data]
# # net_profit = sum(amts)
# # prev_amt = amts[:-1]
# # curr_amt = amts[1:]
# # diffs = [[months[1:][i], amts[1:][i] - amts[:-1][i]] for i in range(rec_num - 1)]

# # # To generate difference data, first get a list of mmonths
# # # and monthly differences for the second through last months
# # monthly_differences = [
# #     [months[i], profits[i] - profits[i - 1]] for i in range(1, num_months)
# # ]

# # # Find the average monthly change in profits
# # avg_diff = avg(diff[1] for diff in monthly_differences)

# # # Find the maximum monthy increase and the month in which it occurs
# # max_incr = max(monthly_differences, key=lambda col: col[1])

# # # Find the maximum monthy decrease and the month in which it occurs
# # max_decr = min(monthly_differences, key=lambda col: col[1])

# # # Create the financial analysis report text
# # report = (
# #     f"{' Financial Analysis ':-^48}\n"
# #     f"{'Total Months:':24}{num_months:24,.0f}\n"
# #     f"{'Net Profits:':24}{net_profits:24,.0f}\n"
# #     f"{'Avg Change:':24}{avg_diff:24,.0f}\n"
# #     f"{'Max Increase:':14}{max_incr[0]:^20}{max_incr[1]:14,.0f}\n"
# #     f"{'Max Decrease:':14}{max_decr[0]:^20}{max_decr[1]:14,.0f}\n"
# #     f"{'--':-^48}"
# # )

# # # Assemble the output resource path. Include the base and
# # # repo paths to allow for both absolute and relative paths
# # resource_path = "Resources/budget_analysis.txt"
# # output_path = os.path.join(base_path, repo_path, resource_path)

# # # Open the analysis resource text file and write the report to it
# # with open(output_path, "w") as textfile:
# #     textfile.write(report)

# # # Check to see if the report exists and is properly formatted:
# # # The input and output resource paths are the same ... but we
# # # we strive for clarity!
# # input_path = output_path

# # # Open report text file for reading and print it to the terminal
# # with open(input_path, "r") as textfile:
# #     report = textfile.read()

# # print(f"\n\n{report}\n\n")

# # prev, curr = data[:-1], data[1:]

# # for i in range(len(curr)):
# #     print(f"{prev[i][1]:10,.0f}  {curr[i][1]:10,.0f}")


# import os
# import csv

# base_path = r"C:\Users\dwigh"
# repo_path = r"Desktop\Repositories\python-challenge\PyBank"
# resource_path = r"Resources\budget_data.csv"
# input_path = os.path.join(base_path, repo_path, resource_path)
# input_path = input_path.replace("\\", "/")
# bank_path = input_path


# # This is an alternate coding of your average change function
# def average_change(bank_data):
#     with open(bank_data, "r") as bankfile:
#         bankreader = csv.reader(bankfile)
#         next(bankreader)

#         previous_value = int(next(bankreader)[1])
#         diff_count = 0

#         for row in bankreader:
#             diff_count += 1

#         current_value = int(row[1])

#     # Return the average of the monthly profit differences
#     return (current_value - previous_value) / diff_count


# # Printing function output with f string formatting
# print(f"{average_change(bank_path):14,.0f}")


# from pathlib import Pathro

# import os
# import csv

# Assemble the input csv file path, starting from the cwd
# input_path = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

# # Open the budget_data csv file for reading
# with open(input_path, encoding="utf-8", newline="") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")

#     # Don't include the csv file header in the data
#     next(csv_reader)

#     # Pass the raw text data out as a list
#     csv_data = list(csv_reader)

# month_list = [row[0] for row in csv_data]
# profit_list = [int(row[1]) for row in csv_data]

# print(f"\n\n{month_list[:5]}\n" f"\n{profit_list[0:5]}\n\n")

# print("\n")

# for i, p_num in enumerate(profit_list):
#     if i == 0:
#         smallest_profit = p_num
#         smallest_month = month_list[0]
#         print(f"{i:3} {smallest_month:>9} {smallest_profit:12,}")

#     elif p_num < smallest_profit:
#         smallest_profit = p_num
#         smallest_month = month_list[i]
#         print(f"{i:3} {smallest_month:>9} {smallest_profit:12,}")

# print("\n")

# for i, p_num in enumerate(profit_list):
#     if i == 0:
#         smallest_profit = p_num
#         smallest_month = month_list[0]
#         print(f"{i:3} {smallest_month:>9} {smallest_profit:12,}")

#     elif p_num > smallest_profit:
#         smallest_profit = p_num
#         smallest_month = month_list[i]
#         print(f"{i:3} {smallest_month:>9} {smallest_profit:12,}")

# print("\n")

# total_votes = 369711
# names = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
# tallies = [85213, 272892, 11606]


# vote_info = [
#     f"{name:<24} {tallies[i]:8,}   {(tallies[i]/total_votes)*100:5,.2f}%\n"
#     for i, name in enumerate(names)
# ]

# lines = [
#     f"{name:<24} {tallies[i]:8,}   {(tallies[i]/total_votes)*100:5,.2f}%\n"
#     for i, name in enumerate(names)
# ]

# print(f"\n\n{vote_info}\n\n")

# # lines = "".join(vote_info)
# # print(lines)

# record = ""
# print(f"record:\n{record}\n{'-'*48}")
# for line in lines:
#     record += line
#     print(f"record:\n{record}\n{'-'*48}\n")

# stats = ""
# print(f"stats:\n{stats}")
# for info in vote_info:
#     stats += info
#     print(f"stats:\n{stats}")

# stats = ""
# print(f"stats:\n{stats}")
# for info in vote_info:
#     stats += info
#     print(f"stats:\n{stats}")

# rows = ""
# print(f"rows:\n\n{rows}\n{'-'*48}")
# for i, name in enumerate(names):
#     rows += f"{name:<24} {tallies[i]:8,}   {(tallies[i]/total_votes)*100:5,.2f}%\n"
#     rows +=
#     print(f"rows:\n\n{rows}\n{'-'*48}")


# # Use the lines data to create a single text string
# record = ""
# print(f"record:\n\n{record}\n{'-'*48}")
# for line in lines:
#     record += line
#     print(f"record:\n\n{record}\n{'-'*48}")

# report = (
#     "Budget Analysis"
#     "-----------------------------"
#     f"Total Months: {total_months}"
#     f"Net Total: ${net_total}"
#     f"Average Change: ${average_change:.2f}"
#     f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})"
#     f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"
# )


crime_data = {"State": "IL", "Year": 1672}

crime_dict = {
    "Murder (Blunderbuss)": 12,
    "Murder (Blade)": 15,
    "Murder (Poisoning)": 267,
    "Murder (Drowning)": 27,
    "Witchcraft": 67,
    "Adulteration of spirits": 4,
}

crime_data.update(crime_dict)

# data = {'a':0,
#         'b':[[1,2],
#              [3,4]],
#         'c':5,
#         'd':(('r', 'g', 'b'),
#              (('h', 's', 'v'),
#               ('c', 'y', 'm', 'k')))}

