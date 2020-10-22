"""Macroscale->Usable Easy Program"""
def makroCalcpr(func):
    def ifif(*args):
        if func(*args)<=1000:
            def mk1k(*args):
                y=1000
                x=func(*args)
                func(*args)
                return print(f'{round(((x/y)*100), 5)}% from 1 000')
            return mk1k()
        elif func(*args)>1000 and func(*args)<=10000:
            def mk1k(*args):
                y=10000
                x=func(*args)
                func(*args)
                return print(f'{round(((x/y)*100), 5)}% from 10 000')
            return mk1k()
        elif func(*args)>10000 and func(*args)<=100000:
            def mk1k(*args):
                y=100000
                x=func(*args)
                func(*args)
                return print(f'{round(((x/y)*100), 5)}% from 100 000')
            return mk1k()
        elif func(*args)>100000 and func(*args)<=1000000:
            def mk1k(*args):
                y=1000000
                x=func(*args)
                func(*args)
                return print(f'{round(((x/y)*100), 5)}% from 1 000 000')
            return mk1k()
        elif func(*args)>1000000 and func(*args)<=10000000:
            def mk1k(*args):
                y=10000000
                x=func(*args)
                func(*args)
                return print(f'{round(((x/y)*100), 5)}% from 10 000 000')
            return mk1k()
        elif func(*args)>10000000 and func(*args)<=100000000:
            def mk1k(*args):
                y=100000000
                x=func(*args)
                func(*args)
                return print(f'{round(((x/y)*100), 5)}% from 100 000 000')
            return mk1k()
        elif func(*args)>100000000 and func(*args)<=1000000000:
            def mk1k(*args):
                y=1000000000
                x=func(*args)
                func(*args)
                return print(f'{round(((x/y)*100), 5)}% from 1 000 000 000')
        elif func(*args)>1000000000 and func(*args)<=10000000000:
            def mk1k(*args):
                y=10000000000
                x=func(*args)
                func(*args)
                return print(f'{round(((x/y)*100), 5)}% from 10 000 000 000')
            return mk1k()
        elif func(*args)>10000000000 and func(*args)<=100000000000:
            def mk1k(*args):
                y=100000000000
                x=func(*args)
                func(*args)
                return print(f'{round(((x/y)*100), 5)}% from 100 000 000 000')
            return mk1k()
        elif func(*args)>100000000000 and func(*args)<=1000000000000:
            def mk1k(*args):
                y=1000000000000
                x=func(*args)
                func(*args)
                return print(f'{round(((x/y)*100), 5)}% from 1 000 000 000 000')
            return mk1k()
    return ifif