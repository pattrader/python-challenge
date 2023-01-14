# importing needed direcetories to read from path and the flie

import os
import csv 
# path to resoruce file
path = os.path.join('.','Resources', 'budget_data.csv')

#Read the resouce file
with open(path) as csvfile:
  csvreader = csv.reader(csvfile)


      # Read the header row first (skip this step if there is now header)
  csv_header = next(csvreader)
   

    # Read each row of data after the header
  total_months = 0
  money = 0
  change = 0
  second_cell = 0
  total_chg = 0
  max = -1000000000
  min = 10000000000
 # Looping each row to read each number
  for row in csvreader:
      #Saving first data point to calculte change
        first_cell = int(row[1])
      # Skipping calculation for the first cell due to header
        if total_months >0: 
          # Calculating change for profits or loss for each month
          chg = first_cell - second_cell
          total_chg += chg
          # Saving Max and Min with month using if statement 
          if max < chg:
            max = chg 
            max_month = row[0]
          if min > chg:
            min = chg
            min_month = row[0]
        
        # Adding one month at a time
        total_months += 1

        # Adding one month dollars at a time
        money += int(row[1])

        # Saving variable for the second cell get change
        second_cell = first_cell  
        
  # Printing everthing asked in HW. For average we have to exclude first month, therefore 
  # its minus 1 month. 
  print(f'Total Months: {total_months}')
  print(f'Total: ${money}')
  print(f'Average Change:  ${round(total_chg/(total_months-1),2)}')
  print(f'Greatest Increase in Profits: {max_month} (${max})')
  print(f'Greatest Decrease in Profits: {min_month} (${min})')

# Specify the file to write to
output_path = os.path.join(".", "analysis", "PyPoll.csv")
with open(output_path, 'w', newline='') as csvfile:

  # Initialize csv.writer and seperating each cell by comma
  csvwriter = csv.writer(csvfile, delimiter=',')
  # Write each row 
  csvwriter.writerow(['Total Months:', (total_months)])
  csvwriter.writerow(['Total $:', (money)])
  csvwriter.writerow(['Agerage Change $', (round(total_chg/(total_months-1),2))])
  csvwriter.writerow(['Greatest Increase in Profits:',(max_month),(max)])
  csvwriter.writerow(['Greatest Decrease in Profits:',(min_month),(min)])