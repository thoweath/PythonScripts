"""
Creates a DictTest class with the file raeder method, then instantiates an
object which has an attribute (testFile) and fRead method for reading the
testFile.
"""
import re

class DictTest4:

    def __init__(self,f):
        self.testFile = f

    def fRead(self,filename):
        d = {}
        with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\' + filename,'r') as file:
            for line in file:
                #key = str(re.findall('\d{3}[.]\d{3}[.]\d{1}[.]\d{1}',line))
                key = str(re.search('\d{3}[.]\d{3}[.]\d{1}[.]\d{1}',line).group())
                #d[key] = re.findall('[^\s\d]\D+[^\d+.]',line)
                d[key] = re.search('[^\s\d]\D+[^\d+.][^\n]',line).group()
        return d
                #print(d)

if __name__   == "__main__":
    filename = input('Enter filename: ')
    x = DictTest4(filename)
    y = x.testFile[::-1]
    print('Filename backwards:',y)
    print(x.fRead(filename))
    #print(x.fRead(filename))
