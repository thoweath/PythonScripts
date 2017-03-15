"""
This (RWFile2.py) is the final version of the RW example
"""

def rfile(filename):
    with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files'+filename,'r') as file:
        for line in file:
            ls.append(line.strip() + '|')
    #return ls
def wfile(filename):
    with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files' + filename,'w') as out_file:
        for item in ls:
            out_file.write(item)

def main(in_file,out_file):
    rfile(in_file)
    wfile(out_file)

if __name__ == "__main__":
    ls = []
    in_file = input('Enter filename to read: ')
    out_file = input('Enter filename to write to: ')
    main(in_file,out_file)
