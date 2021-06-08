# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algo.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 17:53:04 by qpupier           #+#    #+#              #
#    Updated: 2021/06/08 15:32:59 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__

def	delta_neg(var, a, b, delta, solution) :
	if not solution :
		print()
		print("Discriminant is negative, there are 2 complex solutions :")
		print()
	p = 15
	x_r = -b / (2 * a)
	x_i = __utils__.ft_sqrt(-delta, p) / (2 * a)
	s1 = __utils__.ft_round(x_r, p) + " - i * " + __utils__.ft_round(x_i, p)
	s2 = __utils__.ft_round(x_r, p) + " + i * " + __utils__.ft_round(x_i, p)
	if not solution :
		print(var + "1 = " + s1)
		print("and")
		print(var + "2 = " + s2)
		print()
	print("\033[33;1mS = {", end="")
	print(s1, end=", ")
	print(s2, end="")
	print("}\033[0m")
	return

def	delta_null(var, a, b, solution) :
	if not solution :
		print()
		print("Discriminant is null, there is 1 solution :")
		print()
	p = 15
	x = -b / (2 * a)
	s = __utils__.ft_round(x, p)
	if not solution :
		print(var + " = " + s)
	print("\033[33;1mS = {", end="")
	print(s, end="")
	print("}\033[0m")
	return

def	delta_pos(var, a, b, delta, solution) :
	if not solution :
		print()
		print("Discriminant is positive, there are 2 solutions :")
		print()
	p = 15
	x1 = (-b - __utils__.ft_sqrt(delta, p)) / (2 * a)
	x2 = (-b + __utils__.ft_sqrt(delta, p)) / (2 * a)
	s1 = __utils__.ft_round(x1, p)
	s2 = __utils__.ft_round(x2, p)
	if not solution :
		print(var + "1 = " + s1)
		print("and")
		print(var + "2 = " + s2)
	print("\033[33;1mS = {", end="")
	print(s1, end=", ")
	print(s2, end="")
	print("}\033[0m")
	return

def	resolve(var, a, b, c, p, verbose, solution) :
	if a :
		if verbose :
			print("Δ = " + __utils__.ft_round(b, p) + "^2 - 4 * " + __utils__.ft_round(a, p) + " * " + __utils__.ft_round(c, p))
			print("  = " + __utils__.ft_round(b, p) + " * " + __utils__.ft_round(b, p) + " - 4 * " + __utils__.ft_round(a, p) + " * " + __utils__.ft_round(c, p))
			print("  = " + __utils__.ft_round(b * b, p * 2) + " - " + __utils__.ft_round(4 * a, p) + " * " + __utils__.ft_round(c, p))
			print("  = " + __utils__.ft_round(b * b, p * 2) + " - " + __utils__.ft_round(4 * a * c, p))
			print()
		delta = b * b - 4 * a * c
		p *= 2
		if not solution :
			print("Δ = " + __utils__.ft_round(delta, p * 2))
		if delta < 0 :
			delta_neg(var, a, b, delta, solution)
		elif not delta :
			delta_null(var, a, b, solution)
		else :
			delta_pos(var, a, b, delta, solution)
