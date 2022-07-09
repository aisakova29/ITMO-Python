import csv
import os
import time


files = ('data_01.csv', 'data_02.csv', 'data_03.csv')


timestr = time.strftime("%Y%m%d-%H%M%S")
newfile = 'newfile'+timestr+'.txt'
logfile = 'logfile.txt'

with open(newfile, 'w') as my_output_file:
    with open(logfile, 'w') as my_log_file:
        for file in files:
            if os.path.exists(file):
                with open(file, 'r') as my_input_file:
                    [my_output_file.write (" ".join(row)+'\n') for row in csv.reader(my_input_file)]
                    [my_log_file.write(file+' was copied in '+timestr+'\n')]
                    my_input_file.close()
                    os.remove(file)
            else:
                [my_log_file.write(file + ' does not exist ' + timestr + '\n')]
