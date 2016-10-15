#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Leetcode Q1 Two Sum'
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution.'

__author__ = 'Ziyan'

import sys

def two_sum_mostslow(nums, tar) :
	upper = len(nums)
	flag = False
	for i in range(upper-1) :
		for j in range(i,upper) :
			summa = nums[i] + nums[j]
			if summa == tar :
				flag = True
				break
		if flag:
			break
	return [i,j]

def two_sum_slow(nums, tar) :
	upper = len(nums)
	index = list(range(upper))
	dic={}
	for i in range(upper) :
		dic[i] = nums[i]
	print(dic)
	for i in range(upper) :
		dic.pop(i)
		res = tar - nums[i]
		j = dic.get(res)
		if j != None :
			return [i,j]
			break
	return [-1,-1]

def twoSum(nums, target) :
        #set up an empty dictionary
        d = {}
        #run all possible number in the list and store them as a key in the dictionary
        for i in range(len(nums)) :
        	res = target - nums[i]
        	try :
        		ans = [d[res],i]
        	except :
        		d[nums[i]] = i 
        	else :
        		return ans
        #no solution
        return [-1, -1]

if __name__ == '__main__':
	print('Please enter an array of integers:')
	nums = input().split()
	nums = list(map(lambda x:int(x), nums))
	print('Please enter a target integer:')
	target = int(input())
	print(twoSum(nums,target))

