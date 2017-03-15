import re

class DictTest4:
    d = {}

    with open('C:\\Users\\tweatherall\\Desktop\\PythonScripts\\Input_Output_Test_Files\\IPTestFile.txt','r') as file:
        for line in file:
            #key = str(re.findall('\d{3}[.]\d{3}[.]\d{1}[.]\d{1}',line))
            key = str(re.search('\d{3}[.]\d{3}[.]\d{1}[.]\d{1}',line).group())
            #d[key] = re.findall('[^\s\d]\D+[^\d+.]',line)
            d[key] = re.search('[^\s\d]\D+[^\d+.][^\n]',line).group()

    print(d)

if __name__   == "__main__":
    DictTest4()


    
