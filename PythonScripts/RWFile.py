# def rfile(filename):
#     ls = []
#     with open('C:\\Users\\tweatherall\\Desktop\\'+filename,'r') as file:
#         for line in file:
#             ls.append(line.strip() + '|')
    #return ls
# def wfile(filename, ls):
#     with open('C:\\Users\\tweatherall\\Desktop\\' + filename,'w') as out_file:
#         for item in ls:
#             out_file.write(item)

#def main():
ls =[]
with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\sampleText.txt','r') as file:
    #reader = csv.reader(file)
    for line in file:
        ls.append(line.strip() + '|')
    print(ls)

with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\extracted.txt','w') as out_file:
    #writer  = csv.writer(out_file)
    out_file.truncate()
    for item in ls:
        out_file.write(item)

# print (__name__)
#
# if __name__ == "__main__":
#     main()
