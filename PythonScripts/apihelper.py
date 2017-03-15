

def info(object,spacing=10,collapse=1):
    """
    Print methods and doc strings. Take modules, class, list, dictionary
    or string.
    """

    methodList = [method for method in dir(object) if callable(getattr(object,method))]
    processFunc = collapse and (lambda s: ''.join(s.split())) or (lambda s: s)
    print('\n'.join(['{}{}'.format(method.ljust(spacing), processFunc(str(getattr(object, method).__doc__))) for method in methodList]))

if __name__ == "__main__":
    print(info.__doc__)
