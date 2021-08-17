# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sqrt.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 15:14:43 by qpupier           #+#    #+#              #
#    Updated: 2021/08/17 16:19:36 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_b_nota_sqrt(var, b, sqrt_delta, p) :
	str_b = __utils__.ft_round(b, p)
	str_sqrt_delta = __utils__.ft_round(sqrt_delta, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - " + str_sqrt_delta)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + " + str_sqrt_delta)
	b1 = b - sqrt_delta
	b2 = b + sqrt_delta
	str_b1 = __utils__.ft_round(b1, p)
	str_b2 = __utils__.ft_round(b2, p)
	print()
	print("<=>	" + var + "_1 = " + str_b1)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b2)
	if b == int(b) :
		return str_b1, str_b2
	mult = __bonus__.irreducible_mult(b1, 1, p)
	b1_num = int(__utils__.ft_round(b1 * mult, 0))
	b1_den = int(__utils__.ft_round(mult, 0))
	b2_num = int(__utils__.ft_round(b2 * mult, 0))
	b2_den = int(__utils__.ft_round(mult, 0))
	str_b1_num = __utils__.ft_round(b1_num, 0)
	str_b1_den = __utils__.ft_round(b1_den, 0)
	str_b2_num = __utils__.ft_round(b2_num, 0)
	str_b2_den = __utils__.ft_round(b2_den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_b1_num + " / " + str_b1_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b2_num + " / " + str_b2_den)
	primes1 = __bonus__.primes(b1_num)
	primes2 = __bonus__.primes(b1_den)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	num = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(num) > 1 or len(den) > 1 :
		print()
		print("<=>	" + var + "_1 = " + num + " / " + den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b2_num + " / " + str_b2_den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b2_num + " / " + str_b2_den)
		if len(primes1) > 1 or len(primes2) > 1 :
			num, den = __bonus__.irreducible(primes1, primes2)
			str_num = __utils__.ft_round(num, 0)
			str_den = __utils__.ft_round(den, 0)
			print()
			print("<=>	" + var + "_1 = " + str_num + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b2_num + " / " + str_b2_den)
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
		b1_num = num
		b1_den = den
	str_b1_num = __utils__.ft_round(b1_num, 0)
	str_b1_den = __utils__.ft_round(b1_den, 0)
	str1 = str_b1_num + " / " + str_b1_den
	primes1 = __bonus__.primes(b2_num)
	primes2 = __bonus__.primes(b2_den)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	num = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(num) > 1 or len(den) > 1 :
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + " / " + den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den)
		if len(primes1) > 1 or len(primes2) > 1 :
			num, den = __bonus__.irreducible(primes1, primes2)
			str_num = __utils__.ft_round(num, 0)
			str_den = __utils__.ft_round(den, 0)
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + " / " + str_den)
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
		b2_num = num
		b2_den = den
	str_b2_num = __utils__.ft_round(b2_num, 0)
	str_b2_den = __utils__.ft_round(b2_den, 0)
	str2 = str_b2_num + " / " + str_b2_den
	arround1 = __utils__.ft_round(b1_num / b1_den, 14)
	arround2 = __utils__.ft_round(b2_num / b2_den, 14)
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 14 :
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
