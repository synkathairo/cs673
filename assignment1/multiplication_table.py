def multiplication_table(n: int):
	if n > 12:
		return
	index_list: list = list(range(1, n + 1))
	for i in range(1, n + 1):
		[
			print(" " * (3 - len(str(index * i))), index * i, end=" ")
			for index in index_list
		]
		print()


for i in range(1, 13):
	multiplication_table(i)
	print()
