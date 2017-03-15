"""
this reads a file with a delimiter and writes each line (minus the delimiter)
to another file.

this version is the modularized version of RWFileWithDelimiter2.py
"""
def rfile(filename, delimiter):
    ls = []
    with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files'+ filename,'r') as file:
        for line in file:
            ls += line.split(delimiter)

            #temp = line.split(delimiter)
            #ls.extend(temp) #this works the same as above line of code
    return ls

def wfile(filename,ls):
    with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files' + filename,'w') as out_file:
        try:
            print('Writing file...')
            for item in ls:
                out_file.write(item)
                out_file.write('\n')
        except:
            print('End of file reached')

def main(in_file,delimiter,out_file):
    ls = rfile(in_file,delimiter)
    wfile(out_file,ls)

if __name__ == "__main__":
    in_file = input('Enter filename to read: ')
    delimiter = input('Enter file delimiter: ')
    out_file = input('Enter filename to write to: ')
    main(in_file,delimiter,out_file)
    # in_file = input('Enter filename to read: ')
    # delimiter = input('Enter file delimiter: ')
    # out_file = input('Enter filename to write to: ')
    # ls = rfile(in_file,delimiter)
    # main(out_file)
