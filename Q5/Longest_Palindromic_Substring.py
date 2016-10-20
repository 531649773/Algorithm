#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Leetcode Q5 '

__author__ = 'Ziyan'

# Given a string S, find the longest palindromic substring in S. 
# You may assume that the maximum length of S is 1000, 
# and there exists one unique longest palindromic substring.

import sys

def palindromic(S) :
	# O(n^2)
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

def palindromic_Manacher(s):

	S = '#' + '#'.join(s) + '#'

	P = [0] * len(S)
	MR, pos, Maxlen = 0, 0, 0
	for i in range(0,len(S)) :

		if i < MR :
			P[i] = min(P[2*pos - i], 2*(MR - i)+1)
		else :
			P[i] = 1

		while i-P[i]//2 >0 and i+P[i]//2 < len(S)-1 and S[i-P[i]//2] == S[i+P[i]//2]:
			P[i] += 2

		if P[i]//2 + i -1 > MR :
			MR = P[i]//2 + i - 1
			pos = i

		if P[i] > Maxlen :
			Maxlen = P[i]
			center = i
			
	Maxsubstr = S[center-Maxlen//2 +1 : center+ Maxlen//2 : 2]
		#Maxlen = max(Maxlen,P[i])

	return Maxsubstr, len(Maxsubstr)



if __name__ == '__main__' :
	print('Enter a string: ')
	S = input()
	print(palindromic_Manacher(S))


