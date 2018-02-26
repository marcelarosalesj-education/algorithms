import time 
import random

def generate_random_list(num):
	lst = []
	lst.append(random.randint(0, 100))
	return lst

def merge_sort_my_solution(lst, ascending = True):
	# Divide
	sortedLst = []
	n = len(lst)
	if n > 1:
		firstLst = lst[0:(n/2)] 	# split, first half
		secondLst = lst[(n/2):n] 	# split, second half
		firstLst = merge_sort_my_solution(firstLst)		# call to merge_sort to sort
		secondLst = merge_sort_my_solution(secondLst)	#
		#print "firstLst = ", firstLst
		#print "secondLst = ", secondLst

		i = 0; j = 0
		for k in range(0,n):
			# Case: just one remaining
			if i == len(firstLst):
				sortedLst.append(secondLst[j])
				j = j + 1
			elif j == len(secondLst):
				sortedLst.append(firstLst[i])
				i = i + 1 
			# Case: we need to decide the smallest
			elif firstLst[i] > secondLst[j]:
				sortedLst.append(secondLst[j])
				j = j + 1
			elif firstLst[i] < secondLst[j]:
				sortedLst.append(firstLst[i])
				i = i + 1



		return sortedLst
	else:
		return lst

"""
From here: https://www.pythoncentral.io/merge-sort-implementation-guide/
"""
def mergeSort(alist):

   #print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   #print("Merging ",alist)
   return alist


unsortedLst = generate_random_list(40)
start_time = time.time()
sortedLst = merge_sort_my_solution(unsortedLst)
elapsed_time = time.time() - start_time
print "My algorithm's time = ", elapsed_time

start_time = time.time()
sortedLst = mergeSort(unsortedLst)
elapsed_time = time.time() - start_time
print "Internet's algorithm's time = ", elapsed_time
