def bubblesort(L):

	for i in range(len(L)-1):
		for j in range(len(L) - i -1):
			if L[j] > L[j+1]:
				temp = L[j]
				L[j] = L[j+1]
				L[j+1] = temp
			
	return L

		#for i in range(-1,234,3)



L = [1,32,4,12,5,2,7]
print bubblesort(L)
