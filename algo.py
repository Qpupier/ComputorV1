# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algo.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 17:53:04 by qpupier           #+#    #+#              #
#    Updated: 2021/06/07 18:37:13 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__

def	delta_neg(var, a, b, p, delta) :
	x_r = -b / (2 * a)
	x_i = __utils__.ft_sqrt(-delta, p) / (2 * a)
	print(var + "1 = " + __utils__.ft_round(x_r, p) + " - i * " + __utils__.ft_round(x_i, p))
	print(var + "2 = " + __utils__.ft_round(x_r, p) + " + i * " + __utils__.ft_round(x_i, p))
	return

def	delta_null(var, a, b, p, delta) :
	x = -b / (2 * a)
	print(var + " = " + __utils__.ft_round(x, p))
	return

def	delta_pos(var, a, b, p, delta) :
	x1 = (-b - __utils__.ft_sqrt(delta, p)) / (2 * a)
	x2 = (-b + __utils__.ft_sqrt(delta, p)) / (2 * a)
	print(var + "1 = " + __utils__.ft_round(x1, p))
	print(var + "2 = " + __utils__.ft_round(x1, p))
	return

def	resolve(var, a, b, c, p, verbose) :
	# if a :
		if verbose :
			print("Δ = " + __utils__.ft_round(b, p) + "^2 - 4 * " + __utils__.ft_round(a, p) + " * " + __utils__.ft_round(c, p))
			print("  = " + __utils__.ft_round(b, p) + " * " + __utils__.ft_round(b, p) + " - 4 * " + __utils__.ft_round(a, p) + " * " + __utils__.ft_round(c, p))
			print("  = " + __utils__.ft_round(b * b, p * 2) + " - " + __utils__.ft_round(4 * a, p) + " * " + __utils__.ft_round(c, p))
			print("  = " + __utils__.ft_round(b * b, p * 2) + " - " + __utils__.ft_round(4 * a * c, p))
			print()
		delta = b * b - 4 * a * c
		p *= 2
		print("Δ = " + __utils__.ft_round(delta, p * 2))
		if delta < 0 :
			delta_neg(var, a, b, p, delta)
		elif not delta :
			delta_null(var, a, b, p, delta)
		else :
			delta_pos(var, a, b, p, delta)
