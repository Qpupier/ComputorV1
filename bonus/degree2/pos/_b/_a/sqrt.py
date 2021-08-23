# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sqrt.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/21 18:12:21 by qpupier           #+#    #+#              #
#    Updated: 2021/08/23 19:49:57 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_b_a_sqrt(var, b, sqrt_delta, a, p) :
	str_b = __utils__.ft_round(b, p)
	str_delta = __utils__.ft_round(sqrt_delta, 0)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - " + str_delta + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + " + str_delta + ") / " + str_a)
	b1 = b - sqrt_delta
	b2 = b + sqrt_delta
	str_b1 = __utils__.ft_round(b1, p)
	str_b2 = __utils__.ft_round(b2, p)
	print()
	print("<=>	" + var + "_1 = " + str_b1 + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b2 + " / " + str_a)
	mult1 = __bonus__.irreducible_mult(b1, a, p)
	num1 = int(__utils__.ft_round(b1 * mult1, 0))
	den1 = int(__utils__.ft_round(a * mult1, 0))
	str_num1 = __utils__.ft_round(num1, 0)
	str_den1 = __utils__.ft_round(den1, 0)
	mult2 = __bonus__.irreducible_mult(b2, a, p)
	num2 = int(__utils__.ft_round(b2 * mult2, 0))
	den2 = int(__utils__.ft_round(a * mult2, 0))
	str_num2 = __utils__.ft_round(num2, 0)
	str_den2 = __utils__.ft_round(den2, 0)
	if mult1 > 1 or mult2 > 1 :
		print()
		print("<=>	" + var + "_1 = " + str_num1 + " / " + str_den1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num2 + " / " + str_den2)
	primes1_1 = __bonus__.primes(num1)
	primes2_1 = __bonus__.primes(den1)
	delete1 = []
	__bonus__.reduce_fraction(primes1_1, primes2_1, delete1)
	num1 = __bonus__.print_frac(primes1_1, delete1, True)
	den1 = __bonus__.print_frac(primes2_1, delete1, False)
	primes1_2 = __bonus__.primes(num2)
	primes2_2 = __bonus__.primes(den2)
	delete2 = []
	__bonus__.reduce_fraction(primes1_2, primes2_2, delete2)
	num2 = __bonus__.print_frac(primes1_2, delete2, True)
	den2 = __bonus__.print_frac(primes2_2, delete2, False)
	a1 = a
	a2 = a
	if len(num1) > 1 or len(den1) > 1 or len(num2) > 1 or len(den2) > 1 :
		print()
		print("<=>	" + var + "_1 = " + num1 + " / " + den1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num2 + " / " + den2)
		__bonus__.fraction_delete(primes1_1, delete1.copy())
		__bonus__.fraction_delete(primes2_1, delete1.copy())
		str_num1 = __bonus__.print_frac(primes1_1, None, True)
		str_den1 = __bonus__.print_frac(primes2_1, None, False)
		__bonus__.fraction_delete(primes1_2, delete2.copy())
		__bonus__.fraction_delete(primes2_2, delete2.copy())
		str_num2 = __bonus__.print_frac(primes1_2, None, True)
		str_den2 = __bonus__.print_frac(primes2_2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_num1 + " / " + str_den1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num2 + " / " + str_den2)
		if len(primes1_1) > 1 or len(primes2_1) > 1 or len(primes1_2) > 1 or len(primes2_2) > 1 :
			num1, den1 = __bonus__.irreducible(primes1_1, primes2_1)
			str_num1 = __utils__.ft_round(num1, 0)
			str_den1 = __utils__.ft_round(den1, 0)
			num2, den2 = __bonus__.irreducible(primes1_2, primes2_2)
			str_num2 = __utils__.ft_round(num2, 0)
			str_den2 = __utils__.ft_round(den2, 0)
			print()
			print("<=>	" + var + "_1 = " + str_num1 + " / " + str_den1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num2 + " / " + str_den2)
		else :
			num1 = 1 if not primes1_1 else primes1_1[0]
			den1 = 1 if not primes2_1 else primes2_1[0]
			num2 = 1 if not primes1_2 else primes1_2[0]
			den2 = 1 if not primes2_2 else primes2_2[0]
		b1 = num1
		b2 = num2
		a1 = den1
		a2 = den2
	str_b1 = __utils__.ft_round(b1, 0)
	str_b2 = __utils__.ft_round(b2, 0)
	str_a1 = __utils__.ft_round(a1, 0)
	str_a2 = __utils__.ft_round(a2, 0)
	str1 = str_b1 + " / " + str_a1
	str2 = str_b2 + " / " + str_a2
	arround1 = __utils__.ft_round(b1 / a1, 14)
	arround2 = __utils__.ft_round(b2 / a2, 14)
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 13 :
		print("<=>	" + var + "_1 = " + arround1)
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 = " + arround2)
		str1 = arround1
		str2 = arround2
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 ≈ " + arround2)
	return str1, str2
	print("TODO NOW")
	return "", ""
