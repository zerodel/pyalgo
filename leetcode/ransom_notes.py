# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

__doc__ = '''
'''
__author__ = 'zerodel'


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    dd = dict()
    for c in magazine:
        if c in dd:
            dd[c] += 1
        else:
            dd[c] = 1

    for c in ransomNote:
        if c in dd:
            dd[c] -= 1
            if dd[c] < 0:
                return False
        else:
            return False
    else:
        return True


def cons2(note, mag):
    for c in set(note):
        if note.count(c) > mag.count(c):
            return False
    else:
        return True


import timeit

print(timeit.timeit('canConstruct("aa", "aab")', globals=globals()))
print(timeit.timeit('cons2("aa", "aab")', globals=globals()))

if __name__ == "__main__":
    pass
