# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algo.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 17:53:04 by qpupier           #+#    #+#              #
#    Updated: 2021/07/27 18:00:58 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.degree_1 as __deg1__
from bonus.degree2.neg import degree2_neg as __neg__
from bonus.degree2.null import degree2_null as __null__
from bonus.degree2.pos import degree2_pos as __pos__

def	delta_neg(var, a, b, delta, solution) :
	if not solution :
		print()
		print("Discriminant is negative, there are 2 complex solutions :")
		print()
	p = 15
	x_r = -b / (2 * a)
	x_i = __utils__.ft_sqrt(-delta) / (2 * a)
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

def	delta_pos(var, a, b, delta, solution) :
	if not solution :
		print()
		print("Discriminant is positive, there are 2 solutions :")
		print()
	p = 15
	x1 = (-b - __utils__.ft_sqrt(delta)) / (2 * a)
	x2 = (-b + __utils__.ft_sqrt(delta)) / (2 * a)
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

def	degree_1(var, a, b, solution) :
	x = -b / a
	s = __utils__.ft_round(x, 15)
	if not solution :
		print("Polynomial degree : 1")
		print()
		print(var + " = " + s)
		print()
	print("\033[33;1mS = {", end="")
	print(s, end="")
	print("}\033[0m")

def	resolve(equation, var, a, b, c, p, verbose, solution) :
	if a :
		if verbose :
			print("Polynomial degree : 2")
			print()
			print("Δ = b^2 - 4ac")
			print("Δ = " + __utils__.ft_round(b, p) + "^2 - 4 * " + __utils__.ft_round(a, p) + " * " + __utils__.ft_round(c, p))
			print("  = " + __utils__.ft_round(b, p) + " * " + __utils__.ft_round(b, p) + " - 4 * " + __utils__.ft_round(a, p) + " * " + __utils__.ft_round(c, p))
			print("  = " + __utils__.ft_round(b * b, p * 2) + " - " + __utils__.ft_round(4 * a, p) + " * " + __utils__.ft_round(c, p))
			print("  = " + __utils__.ft_round(b * b, p * 2) + " - " + __utils__.ft_round(4 * a * c, p))
			print()
		delta = b * b - 4 * a * c
		p *= 2
		if not solution :
			print("Δ = " + __utils__.ft_round(delta, p * 2))
		if verbose :
			if delta < 0 :
				s1, s2 = __neg__.delta_neg(var, a, b, delta, p)
			elif not delta :
				s1, s2 = __null__.delta_null(var, a, b, p)
			else :
				s1, s2 = __pos__.delta_pos(var, a, b, delta, p)
			print("\033[36;1m")
			print("S = {" + s1, end="")
			if s2 :
				print(", " + s2, end="")
			print("}\033[0m")
		else :
			if delta < 0 :
				delta_neg(var, a, b, delta, solution)
			elif not delta :
				delta_null(var, a, b, solution)
			else :
				delta_pos(var, a, b, delta, solution)
	elif b :
		if verbose :
			__deg1__.degree_1_bonus(equation, var, p)
		else :
			degree_1(var, b, c, solution)
	elif c :
		if not solution :
			print("Polynomial degree : 0")
			print()
			print("There are no solutions")
			print()
		print("\033[33;1mS = ∅\033[0m")
	else :
		if not solution :
			print("Polynomial degree : 0")
			print()
			print("All numbers are solutions")
			print()
		print("\033[33;1mS = ℝ\033[0m")
