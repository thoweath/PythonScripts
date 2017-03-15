'''
condition = 1
while condition < 10:
    print(condition)
    condition += 1
'''

exampleList = [1,2,3,4,5,6,0]
'''
for x in exampleList:
    print (x)
'''
'''
for x in range(1,11):
    print (x)
    
'''
'''
x = 3
y = 7
z = 10

if x > y:
    print(x,'is greater than',y)
elif x < z:
    print(x,'is greater than',z)
elif y < z:
    print(y, 'is greater than',z)
else:
    print ('nothing was the case')
'''

'''
if x < y:
    print (x, 'is less than',y)
else:
    print(x,'is not less than',y)
'''

'''
if x > y:
    print (x,'is greater than',y)
if x < y:
    print(x,'is less than',y)
if x == y:
    print (x,'is equal to',y)
    
if z > y > x:
    print(z,'is greater than',y,'which is greater than',x)
'''




#functions
'''
def addition(x,y):
    answer = x+y
    return answer

print(addition(3,4))
'''

'''
x =1
saveFile = open ('exampleWrite.txt','a')
while x <=10:
    writeMe = 'example text' + str(x)
    saveFile.write(writeMe)
    saveFile.write('\n')
    x += 1
saveFile.close()
'''
'''
readMe = open('exampleFile.txt','w')
readMe.write('Hi Tom')
readMe.write('\nHi Tom')
readMe.write('\nHi Tom')
readMe.write('\nHi Tom')
readMe.close()
readMe = open('exampleFile.txt','r').readlines()
#splitMe = readMe.split('\n')

print(readMe)


class calc:

    def add (x,y):
        answer = x + y
        print (answer)

    def sub(x,y):
        answer = x-y
        print(answer)

    def mult(x,y):
        answer = x*y
        print(answer)

    def div(x,y):
        answer = x/y
        print(answer)
'''

#name = input('what is your name: ')

#print('Hello',name)
'''
import statistics as s 

exList = [1,3,5,6,7,2]

x = s.mean(exList)

print(x)
'''
#from statistics import mean
#print(mean(exList))

#from statistics import mean as m, stdev as s

#print(m(exList))
'''
import exampleModule

exampleModule.exampleFunc('this is a test')
'''

'''
try:
    print('running the try...')
    import mars
    print(5+x)
except TypeError as t:
    print('Type error triggered...')
    print(str(t))
    readMe = open('ExceptionLog.txt','a')
    readMe.write(str(t))
    readMe.write('\n')
    readMe.close()
except NameError as n:
    print('Name error triggered...')
    print(str(n))
    readMe = open('ExceptionLog.txt','a')
    readMe.write(str(n))
    readMe.write('\n')
    readMe.close()
except Exception as e:
    print('general exception')
    print(str(e))
    readMe = open('ExceptionLog.txt','a')
    readMe.write(str(e))
    readMe.write('\n')
    readMe.close()
print('code continues onwards')


s  = str.upper('d')
print(s)

'''

from statistics import mean as m 

admins = {'Python':'Pass123@', 'user2':'pass2'}

studentDict = {'Jeff':[78.88,93],
               'Alex':[92,76,88],
               'Sam':[89,92,93]}

            

def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')

    print(studentDict)

def removeStudent():
    nameToRemove = input('What student to remove?: ')
    print('Removing student...')
    del studentDict[nameToRemove]
    
    print (studentDict)

def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent,'has an average grade of: ',avgGrade)
        


def main():
    print("""
    Welcome to Grade Central
    [1] - Enter Grades
    [2] - Remove Students
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input('What would you like to do today? (Enter a number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, try again!')
        main()

login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome, ',login)   
        while True:
            main()
    else:
        print('Invalid password, will detonate in 5 seconds!')
else:
    print('Invalid username, calling the FBI to report this')
            


price = 100.5
tax = 12.5/100
value = price * tax

newValue  = _ + price

print(newValue)


