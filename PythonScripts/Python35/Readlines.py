'''
searchParams = ['nice','people','day','whole','dream']

for line in open('C:\\Users\\tweatherall\\Desktop\\sampleText.txt', 'r'):
    for txt in searchParams:
        if txt in file:
            print(txt,'was found')
        else:
            print(txt,'not found')
'''


#file = open('C:\\Users\\tweatherall\\Desktop\\sampleText.txt','r')
'''
searchParams = ['nice','people','day','whole','dream']
with open('C:\\Users\\tweatherall\\Desktop\\sampleText.txt','r') as file:
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

searchParam = input('Enter search term: ')
with open('C:\\Users\\tweatherall\\Desktop\\sampleText.txt','r') as file:
    print('*'*100)
    for line in file:
        print('\n','READING LINE:',line,'\n')
        if searchParam in line:
            print('"',searchParam,'"', 'found in: ',line)
            print('-'*50)
            break
        else:
            print('"',searchParam,'"','not found')
            print('-'*50)
    print('*'*100)



