def ft_round(n, p) :
	if n == int(n) or not p :
		return str(int(n))
	n = str(n)
	sign = int('-' in n)
	size = n.find('.') + p + 1
	if size >= 0 and size < len(n) and int(n[size]) >= 5 :
		i = 1.0000000000001
		tmp = p
		while tmp > 0 :
			i /= 10
			tmp -= 1
		if sign :
			i *= -1
		n = str(float(n) + i)
	result = n if size < 0 or size >= len(n) else n[:size]
	while len(result) and (result[-1] == '0' or result[-1] == '.') :
		if result[-1] == '.' :
			return result[:-1]
		result = result[:-1]
	return result

print(ft_round(14.099996, 2))
print(ft_round(-14, 0))