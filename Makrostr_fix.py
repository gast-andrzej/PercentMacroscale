"""Makroscale->Fixture"""

def makro1k(func):
    def mk1k(*args):
        y=1000
        x=func(*args)
        func(*args)
        return print(f'{round(((x/y)*100), 5)}%')
    return mk1k

def makro10k(func):
    def mk1k(*args):
        y=10000
        x=func(*args)
        func(*args)
        return print(f'{round(((x/y)*100), 5)}%')
    return mk1k

def makro100k(func):
    def mk1k(*args):
        y=100000
        x=func(*args)
        func(*args)
        return print(f'{round(((x/y)*100), 5)}%')
    return mk1k

def makro1mln(func):
    def mk1k(*args):
        y=1000000
        x=func(*args)
        func(*args)
        return print(f'{round(((x/y)*100), 5)}%')
    return mk1k

def makro10mln(func):
    def mk1k(*args):
        y=10000000
        x=func(*args)
        func(*args)
        return print(f'{round(((x/y)*100), 5)}%')
    return mk1k

def makro100mln(func):
    def mk1k(*args):
        y=100000000
        x=func(*args)
        func(*args)
        return print(f'{round(((x/y)*100), 5)}%')
    return mk1k

def makro1mld(func):
    def mk1k(*args):
        y=1000000000
        x=func(*args)
        func(*args)
        return print(f'{round(((x/y)*100), 5)}%')
    return mk1k

def makro10mld(func):
    def mk1k(*args):
        y=10000000000
        x=func(*args)
        func(*args)
        return print(f'{round(((x/y)*100), 5)}%')
    return mk1k

def makro100mld(func):
    def mk1k(*args):
        y=100000000000
        x=func(*args)
        func(*args)
        return print(f'{round(((x/y)*100), 5)}%')
    return mk1k

def makro1T(func):
    def mk1k(*args):
        y=1000000000000
        x=func(*args)
        func(*args)
        return print(f'{round(((x/y)*100), 5)}%')
    return mk1k