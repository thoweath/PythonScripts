"""
this reads a file with a delimiter and writes each line (minus the delimiter)
to another file.
"""

ls =[]
with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\sampleText2.txt','r') as file:
    #reader = csv.reader(file)
    for line in file:
        #ls.append(line.split('.'))
        ls = line.split('.')
        #ls.append(lines)
        #ls.append(line.split('|'))
with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\extracted5.txt','w') as out_file:
    #writer  = csv.writer(out_file)
    try:
        print('Writing file...')
        for item in ls:
            out_file.write(item)
            out_file.write('\n')
    except:
        print('End of file reached')
            #out_file.write(ls[0][i] )
            #print(ls[i][0])
            #i +=1
            #out_file.write(item)
