# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    verbose.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/05 18:16:01 by qpupier           #+#    #+#              #
#    Updated: 2021/06/08 19:49:27 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__

def	print_var(a, x, begin) :
	if a == 1 :
		if begin :
			print(x, end="")
		else :
			print(" + " + x, end="")
	elif a == -1 :
		if begin :
			print("-" + x, end="")
		else :
			print(" - " + x, end="")
	elif begin :
		print(__utils__.ft_round(a, precision) + x, end="")
	elif a < 0 :
		print(" - " + __utils__.ft_round(-a, precision) + x, end="")
	else :
		print(" + " + __utils__.ft_round(a, precision) + x, end="")

def	print_part(part) :
	display = False
	begin = True
	for var in part :
		a = var[0]
		if a == int(a) :
			a = int(a)
		if var[1] :
			x = var[1][0]
			n = var[1][1]
			if n == int(n) :
				n = int(n)
		if a :
			if not (var[1] and n) :
				if begin :
					print(__utils__.ft_round(a, precision), end="")
				elif a < 0 :
					print(" - " + __utils__.ft_round(-a, precision), end="")
				else :
					print(" + " + __utils__.ft_round(a, precision), end="")
			elif n == 1 :
				print_var(a, x, begin)
			else :
				print_var(a, x + "^" + __utils__.ft_round(n, precision), begin)
			begin = False
			display = True
	if not display :
		print("0", end="")

def print_step(part1, part2, first, p) :
	global precision
	precision = p
	if not first :
		print("<=>	", end="")
	else :
		print("	", end="")
	print_part(part1)
	if part2 :
		print(" = ", end="")
		print_part(part2)
	else :
		print(" = 0", end="")
	print()
