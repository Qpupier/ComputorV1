# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree2_null.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 14:12:37 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 18:12:36 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_null(var, a, b, p) :
	print()
	print("Discriminant is null, there is 1 real solution :")
	print()
	print("\033[32m")
	print("Steps :")
	print()
	print("	" + var + " = -b / 2a")
	if b < 0 :
		print()
		print("<=>	" + var + " = -(" + __utils__.ft_round(b, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	elif not b :
		print()
		print("<=>	" + var + " = -" + __utils__.ft_round(b, p) + " / (2 * " + __utils__.ft_round(a, p) + ")")
	b *= -1
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + " = " + str_b + " / (2 * " + __utils__.ft_round(a, p) + ")")
	if str_b == "-0" :
		str_b = "0"
		print()
		print("<=>	" + var + " = " + str_b + " / (2 * " + __utils__.ft_round(a, p) + ")")
	a *= 2
	print()
	print("<=>	" + var + " = " + str_b + " / " + __utils__.ft_round(a, p))
	tmp = b / a
	if tmp == int(tmp) :
		result = __utils__.ft_round(b / a, 0)
		print()
		print("<=>	" + var + " = " + result)
	else :
		if a < 0 :
			b *= -1
			a *= -1
			str_b = __utils__.ft_round(b, p)
			str_a = __utils__.ft_round(a, p)
			print()
			print("<=>	" + var + " = " + str_b + " / " + str_a)
			if a == 1 :
				print()
				print("<=>	" + var + " = " + str_b)
		mult = __bonus__.irreducible_mult(b, a, p)
		b_num = int(b * mult)
		b_den = int(a * mult)
		str_den = " / " + __utils__.ft_round(b_den, 0)
		if str_den == " / 1" :
			str_den = ""
		result = __utils__.ft_round(b_num, 0) + str_den
		if mult > 1 :
			print()
			print("<=>	" + var + " = " + result)
		primes1 = __bonus__.primes(b_num)
		primes2 = __bonus__.primes(b_den)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		num = __bonus__.print_frac(primes1, delete, True)
		den = __bonus__.print_frac(primes2, delete, False)
		if len(num) > 1 or len(den) > 1 :
			print()
			print("<=>	" + var + " = " + num + " / " + den)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_num = __bonus__.print_frac(primes1, None, True)
			str_den = " / " + __bonus__.print_frac(primes2, None, False)
			if str_den == " / 1" :
				str_den = ""
			result = str_num + str_den
			print()
			print("<=>	" + var + " = " + result)
			if len(primes1) > 1 or len(primes2) > 1 :
				num, den = __bonus__.irreducible(primes1, primes2)
				str_den = " / " + __utils__.ft_round(den, 0)
				if str_den == " / 1" :
					str_den = ""
				result = __utils__.ft_round(num, 0) + str_den
				print()
				print("<=>	" + var + " = " + result)
		arround = __utils__.ft_round(b / a, 14)
		print("\033[35m")
		if len(arround[arround.find('.') + 1:]) < 14 :
			print("<=>	" + var + " = " + arround)
			result = arround
		else :
			print("<=>	" + var + " ≈ " + arround)
	print("\033[0m")
	return result, ""
