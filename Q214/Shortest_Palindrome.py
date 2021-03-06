#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Leetcode Q5 '

__author__ = 'Ziyan'

# Given a string S, find the longest palindromic substring in S. 
# You may assume that the maximum length of S is 1000, 
# and there exists one unique longest palindromic substring.

import sys

def shortest_palindromic(s):
	#adopt the idea from find the longest palindromic substring(LPS)
	#find the LPS with the left element is the same as the very left element of the input string
	S = '#' + '#'.join(s) + '#'

	P = [0] * len(S)
	ML, pos, Maxlen = 0, 0, 0
	for i in range(len(S)//2, 0 ,-1) :

		if i > ML :
			P[i] = min(P[2*pos - i], 2*(i - ML)+1)
		else :
			P[i] = 1

		if S[2*i-1] == S[1] :
			while i-P[i]//2 >0 and i+P[i]//2 < len(S)-1 and S[i-P[i]//2] == S[i+P[i]//2]:
				P[i] += 2
			if i - P[i]//2 <= 1 :
				# if we have the LPS starting from the first char of s, then break
				temp_len = i + P[i]//2 +1
				break

		if i - P[i]//2  < ML :
			ML = i - P[i]//2 
			pos = i

		if P[i] > Maxlen :
			Maxlen = P[i]
				
	#Maxsubstr = S[temp_center-temp_len//2 +1 : temp_center+ temp_len//2 : 2]
	res = S[temp_len:: 2]
	res = res[::-1]
	return res + s



if __name__ == '__main__' :
	print('Enter a string: ')
	S = input()
	print(shortest_palindromic(S))


