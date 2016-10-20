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
	MR, pos, Maxlen = 0, 0, 0
	for i in range(0,len(S)//2+1) :

		if i < MR :
			P[i] = min(P[2*pos - i], 2*(MR - i)+1)
		else :
			P[i] = 1

		if S[2*i-1] == S[1] :
			while i-P[i]//2 >0 and i+P[i]//2 < len(S)-1 and S[i-P[i]//2] == S[i+P[i]//2]:
				P[i] += 2

		if P[i]//2 + i -1 > MR :
			MR = P[i]//2 + i - 1
			pos = i

		if P[i] > Maxlen :
			Maxlen = P[i]
			if i - P[i]//2 == 0 :
				#temp_center = i
				temp_len = Maxlen
				
	#Maxsubstr = S[temp_center-temp_len//2 +1 : temp_center+ temp_len//2 : 2]
	res = S[temp_len:: 2]
	res = res[::-1]
	return res



if __name__ == '__main__' :
	print('Enter a string: ')
	S = input()
	print(shortest_palindromic(S))


