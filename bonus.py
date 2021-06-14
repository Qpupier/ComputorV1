# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bonus.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 19:39:06 by qpupier           #+#    #+#              #
#    Updated: 2021/06/11 18:12:19 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from typing import MutableMapping
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
	return [1] if not result else result

def	reduce_fraction(first, second, result) :
	tmp_a = []
	tmp_b = []
	for a in range(len(first)) :
		for b in range(len(second)) :
			if not a in tmp_a and not b in tmp_b and first[a] == second[b] :
				tmp_a.append(a)
				tmp_b.append(b)
				result.append(first[a])

def	irreducible_mult(num, div) :
	l_n = str(num).find('.')
	l_d = str(div).find('.')
	l_n = 0 if l_n == -1 else len(str(num)[(l_n + 1):])
	l_d = 0 if l_d == -1 else len(str(div)[(l_d + 1):])
	mult = __utils__.ft_pow(10, l_n if l_n >= l_d else l_d)
	return mult

def	print_fraction(num, div, delete) :
	copy = None if not delete else delete.copy()
	copy2 = None if not delete else delete.copy()
	for i in range(len(num)) :
		if i :
			print(" * ", end="")
		if copy and num[i] in copy :
			print("\033[34m", end="")
		print(num[i], end="")
		if copy and num[i] in copy :
			print("\033[32m", end="")
			copy.pop(copy.index(num[i]))
	print(" / ", end="")
	if len(div) > 1 :
		print("(", end= "")
	for i in range(len(div)) :
		if i :
			print(" * ", end="")
		if copy2 and div[i] in copy2 :
			print("\033[34m", end="")
		print(div[i], end="")
		if copy2 and div[i] in copy2 :
			print("\033[32m", end="")
			copy2.pop(copy2.index(div[i]))
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

def	fraction_delete(frac, copy) :
	for a in range(len(frac)) :
		for tmp in range(len(copy)) :
			if frac[a] == copy[tmp] :
				frac.pop(a)
				copy.pop(tmp)
				return fraction_delete(frac, copy)

def	degree_1_bonus(equation, var, p) :
	print("Polynomial degree : 1")
	print("\033[32m")
	print("Steps :")
	part2 = []
	part2.append(equation[2])
	equation.pop(2)
	part2[0][0] *= -1
	__verbose__.print_step(equation, part2, True, p)
	result = __utils__.ft_round(part2[0][0], p)
	if equation[1][0] != 1 and equation[1][0] != -1 :
		print("<=>	" + var + " = " + __utils__.ft_round(part2[0][0], p) + " / " + __utils__.ft_round(equation[1][0], p))
		div = __utils__.ft_round(part2[0][0] / equation[1][0], 15)
		if div == int(float(div)) :
			result = str(int(div))
			result = str(int(div))
			print("<=>	" + var + " = " + result)
		else :
			num = part2[0][0]
			div = equation[1][0]
			if num == int(num) :
				num = int(num)
			if div == int(div) :
				div = int(div)
			mult = irreducible_mult(num, div)
			if mult > 1 :
				print("<=>	" + var + " = " + str(num) + " * " + str(mult) + " / (" + str(div) + " * " + str(mult) + ")")
				num = int(__utils__.ft_round(int(num * mult), 0))
				div = int(__utils__.ft_round(int(div * mult), 0))
				print("<=>	" + var + " = " + str(num) + " / " + str(div))
			primes_num = primes(num)
			primes_div = primes(div)
			delete = []
			reduce_fraction(primes_num, primes_div, delete)
			if delete :
				print("<=>	" + var + " = ", end="")
				print_fraction(primes_num, primes_div, delete)
				print()
				fraction_delete(primes_num, delete.copy())
				fraction_delete(primes_div, delete.copy())
				print("<=>	" + var + " = ", end="")
				print_fraction(primes_num, primes_div, None)
				print()
				if len(primes_num) > 1 or len(primes_div) > 1 :
					num, div = irreducible(primes_num, primes_div)
					print("<=>	" + var + " = " + str(num) + " / " + str(div))
				else :
					num = 1 if not primes_num else primes_num[0]
					div = 1 if not primes_div else primes_div[0]
			if div < 0 :
				num *= -1
				div *= -1
				print("<=>	" + var + " = " + str(num) + " / " + str(div))
			round = __utils__.ft_round(num / div, 15)
			equal = " ≈ "
			result = str(num) + " / " + str(div)
			if len(round[round.find('.') + 1:]) < 15 :
				equal = " = "
				result = round
			print("\033[35m<=>	" + var + equal + __utils__.ft_round(num / div, 15) + "\033[0m")
	elif equation[1][0] == -1 :
		part2[0][0] *= -1
		result = __utils__.ft_round(part2[0][0], p)
		print("<=>	" + var + " = " + result)
	print("\033[33;1m")
	print("S = {" + result + "}\033[0m")
