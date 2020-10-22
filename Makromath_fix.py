"""Makroscale->Fixture"""

def Mat_makro1k(func):
    def mk1k(*args):
        y=1000
        x=func(*args)
        func(*args)
        return round(((x/y)*100), 5)
    return mk1k

def Mat_makro10k(func):
    def mk1k(*args):
        y=10000
        x=func(*args)
        func(*args)
        return round(((x/y)*100), 5)
    return mk1k

def Mat_makro100k(func):
    def mk1k(*args):
        y=100000
        x=func(*args)
        func(*args)
        return round(((x/y)*100), 5)
    return mk1k

def Mat_makro1mln(func):
    def mk1k(*args):
        y=1000000
        x=func(*args)
        func(*args)
        return round(((x/y)*100), 5)
    return mk1k

def Mat_makro10mln(func):
    def mk1k(*args):
        y=10000000
        x=func(*args)
        func(*args)
        return round(((x/y)*100), 5)
    return mk1k

def Mat_makro100mln(func):
    def mk1k(*args):
        y=100000000
        x=func(*args)
        func(*args)
        return round(((x/y)*100), 5)
    return mk1k

def Mat_makro1mld(func):
    def mk1k(*args):
        y=1000000000
        x=func(*args)
        func(*args)
        return round(((x/y)*100), 5)
    return mk1k

def Mat_makro10mld(func):
    def mk1k(*args):
        y=10000000000
        x=func(*args)
        func(*args)
        return round(((x/y)*100), 5)
    return mk1k

def Mat_makro100mld(func):
    def mk1k(*args):
        y=100000000000
        x=func(*args)
        func(*args)
        return round(((x/y)*100), 5)
    return mk1k

def Mat_makro1T(func):
    def mk1k(*args):
        y=1000000000000
        x=func(*args)
        func(*args)
        return round(((x/y)*100), 5)
    return mk1k