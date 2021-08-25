# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 17:58:11 by qpupier           #+#    #+#              #
#    Updated: 2021/08/25 11:25:21 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

def	ft_round(n, p) :
	if n == int(n) :
		return str(int(n))
	n = str(n)
	size = n.find('.') + p + 1
	sign = int('-' in n)
	if size >= sign and size < len(n) and int(n[size]) >= 5 :
		i = 1.1
		tmp = p
		while tmp > 0 :
			i /= 10
			tmp -= 1
		if sign :
			i *= -1
		n = str(float(n[:size]) + i)
	result = n if size < sign or size >= len(n) else n[:size]
	if 'e' in result :
		result = "0"
	while len(result) and (result[-1] == '0' or result[-1] == '.') :
		if result[-1] == '.' :
			return result[:-1]
		result = result[:-1]
	if not result or result == "-" :
		result = "0"
	return result

def	sqrt_loop(nb, prec, tmp) :
	test = 0
	new = tmp + str(test)
	while float(new) * float(new) <= nb :
		if float(new) * float(new) == nb :
			return new
		test += 1
		new = tmp + str(test)
	test -= 1
	new = tmp + str(test)
	if prec > 0 :
		return sqrt_loop(nb, prec - 1, new)
	return new

def	ft_sqrt(nb) :
	test = 0
	while test * test < nb :
		test += 1
	if test * test == nb :
		return test
	test -= 1
	return float(sqrt_loop(nb, 15, str(test) + "."))

def	ft_pow(nb, p) :
	result = 1
	for i in range(p) :
		result *= nb
	return result
