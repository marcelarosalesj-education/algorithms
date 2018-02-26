def merge_sort(lst, ascending = True):
	# Divide
	sortedLst = []
	n = len(lst)
	if n > 1:
		firstLst = lst[0:(n/2)] 	# split, first half
		secondLst = lst[(n/2):n] 	# split, second half
		firstLst = merge_sort(firstLst)		# call to merge_sort to sort
		secondLst = merge_sort(secondLst)	#
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

unsortedLst = [4,8,10,3,1,7,5,2,9,6]
sortedLst = merge_sort(unsortedLst)
print "unsorted = ", unsortedLst
print "sorted   = ", sortedLst 
