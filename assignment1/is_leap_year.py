def is_leap_year(test_year: int) -> bool:
	# according to Gregorian formula beginning use in 1582
	assert test_year >= 1582
	if test_year % 4 == 0:
		if (test_year % 100 != 0) or (test_year % 400 == 0):
			return True
		else:
			return False
	else:
		return False


print(is_leap_year(1700))
print(is_leap_year(2000))
print(is_leap_year(2012))
print(is_leap_year(2023))
print(is_leap_year(3024))