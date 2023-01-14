# importing needed direcetories to read from path and the flie

import os
import csv 
# path to resoruce file
path = os.path.join('.','Resources', 'election_data.csv')


#Read the resouce file
with open(path) as csvfile:
  csvreader = csv.reader(csvfile)


      # Read the header row first (skip this step if there is now header)
  csv_header = next(csvreader)
  # Calculating total count and intializing all the varibales to count all the votes
  total_count = 0
  c_vote = 0
  d_vote = 0
  r_vote = 0
  # Simple if formulas to count vote by name
  for row in csvreader:
    total_count +=  1
    if row[2] == 'Charles Casper Stockham':
        c_vote += 1
    if row[2] == 'Diana DeGette':
        d_vote += 1
    if row[2] == 'Raymon Anthony Doane':
        r_vote += 1

# Creating dictonary to keep count by name 
member = {c_vote:'Charles Casper Stockham',
          d_vote:'Diana DeGette',
          r_vote:'Raymon Anthony Doane',
}
# If statement to get the winner
if c_vote > d_vote and c_vote > r_vote:
    winner = (member[c_vote])
elif d_vote > c_vote and d_vote > r_vote:
    winner = (member[d_vote])
else: 
    winner = (member[r_vote])

# All the print functions
print('Election Results')
print('---------------------------')
print(f'Total Votes {total_count}')
print('---------------------------')
print(f'Charles Casper Stockham: {round(c_vote/total_count * 100,3)}% ({c_vote})')
print(f'Diana DeGette: {round(d_vote/total_count * 100,3)}% ({d_vote})')
print(f'Raymon Anthony Doane: {round(r_vote/total_count * 100,3)}% ({r_vote})')
print('---------------------------')
print(f'Winner: {winner}')

# Specify the file to write to
output_path = os.path.join(".", "analysis", "pypoll_text.txt")
with open(output_path, 'w', newline='') as txtfile:
 
 # Initialize text writer and writting all the lines
    txtfile.write('Election Results')
    txtfile.write('\n')
    txtfile.write('---------------------------')
    txtfile.write('\n')
    txtfile.write(f'Total Votes {total_count}')
    txtfile.write('\n')
    txtfile.write('---------------------------')
    txtfile.write('\n')
    txtfile.write(f'Charles Casper Stockham: {round(c_vote/total_count * 100,3)}% ({c_vote})')
    txtfile.write('\n')
    txtfile.write(f'Diana DeGette: {round(d_vote/total_count * 100,3)}% ({d_vote})')
    txtfile.write('\n')
    txtfile.write(f'Raymon Anthony Doane: {round(r_vote/total_count * 100,3)}% ({r_vote})')
    txtfile.write('\n')
    txtfile.write('---------------------------')
    txtfile.write('\n')
    txtfile.write(f'Winner: {winner}')