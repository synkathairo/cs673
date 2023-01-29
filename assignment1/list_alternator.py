def list_alternator(list1: list, list2: list) -> list:
	# assuming two lists have equivalent length
	assert len(list1) == len(list2)
	result_list = []
	for i in range(0, len(list1)):
		result_list.append(list1[i])
		result_list.append(list2[i])
	return result_list


print(list_alternator(["a", "b", "c"], [1, 2, 3]))
