"""
Read lines into Dictionary instead of list
and write dictionary key value pairs to file

Also prints what terms were found in what line, and prints what terms were not
found only once. Version 3 differs from version 2 in that this version uses the
zip function to create a tuple comprised of the Found status and Search term.

Also uses a list comprehension instead of a for loop to construct the 'Found'
list of the same length as the 'searchParam' list, and populate with default
values ('default'). Update: using the Found = searchParam[:] is the more
pythonic way to copy elements from one list/string to another.
"""

searchParam = []
searchParam.append( input('Enter search term: ').upper())
continueSearch = input('Additional search terms (y/n)?: ')

while continueSearch == 'y':
    addSearch = input('Enter search term: ').upper()
    searchParam.append(addSearch)
    continueSearch = input('Additional search terms(y/n)?: ')

#uses a list comprehension to create a list of the same size as the searchParam
#list with default values of 50.
#Found = ['default' for i in range(len(searchParam))]
Found = searchParam[:] #this is the more pythonic way of copying elements from one list to another
#create list to update with 1-Found or 0-Not Found and populate with as many defualt starting
#values as there are search terms.
# for i in range(len(searchParam)):
#     Found.append(50)
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
                print('\n','"',i,'"', 'found in line ',k,':',v)
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

#uses the zip function to comnbine the Found status and the search term in a
#single tuple pair.
for status, term in zip(Found,searchParam):
    if status == 0:
        print('\n','"',term,'"','not found')
