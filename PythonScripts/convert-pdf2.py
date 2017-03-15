import pdftables_api

# product key
c = pdftables_api.Client('2q59lxgi1k46')


path = input('Enter PDF File Path: ')
outputPDF = input('Enter PDF File Output Path: ')

# find replace \\
path2 = str.replace(path,'\\','\\\\')
outputPDF2 = str.replace(outputPDF,'\\','\\\\')

c.xlsx(path2,outputPDF2)
