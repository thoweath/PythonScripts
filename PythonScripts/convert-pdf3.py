import pdftables_api
import os
import os.path
import re


# product key
c = pdftables_api.Client('2q59lxgi1k46')


path = input('Enter PDF File Path: ')
outputPDF = input('Enter PDF File Output Path: ')

# outputPDF2 = str.replace(outputPDF,'\\','\\\\')
#

filenames = [re.search('.+[.]',f).group() for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]


for f in filenames:
    c.xlsx(os.path.join(path,f) + 'pdf',os.path.join(path,f) + 'xlsx')
