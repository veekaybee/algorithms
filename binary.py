

"""
Binary search implementation in Python 2.7
From Grokking Algorithms by Bhargava
"""



sorted_list = list(raw_input("Enter a list of numbers>"))
print sorted_list
position = raw_input("Which number's position would you like to look up? >")


def binary_search(list, item): #uses Python list - array - as input
	low = 0
	high = len(list) - 1 #ordinal/cardinal

	while low <= high:
		mid = (low + high)
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1 
		else:
			low = mid + 1
	return None #if item is not in list



print binary_search(sorted_list, position)
