#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Leetcode Q4 '

__author__ = 'Ziyan'

#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. 
#The overall run time complexity should be O(log (m+n)).

import sys

def Find_Median_Sorted_Arrays(num1, num2):
	N = len(num1) + len(num2)
	if N % 2 == 1 :
		k = N // 2 + 1
		return Get_Median(num1, num2, k)
	else :
		k = N // 2
		return (Get_Median(num1, num2, k) + Get_Median(num1,num2, k+1) ) * 0.5		


def Get_Median(num1,num2,k):
	m, n = len(num1), len(num2)
	if m > n : 
		return Get_Median(num2,num1,k)
	if m == 0 :
		return num2[k-1]
	if k == 1 :
		return min(num1[0], num2[0])
	pa = min(k//2, m) 
	pb = k - pa
	if num1[pa-1] == num2[pb-1] :
		return num1[pa-1]
	elif num1[pa-1] < num2[pb-1] :
		return Get_Median(num1[pa:], num2[:pb] , k - pa )
	else :
		return Get_Median(num1[:pa], num2[pb:], k - pb )

if __name__ == '__main__':
	print('Enter two arrays of sorted integers: ')
	num1 = input().split()
	num2 = input().split()
	num1 = list(map(lambda x:int(x) , num1))
	num2 = list(map(lambda x:int(x) , num2))
	print(Find_Median_Sorted_Arrays(num1,num2))


