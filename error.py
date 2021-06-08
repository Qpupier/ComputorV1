# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    error.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 13:27:41 by qpupier           #+#    #+#              #
#    Updated: 2021/06/08 19:19:10 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import computor as __computor__
import pre_reduce as __pre_reduce__
import utils as __utils__

def	print_var(a, x, begin, precision) :
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
		print(str(a) + x, end="")
	elif a < 0 :
		print(" - " + __utils__.ft_round(-a, precision) + x, end="")
	else :
		print(" + " + __utils__.ft_round(a, precision) + x, end="")

def	print_part_x(part, precision) :
	part = __computor__.clear_equation(part, precision)
	if part :
		begin = True
		for var in part :
			a = var[0]
			if a == int(a) :
				a = int(a)
			if var[1] :
				x = "\033[31;1m" + var[1][0] + "\033[0m"
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
					print_var(a, x, begin, precision)
				else :
					print_var(a, x + "^" + __utils__.ft_round(n, precision), begin, precision)
				begin = False
	else :
		print("0", end="")

def	print_part_n_naturals(part, precision) :
	part = __computor__.clear_equation(part, precision)
	if part :
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
					print_var(a, x, begin, precision)
				elif n == int(n) and n >= 0 :
					print_var(a, x + "^" + __utils__.ft_round(n, precision), begin, precision)
				else :
					print_var(a, x + "^\033[31;1m" + __utils__.ft_round(n, precision) + "\033[0m", begin, precision)
				begin = False
	else :
		print("0", end="")

def	print_part_n_second(part, precision) :
	part = __computor__.clear_equation(part, precision)
	if part :
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
					print_var(a, x, begin, precision)
				elif n <= 2 :
					print_var(a, x + "^" + __utils__.ft_round(n, precision), begin, precision)
				else :
					print_var(a, x + "^\033[31;1m" + __utils__.ft_round(n, precision) + "\033[0m", begin, precision)
				begin = False
	else :
		print("0", end="")

def	error_var(equation, precision, solution) :
	__pre_reduce__.print_reduce(equation, precision, solution)
	print("\033[31mError\033[0m (Multiple variables) : 			", end="")
	print_part_x(equation, precision)
	print(" = 0")
	exit(1)

def	error_n_naturals(equation, precision, solution) :
	__pre_reduce__.print_reduce(equation, precision, solution)
	print("\033[31mError\033[0m (Powers are not natural numbers) : 	", end="")
	print_part_n_naturals(equation, precision)
	print(" = 0")
	exit(1)

def	error_n_second(equation, precision, solution) :
	__pre_reduce__.print_reduce(equation, precision, solution)
	print("\033[31mError\033[0m (Powers are not strictly less than 3) : 	", end="")
	print_part_n_second(equation, precision)
	print(" = 0")
	exit(1)

def	error_parsing(equation, precision, solution) :
	__pre_reduce__.print_reduce(equation, precision, solution)
	print("\033[31mError\033[0m : 					\033[31;1m", end="")
	print_part_n_second(equation, precision)
	print(" = 0\033[0m")
	exit(1)
