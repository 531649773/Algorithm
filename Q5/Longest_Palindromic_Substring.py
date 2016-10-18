#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Leetcode Q5 '

__author__ = 'Ziyan'

# Given a string S, find the longest palindromic substring in S. 
# You may assume that the maximum length of S is 1000, 
# and there exists one unique longest palindromic substring.

import sys

def palindromic_navie(S) :
	length = []
	D = {}
	for i in range(len(S)) :
		for j in reversed(range(i+1, len(S)+1)) :
			substring = S[i:j]
			if substring == substring[::-1] :
				length.append(len(substring))
				D[len(substring)] = substring
				break
	return D[max(length)]


if __name__ == '__main__' :
	print('Enter a string: ')
	S = input()
	print(palindromic_navie(S))


