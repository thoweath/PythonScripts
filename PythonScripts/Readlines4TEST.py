"""
this differs from Readlines3TEST.py in that this uses a generator object
to iterate over lines in the file instead of a list
"""

def rdline(filename, searchterm):
    with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files' + filename,'r') as in_file:
        Found = 0
        for line in in_file:
            #rline = line
            #print(rline)
            if searchTerm in line:
                #print('Search term found in line: ',line)
                Found = 1
                yield ''.join(line)
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
    wfile(out_file,''.join(rdline(in_file,searchTerm)))
