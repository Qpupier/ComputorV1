# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bonus.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 19:39:06 by qpupier           #+#    #+#              #
#    Updated: 2021/06/10 17:43:57 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import verbose as __verbose__
import utils as __utils__

def	first_prime(nb, j) :
	for i in range(j, int(nb / 2) + 1) :
		if nb / i == int(nb / i) :
			return i
	return -1

def	primes(nb) :
	result = []
	if nb < 0 :
		result.append(-1)
		nb *= -1
	new = 2
	while nb >= 0 :
		new = first_prime(nb, new)
		if new == -1 :
			result.append(int(nb))
			return result
		result.append(new)
		nb /= new
	return result

def	reduce_fraction(first, second) :
	for a in range(len(first)) :
		for b in range(len(second)) :
			if first[a] == second[b] :
				first.pop(a)
				second.pop(b)
				return reduce_fraction(first, second)
	return first, second

def	irreducible_mult(num, div, p) :
	verif = False
	while not verif and p > 0 :
		try :
			if num != int(num) or div != int(div) :
				num *= 10
				div *= 10
			else :
				verif = True
		except :
			num *= 10
			div *= 10
		p -= 1
	num = int(__utils__.ft_round(num, 0))
	div = int(__utils__.ft_round(div, 0))
	return num, div
	print(num, div)
	first = primes(num)
	second = primes(div)
	print(first, second)
	first, second = reduce_fraction(first, second)
	print(first, second)

def	print_fraction(num, div) :
	for i in range(len(num)) :
		if i :
			print(" * ", end="")
		print(num[i], end="")
	print(" / ", end="")
	if len(div) > 1 :
		print("(", end= "")
	for i in range(len(div)) :
		if i :
			print(" * ", end="")
		print(div[i], end="")
	if len(div) > 1 :
		print(")", end= "")

def	irreducible(num, div) :
	a = 1
	for i in num :
		a *= i
	b = 1
	for i in div :
		b *= i
	return a, b

def	degree_1_bonus(equation, var, p) :
	print("Polynomial degree : 1")
	print("\033[32m")
	print("Steps :")
	part2 = []
	part2.append(equation[2])
	equation.pop(2)
	part2[0][0] *= -1
	__verbose__.print_step(equation, part2, True, p)
	if equation[1][0] != 1 :
		print("<=>	" + var + " = " + __utils__.ft_round(part2[0][0], p) + " / " + __utils__.ft_round(equation[1][0], p))
		div = __utils__.ft_round(part2[0][0] / equation[1][0], 15)
		if div == int(float(div)) :
			print("<=>	" + var + " = " + int(div))
		else :
			num, div = irreducible_mult(part2[0][0], equation[1][0], p)
			print("<=>	" + var + " = " + str(num) + " / " + str(div))
			num = primes(num)
			div = primes(div)
			print("<=>	" + var + " = ", end="")
			print_fraction(num, div)
			print()
			num, div = reduce_fraction(num, div)
			print("<=>	" + var + " = ", end="")
			print_fraction(num, div)
			print()
			num, div = irreducible(num, div)
			print("<=>	" + var + " = " + str(num) + " / " + str(div))
	# 	print(var + " = " + s)
	# 	print()
	# print("\033[33;1mS = {", end="")
	# print(s, end="")
	# print("}\033[0m")
