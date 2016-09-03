# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#
__doc__ = '''
'''
__author__ = 'zerodel'

class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self


x = 1
y = 3

point = Bunch(datum=y, squared=y*y, coord=x)
print("coord" in point)




if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
