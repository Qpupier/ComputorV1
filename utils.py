# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 17:58:11 by qpupier           #+#    #+#              #
#    Updated: 2021/06/11 18:17:19 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

def	ft_round(n, p) :
	r = round(n, p)
	if r == int(r) :
		r = int(r)
	return str(r)

def	sqrt_loop(nb, prec, tmp) :
	test = 0
	new = float(tmp + str(test))
	while new * new <= nb :
		if new * new == nb :
			return new
		test += 1
		new = float(tmp + str(test))
	test -= 1
	new = float(tmp + str(test))
	if prec > 0 :
		return sqrt_loop(nb, prec - 1, str(new))
	return new

def	ft_sqrt(nb) :
	test = 0
	while test * test < nb :
		test += 1
	test -= 1
	return sqrt_loop(nb, 11, str(test) + ".")

def	ft_pow(nb, p) :
	result = 1
	for i in range(p) :
		result *= nb
	return result
