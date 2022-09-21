# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 08:05:52 2022

@author: xzajic22
"""

import matplotlib.pyplot as plt
from functools import wraps
import time as tm
import random as rnd

global results
global start
start=0
results = {}
#decorator that calculates execution time of function in miliseconds
def time(x):
    @wraps(x)
    def time_wrapper(*args,**kwargs):
        start=tm.perf_counter_ns()
        res=x(*args,**kwargs)
        end=tm.perf_counter_ns()
        total_time=int((end-start)/1000)
        results[x.__name__]=total_time
        return res
    return time_wrapper
    
#function to create randomized array of numbers
#takes arg x as the lenght of array
def randarr(x):
    arr=[]
    while x>0:
        arr.append(rnd.randint(x*-100,x*100))
        x-=1
    return arr

def isSorted(arr):
    n=len(arr)
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            return False
    return True

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
@time
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

@time
def quicksort(arr,low,high):
    if low < high:
      pi = partition(arr, low, high)
      quicksort(arr, low, pi - 1)  
      quicksort(arr, pi + 1, high)

@time
def mergesort(arr):
    n=len(arr)
    if n> 1:
       mid = n//2
       L = arr[:mid]
       R = arr[mid:]
       mergesort(L)
       mergesort(R)
       i = j = k = 0
       # Copy data to temp arrays L[] and R[]
       while i < len(L) and j < len(R):
           if L[i] < R[j]:
               arr[k] = L[i]
               i += 1
           else:
               arr[k] = R[j]
               j += 1
           k += 1
       while i < len(L):
           arr[k] = L[i]
           i += 1
           k += 1
       while j < len(R):
           arr[k] = R[j]
           j += 1
           k += 1

@time
def shellsort(arr):
    n=len(arr)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
        interval //= 2

@time
def insertsort(arr):
    for i in range(1, len(arr)):
       key = arr[i]
       j = i-1
       while j >= 0 and key < arr[j] :
               arr[j + 1] = arr[j]
               j -= 1
       arr[j + 1] = key
       
@time
def radixsort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
        
#this is really trash algorithm
@time
def bogosort(arr):
    while not isSorted(arr):
        rnd.shuffle(arr)

#main function for rendering graph
def sorts():
    x=list(results.keys())
    y=list(results.values())
    plt.figure(dpi=600)
    plt.style.use('seaborn-darkgrid')
    plt.ylabel("time in microseconds")
    plt.fill_between(x,y,color="skyblue",alpha=0.4)
    plt.plot(x,y,color="lime",alpha=0.2)
    plt.plot(x,y,"go")
    try:
        plt.savefig('plots/plot.png')
    except:
        plt.savefig('plot.png')
    e=tm.perf_counter_ns()
    r=(e-start)/10**9
    print(f'The program took {r:.9f} seconds')