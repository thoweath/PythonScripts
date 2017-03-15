"""
Read lines into Dictionary instead of list
and write dictionary key value pairs to file

Also prints what terms were found in what line, and prints what terms were not
found only once.
"""

searchParam = []
searchParam.append( input('Enter search term: ').upper())
continueSearch = input('Additional search terms (y/n)?: ')

while continueSearch == 'y':
    addSearch = input('Enter search term: ').upper()
    searchParam.append(addSearch)
    continueSearch = input('Additional search terms(y/n)?: ')
#create list to update with 1-Found or 0-Not Found and populate with as many defualt starting
#values as there are search terms.
Found = []
for i in range(len(searchParam)):
    Found.append(50)
with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\sampleText2WITHNEWLINES.txt','r') as file:
    d = {}
    linePos = 1
    for line in file:
        #print('\n','READING LINE:',line,'\n')
        d[linePos] = line
        linePos += 1
with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\extracted5.txt','w') as out_file:
    for k,v in d.items():
        out_file.write(str(k) + ':')
        out_file.write(v)
        for i in searchParam:
            if str(i) in v.upper():
                # foundparam = searchParam.index(i)
                # print(foundparam)
                # Found[foundparam] = 1
                #print(Found)
                print('"',i,'"', 'found in line ',k,':',v)
                foundparam = searchParam.index(i)
                if Found[foundparam] != 1:
                    Found[foundparam] = 1
                # Found[foundparam] = 1
                # Found.append(foundparam)
                # foundparamindex += 1
                continue
            else:
                #print(Found)
                foundparam = searchParam.index(i)
                #print(foundparam)
                if Found[foundparam] != 1:
                    Found[foundparam] = 0
                #print(Found)
                #Found[foundparam] = 0
                # foundparam = 0
                # Found.append(foundparam)
                # foundparamindex += 1


for index, item in enumerate(searchParam):
    if Found[index] == 0:
        print('"',searchParam[index],'"','not found')
