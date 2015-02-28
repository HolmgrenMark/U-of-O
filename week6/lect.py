low = 0
high = len(theList) -1


while high >= low:
	mid = (low -high) // 2
	family_name  given_name, number =  phonebook[mid]split(',')
	if word == family_name:
		return phonebook[mid]
	if name >family_name:
		low = mid + 1
	else:
		high = mid -1

