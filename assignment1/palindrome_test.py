def palindromeTest(test_str: str) -> bool:
	if test_str[0] != test_str[-1]:
		return False
	else:
		return palindromeTest(test_str[1:-1]) if len(test_str) > 3 else True


print("test 'amanaplanacanalpanama' expect True:")
print(palindromeTest("amanaplanacanalpanama"))
print("test 'cat' expect False:")
print(palindromeTest("cat"))
