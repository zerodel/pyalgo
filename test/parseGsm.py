# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
# 
import bs4 


__doc__ = ''' 
'''
__author__ = 'zerodel'

fr = "./acc.cgi?acc=GSM1298123"

with open(fr) as frr:
    ent = frr.read()
    print(len(ent))

if __name__ == "__main__":
    pass