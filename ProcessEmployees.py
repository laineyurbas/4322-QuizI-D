'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file
infile = open("employee_data.csv", "r")
# outfile = open("Newemployee_data.csv", "w")
reader = csv.reader(infile)

# create an empty dictionary
newdict = {}
for item in reader:
    # use a loop to iterate through the csv file
    name = item[1] + item[2]
    salary = item[5]
    # outfile.write(f"Manager Name:{name}\n Current Salary:{salary}/n")
    print(f"Manager Name:{name}\n Current Salary:{salary}/n")


print()
print('=========================================')
print()

# iternate through the dictionary and print out the key and value as per printout
newdict[name] = [salary]
newdict = {
    "Manager Name": {[name]: "New salary" 46, 750.00},
    "Manager Name": {[name]: "New salary" 42, 790.00},
    "Manager Name": {[name]: "New salary" 45, 100.00},
    "Manager Name": {[name]: "New salary" 43, 500.00}}

print(newdict)

infile.close
