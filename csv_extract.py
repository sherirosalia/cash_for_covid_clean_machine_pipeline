# from https://stackoverflow.com/questions/49142612/python-iterate-over-folders-and-combine-csv-files-inside

import pandas as pd
import csv
import os
import sys 

root_path = 'states'

with open('all_states.csv', 'w') as all_states:


    for root, sub, files in os.walk(root_path):
        # print(root)
        # print(files)
        # print(sub)
        filenames = [os.path.join(root, filename) for filename in files
                    if filename.endswith('.csv')]
        # print(filenames)
        # one option if multiple csv files in one directory and combining files just in that direcotory.
        # Won't work in this case because each directory is separate.

        # Saved for future reference:
        # combined_path = os.path.join(root, 'combined.csv')

        # combining all files into one 
        for state_csv in filenames:
            print(state_csv)
            
            with open(state_csv, 'r') as state_csv_lines:
                #this loop opens the csv, reads it and treats each line as a separate entity
                # next(file, None) tells python to skip the first line which in this case is a 
                # header that should not be repeated 49 times (50 states - 1 header needed)
                # print(next(state_csv_lines, None))

                next(state_csv_lines, None)
                for line in state_csv_lines:
                    all_states.write(line)

            # REMINDER: all headers have been removed, so go back into the csv and add


    






