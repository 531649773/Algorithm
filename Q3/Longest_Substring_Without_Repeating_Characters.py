#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Leetcode Q3 '

__author__ = 'Ziyan Zhu'

#Given a string, find the length of the longest substring without repeating characters.

import sys

def longest_substring(string):

	Distance = 0
	D = {}
	start = 0
	for i in range(len(string)):
		char = string[i]
		if char in D and D[char] >= start :
			Distance = max(Distance, i - start )
			start = D[char] + 1			
		else:
			D[char] = i
	return Distance

if __name__ == '__main__':
	print('Enter some letters')
	string = input()
	print(longest_substring(string))
		



