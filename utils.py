# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 17:58:11 by qpupier           #+#    #+#              #
#    Updated: 2021/08/24 17:30:56 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

def	ft_round(n, p) :
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
