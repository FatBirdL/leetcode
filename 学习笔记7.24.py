# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:18:42 2020

@author: Bird L
"""

###未排序数组里面的连续元素累加和等于某一个数值，这个连续元素的最长长度是多少
#1.穷举所有连续元素的排列的方法，一般都会超时，时间复杂度O(n3)
def max_length_of_sub_array_with_sum2(arr, k):
    if arr is None or len(arr) == 0:
        return 0
    ans = 0
    for i in range(len(arr)):
        current = 0
        for j in range(i, len(arr)):
            current += arr[j]
            if current == k:
                ans = max(ans, j-i+1)
    return ans
#运用双指针滑动窗口求解
def getMaxLength(arr, k):
    if arr == None or len(arr) == 0 or k < 1:
        return 0
    left = 0
    right = 0
    length = 0
    sum = arr[0]
    while left < len(arr) and right < len(arr):
        if sum == k:
            length = max(length, right-left+1)
            sum -= arr[left]
            left += 1
        elif sum > k:
            sum -= arr[left]
            left += 1
        else:
            right += 1
            if right == len(arr):
                break
            sum += arr[right]
    return length
#用哈希表（没看）
def max_length_of_sub_array_with_sum(arr, k):
    if arr is None or len(arr) == 0:
        return 0

    sum_map = {0: -1}
    current = 0
    ans = 0

    for i in range(len(arr)):
        current += arr[i]
        if current-k in sum_map:
            ans = max(ans, i-sum_map[current-k])
        if current not in sum_map:
            sum_map[current] = i

    return ans

###逆时针打印矩阵（来自笔试题，所以用了牛客的OJ）
m,n = [int(i) for i in input().split()]
a = []
for i in range(m):
    c = [int(i) for i in input().split()]
    a.append(c)
#print(a)   
def printMatrix(matrix):
        # write code here
        if not matrix:
            return []
        l,r = 0,len(matrix[0])-1
        t,b = 0,len(matrix) - 1
        res = []
        while True:
            for i in range(t,b+1):
                res.append(matrix[i][l])
            l += 1
            if l>r:
                break
            for i in range(l,r+1):
                res.append(matrix[b][i])
            b -= 1
            if t>b:
                break
            for i in range(b,t-1,-1):
                res.append(matrix[i][r])
            r -= 1
            if l>r:
                break
            for i in range(r,l-1,-1):
                res.append(matrix[t][i])
            t += 1
            if t>b:
                break
        return res
res = printMatrix(a)
res1 = []
for i in res:
    res1.append(str(i))
print(' '.join(res1))#最后这里要尤其注意它的输出是字符串类型，不能直接输出list里面的元素
###同一类型的剑指offer上的顺时针打印矩阵，思想完全一样
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        l,r,t,b = 0,len(matrix[0])-1,0,len(matrix)-1
        res = []
        while True:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t += 1
            if t>b:
                break
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r -= 1
            if l>r:
                break
            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            b -= 1
            if t>b:
                break
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l += 1
            if l>r:
                break
        return res


