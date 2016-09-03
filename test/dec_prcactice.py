# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = '''
========================================================
practice for decorator in Python
'''
__author__ = 'zerodel'


def func1():
    print("func1....")




def deco(func):
    print("a porior to inside function  ....")
    func()
    print("a post  , .... func")
    return func



@deco
def func2():
    print("this is func2>>> ")


def deco_inline(func):
    def _inner_deco():
        print("a prior call ...")
        func()
        print("a post call ....")

    return _inner_deco

@deco_inline
def func3():
    print("this is the 3rd function ")

# decorate functions with parameter .
def deco_p(func):
    def _innner_deco(*args, **kwargs):
        print("----- a prior call to function")
        func(*args, **kwargs)
        print("----- a post call to function")

    return _innner_deco

@deco_p
def my_func(a, b):
    print("arguments : {a}, and {b}".format(a = a,
                                            b = b))

@deco_p
def my_fun_m_p(a, b, c ):
    print(repr(a), repr(b), repr(c))

# decorator with arguments in decorator itself.
def deco_times(pd):
    def _deco_fun(func):
        def _inner_fun(*args, **kwargs):
            print("a prior call to {}".format(func.__name__))
            for x in range(pd):
                func(*args, **kwargs)
            print("after invoking the function : {}".format(func.__name__))
        return _inner_fun
    return _deco_fun







# # -----------------------------------------------------------------
# # function invoking here.
print("----simple decorator-----")
a = deco(func1)

print("----- using syntax sugar ----")
func2()

print("----- using a nest function , to make sure a new function will be invoked each time -----")
func3()

print("------------------------------ using a nest function , and this function has two arguments")
my_func("a", "b")


print("----- nest function , with unlimited arguments")
my_fun_m_p("a,", "b", "c")

print("----- decorator has its own arguments-----")

@deco_times(3)
def myfunc(x):
    print("x is {}".format(str(x)))

myfunc("9")




if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
