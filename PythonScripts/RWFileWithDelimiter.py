"""
this reads a file with a delimiter and writes each line (minus the delimiter)
to another file.
"""
import csv

ls =[]
with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\sampleText2.txt','r') as file:
    #reader = csv.reader(file)
    c = csv.reader(file,delimiter ='.')
    for line in c:
        ls.append(line)
with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\extracted5.txt','w') as out_file:
    #writer  = csv.writer(out_file)
    i = 0
    try:
        print('Reading file...')
        for item in ls[0][i]:
            out_file.write(ls[0][i] + '\n')
            i+=1
    except IndexError:
        print('End of file reached')
            #out_file.write(ls[0][i] )
            #print(ls[i][0])
            #i +=1
            #out_file.write(item)
