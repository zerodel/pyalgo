# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
#


__doc__ = '''
'''
__author__ = 'zerodel'


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        letter_to_word = {}
        word_to_letter = {}

        letters = list(pattern)
        words = str.split()
        if not len(letters) == len(words):
            return False

        for letter, word in zip(letters, words):
            if letter in letter_to_word:
                if not word == letter_to_word[letter]:
                    return False

            if word in word_to_letter:
                if not letter == word_to_letter[word]:
                    return False
            if letter not in letter_to_word and word not in word_to_letter:
                letter_to_word[letter] = word
                word_to_letter[word] = letter
        else:
            return True


a = Solution()
print(a.wordPattern("abba", "dog dog dog dog"))

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(__doc__)
    else:
        pass
