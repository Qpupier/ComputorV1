# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 19:39:06 by qpupier           #+#    #+#              #
#    Updated: 2021/06/26 14:28:44 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

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

def	irreducible_mult(num, div, p) :
	l_n = str(num).find('.')
	l_d = str(div).find('.')
	l_n = 0 if l_n == -1 else len(str(num)[(l_n + 1):])
	l_d = 0 if l_d == -1 else len(str(div)[(l_d + 1):])
	mult = l_n if l_n >= l_d else l_d
	return __utils__.ft_pow(10, p if mult > p else mult)

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
	if num :
		for i in num :
			a *= i
	b = 1
	if div :
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

def	perfect_squares(nb, result) :
	if nb < 4 :
		return int(nb)
	first = int(__utils__.ft_sqrt(int(nb * 0.5)))
	for i in range(first, 1, -1) :
		square = i * i
		if nb / square == int(nb / square) :
			result.append(i)
			return perfect_squares(nb / square, result)
	return int(nb)

def	reduce_sqrt(delta) :
	squares = []
	delta = perfect_squares(delta, squares)
	return squares, delta

def	print_frac(prime, delete, top) :
	copy = None if not delete else delete.copy()
	result = ""
	if prime :
		if not top and len(prime) > 1 :
			result += "("
		for i in range(len(prime)) :
			if i :
				result += " * "
			if copy and prime[i] in copy :
				result += "\033[34m"
			result += str(prime[i])
			if copy and prime[i] in copy :
				result += "\033[32m"
				copy.pop(copy.index(prime[i]))
		if not top and len(prime) > 1 :
			result += ")"
	else :
		result = "1"
	return result

def	str_lst_sq(lst, delta) :
	result = ""
	if lst and delta :
		if lst :
			result += "("
		for i in range(len(lst)) :
			if i :
				result += " * "
			result += __utils__.ft_round(lst[i] * lst[i], 14)
		if lst :
			result += " * "
		result += __utils__.ft_round(delta, 14)
		if lst :
			result += ")"
	return result

def	irreducible_sq(sq) :
	nb = 1
	for each in sq :
		nb *= each * each
	return [__utils__.ft_sqrt(nb)]
