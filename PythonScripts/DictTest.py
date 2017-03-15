"""
Read lines into Dictionary instead of list
and write dictionary key value pairs to file
"""

searchParam = []
searchParam.append( input('Enter search term: ').upper())
continueSearch = input('Additional search terms (y/n)?: ')
Found = []
Found = searchParam
foundparam = 0
foundparamindex = 0
while continueSearch == 'y':
    addSearch = input('Enter search term: ').upper()
    searchParam.append(addSearch)
    continueSearch = input('Additional search terms?: ')

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
            if i in v.upper():
                # foundparam = searchParam.index(i)
                # print(foundparam)
                # Found[foundparam] = 1
                #print(Found)
                print('"',i,'"', 'found in line ',k,':',v)
                # Found[foundparam] = 1
                # Found.append(foundparam)
                # foundparamindex += 1
                continue
            # else:
            #     foundparam = searchParam.index(i)
            #     print(foundparam)
            #     Found += foundparam
            #     print(Found)
                #Found[foundparam] = 0
                # foundparam = 0
                # Found.append(foundparam)
                # foundparamindex += 1
#print(searchParam)
#print(Found)

# for index, item in enumerate(searchParam):
#     if Found[index] == 0:
#         print('"',searchParam[index],'"','not found')

                # if Found[foundparamindex - 1] == 0:
                #     print('"',i,'"','not found')
