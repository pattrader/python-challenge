import os
import csv 

path = os.path.join('.','Resources', 'budget_data.csv')

with open(path) as csvfile:
  csvreader = csv.reader(csvfile)

  print(csvreader)
      # Read the header row first (skip this step if there is now header)
  csv_header = next(csvreader)
   

    # Read each row of data after the header
  total_months = 0
  money = 0
  change = 0
  second_cell = 0
  total_chg = 0
  max = -1000000000
  for row in csvreader:
      
        first_cell = int(row[1])
      
        if total_months >0: 
          chg = first_cell - second_cell
          total_chg += chg
          if max < chg:
            max = chg 
            max_month = row[0]
        
        
        total_months += 1
   
        money += int(row[1])
        second_cell = first_cell  
        
   
  print(f'Greatest Increase in Profits {max_month} (${max})')
  print(f'Average Change {total_chg/(total_months-1)}')
  print(f'Total Months: {total_months}')
    #print(f'Average Change: {avg}')
  print(f'Total: {money}')

    #print(f'Greatest increase in Profits: {month} ({max})')
    #print(f'Average Change: {money}')
