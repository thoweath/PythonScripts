import re
#
# class slist(list):
#     @property
#     def length(self):
#         return len(self)


expression  = input('Enter expression to search for: ')

ls = ['this','is','just','a','test','test']

regex = re.compile(expression)
matches = []
matches += (term for term in ls if re.match(regex,term))

if len(matches) > 0 :
    print('Match found')
else:
    print('No match')

print(len(matches))
print(matches)
# if matches:
#     print('No matches')
# else:
#     print('Match found: ',matches)
