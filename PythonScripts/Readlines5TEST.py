"""
this differs from Readlines4TEST.py as this assigns each line to a variable each
time, instead of using the ''.join() method to assign the value that is in the
generator object at a given time
"""

def rdline(filename, searchterm):
    with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files' + filename,'r') as in_file:
        Found = 0
        for line in in_file:
            rline = line
            #print(rline)
            if searchTerm in line:
                #print('Search term found in line: ',line)
                Found = 1
                yield rline
        if Found == 0:
            print('Not found')

def wfile(filename,line):
    with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files' + filename,'w') as out_file:
        try:
            print('Writing file...')
            out_file.write(line)
            #out_file.write('\n')
        except:
            print('End of file reached')

if __name__ == "__main__":
    in_file = input('Enter file to read: ')
    searchTerm = input('Enter search term: ')
    out_file = input('Enter file to write to: ')
    #print(''.join(rdline(in_file,searchTerm)))
    wfile(out_file,rdline(in_file,searchTerm))
