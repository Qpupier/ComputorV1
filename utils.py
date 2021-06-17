# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 17:58:11 by qpupier           #+#    #+#              #
#    Updated: 2021/06/17 13:57:40 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

def	ft_round(n, p) :
	r = round(n, p)
	if r == int(r) :
		r = int(r)
	return str(r)

def	sqrt_loop(nb, prec, tmp) :
	# print(nb, prec, tmp)
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
