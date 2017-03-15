'''
searchParams = ['nice','people','day','whole','dream']

for line in open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\sampleText.txt', 'r'):
    for txt in searchParams:
        if txt in file:
            print(txt,'was found')
        else:
            print(txt,'not found')
'''


#file = open('C:\\Users\\tweatherall\\Desktop\\sampleText.txt','r')
'''
searchParams = ['nice','people','day','whole','dream']
with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\sampleText.txt','r') as file:
    print('*'*100)
    for line in file:
        print('\n','READING LINE:',line,'\n')
        for param in searchParams:
            print('\n','SEARCHING FOR:',param,'\n')
            if param in line:
                print('"',param,'"', 'found in: ',line)
                continue
            else:
                print('"',param,'"','not found')
            continue
        print('-'*50)
    print('*'*100)
'''

#Need to modify input file or line reader to read line by line
searchParam = []
searchParam.append( input('Enter search term: '))
continueSearch = input('Additional search terms?: ')
while continueSearch == 'y':
    addSearch = input('Enter search term: ')
    searchParam.append(addSearch)
    continueSearch = input('Additional search terms?: ')

with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\sampleText2.txt','r') as file:
    print('*'*70)
    for line in file:
        print('\n','READING LINE:',line,'\n')
        for i in searchParam:
            if i in line:
                print('"',i,'"', 'found in: ',line)
                print('-'*70)
                continue
            else:
                print('"',i,'"','not found')
                print('-'*70)
    print('*'*70)
