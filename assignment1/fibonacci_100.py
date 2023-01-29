def fibonacci_100() -> list[int]:
	old_num, new_num = 1, 1
	fibonacci_list = []
	for i in range(0, 100):
		fibonacci_list.append(old_num)
		old_num, new_num = new_num, (old_num + new_num)
	return fibonacci_list


assert len(fibonacci_100()) == 100
print(fibonacci_100())
