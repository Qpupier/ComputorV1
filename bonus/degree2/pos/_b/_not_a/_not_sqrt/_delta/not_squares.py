# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_squares.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 16:40:01 by qpupier           #+#    #+#              #
#    Updated: 2021/08/17 17:16:54 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_notb_nota_notsqrt_delta_notsquares(var, b, delta, sqrt_delta, p) :
	str_delta = __utils__.ft_round(delta, 0)
	if b == int(b) :
		str_b = __utils__.ft_round(b, 0)
		return str_b + " - √" + str_delta, str_b + " + √" + str_delta
	mult = __bonus__.irreducible_mult(b, 1, p)
	num = int(__utils__.ft_round(b * mult, 0))
	den = int(__utils__.ft_round(mult, 0))
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - √" + str_delta)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + " / " + str_den + " + √" + str_delta)
	primes1 = __bonus__.primes(num)
	primes2 = __bonus__.primes(den)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	num = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(num) > 1 or len(den) > 1 :
		print()
		print("<=>	" + var + "_1 = " + num + " / " + den + " - √" + str_delta)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + " / " + den + " + √" + str_delta)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - √" + str_delta)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den + " + √" + str_delta)
		if len(primes1) > 1 or len(primes2) > 1 :
			num, den = __bonus__.irreducible(primes1, primes2)
			str_num = __utils__.ft_round(num, 0)
			str_den = __utils__.ft_round(den, 0)
			print()
			print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - √" + str_delta)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + " / " + str_den + " + √" + str_delta)
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
	str_num = __utils__.ft_round(num, 0)
	str_den = " / " + __utils__.ft_round(den, 0)
	if str_den == " / 1" :
		str_den = ""
	arround1 = __utils__.ft_round(num / den - sqrt_delta, 14)
	arround2 = __utils__.ft_round(num / den + sqrt_delta, 14)
	str1 = str_num + str_den + " - √" + str_delta
	str2 = str_num + str_den + " + √" + str_delta
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 14 or len(arround2[arround2.find('.') + 1:]) < 14 :
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
