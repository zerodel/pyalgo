# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#



__doc__ = ''' Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

click to show corner cases.
Corner Cases:

    Did you consider the case where path = "/../"?
    In this case, you should return "/".
    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
'''
__author__ = 'zerodel'


class Solution(object):
    pass


# def simplifyPath(path):
#     """
#     :type path: str
#     :rtype: str
#     """
#     stk = []
#     res = []
#     for x in reversed(path.split("/")):
#         if x == "..":
#             stk.append(x)
#             continue
#         elif x == ".":
#             continue
#         elif x:
#             if stk:
#                 stk.pop()
#             else:
#                 res.append(x)
#
#     return "/" + "/".join(reversed(res))

def simplifyPath(path):
    res = []
    for x in path.split("/"):
        if x == "..":
            if res:
                res.pop()
        elif x == ".":
            continue
        elif x:
            res.append(x)

    return "/" + "/".join(res)


print(simplifyPath("/home/"))
print(simplifyPath("/../"))
print(simplifyPath("/a/./b/../../c/"))

if __name__ == "__main__":
    pass
