"""
This uses the enumerate function to enumerate the list, so each line will have
a corresponding line number.
"""

def main():
    searchParam = []
    searchParam.append( input('Enter search term: '))
    continueSearch = input('Additional search terms?: ')
    while continueSearch == 'y':
        addSearch = input('Enter search term: ')
        searchParam.append(addSearch)
        continueSearch = input('Additional search terms?: ')

    with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\sampleText2.txt','r') as file:
        print('*'*70)
        ls = []
        Found = 0
        for line in file:
            ls = line.split('.')
            print('Searching...')
            for i in searchParam:
                for index, item in enumerate(ls):
                    if i in item:
                        Found = 1
                        print('"',i,'"', 'found in line: ',index, ':',item)
                        print('-'*70)
                        continue
                    else:
                        pass
                        # print('"',i,'"','not found in line: ', item)
                        # print('-'*70)
                if Found == 0:
                    print(i,'not found')
        print('*'*70)

if __name__ == "__main__":
    main()
