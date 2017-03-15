with open('C:\\Users\\tweatherall\\Desktop\\sampleText2WITHNEWLINES.txt') as in_file:

    searchTerm = input('Enter search term: ')
    Found = 0

    for line in in_file:
        rline = line
        #print(rline)
        if searchTerm in rline:
            print('Search term found in line: ',line)
            Found = 1
    if Found == 0:
        print('Not found')
