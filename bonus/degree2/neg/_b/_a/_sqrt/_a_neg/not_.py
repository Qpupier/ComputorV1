# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 12:07:46 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 12:07:58 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	delta_neg_b_a_sqrt_aneg_not(var, b, delta_sqrt, p) :
	str_b = __utils__.ft_round(b, p)
	str_delta_sqrt = __utils__.ft_round(delta_sqrt, p)
	if str_delta_sqrt == "1" :
		str_delta_sqrt = ""
	print()
	print("<=>	" + var + "_1 = " + str_b + " + " + str_delta_sqrt + "i")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - " + str_delta_sqrt + "i")
	str_i = str_delta_sqrt + "i"
	if b == int(b) :
		str1 = str_b + " + " + str_i
		str2 = str_b + " - " + str_i
		return str2, str1
	else :
		mult = __bonus__.irreducible_mult(b, 1, p)
		a1 = 1
		str_a1 = __utils__.ft_round(a1, 0)
		if mult > 1 :
			b = int(b * mult)
			a1 = int(a1 * mult)
			str_b = __utils__.ft_round(b, p)
			str_a1 = __utils__.ft_round(a1, p)
			print()
			print("<=>	" + var + "_1 = " + str_b + " / " + str_a1 + " + " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " / " + str_a1 + " - " + str_i)
		primes1 = __bonus__.primes(b)
		primes2 = __bonus__.primes(a1)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		if delete and delete != [1] :
			str_num = __bonus__.print_frac(primes1, delete, True)
			str_den = __bonus__.print_frac(primes2, delete, False)
			print()
			print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " + " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + " / " + str_den + " - " + str_i)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_num = __bonus__.print_frac(primes1, None, True)
			str_den = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " + " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + " / " + str_den + " - " + str_i)
			b, a1 = __bonus__.irreducible(primes1, primes2)
			str_b = __utils__.ft_round(b, 0)
			str_a1 = __utils__.ft_round(a1, 0)
			if len(primes1) > 1 or len(primes2) > 1 :
				print()
				print("<=>	" + var + "_1 = " + str_b + " / " + str_a1 + " + " + str_i)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_b + " / " + str_a1 + " - " + str_i)
	arround_b = __utils__.ft_round(b / a1, p)
	str1 = str_b + " + " + str_i
	str2 = str_b + " - " + str_i
	print("\033[35m")
	if len(arround_b[arround_b.find('.') + 1:]) < 14 :
		print("<=>	" + var + "_1 = " + arround_b + " + " + str_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + arround_b + " - " + str_i)
		str1 = arround_b + " + " + str_i
		str2 = arround_b + " - " + str_i
	else :
		print("<=>	" + var + "_1 ≈ " + arround_b + " + " + str_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + arround_b + " - " + str_i)
	return str2, str1
