'''
words = ['cat', 'window', 'defenstrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0,w)
        print(words)
'''    

'''
for enum in enumerate(['my','name','is','Tom']):
    print(enum)
    print(len(enum))
'''


'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
       # loop fell through without finding a factor
        print(n, 'is a prime number')


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
'''
'''
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(fib2(100))
'''
'''
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
'''
'''
will print 5, because default arguments are defined upon
function definition, so since i was first defined
as 5 then immediately referenced in the function,
the default value is 5
'''
'''
def f(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(6))
print(f(9))
'''


def cheeseshop(kind, *arguments, **keywords):
    print("-- do you have any",kind,"?")
    print("-- im sorry, we're all out of",kind)
    for args in arguments:
        print(args)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw,":",keywords[kw])
        

cheeseshop("breakfast beat","so amazzzzing sir","sooooo fucking amazing SIR", patron = "Tom", baker = "some french guy in training", time_elapsed = "too much for a sandwhich")
