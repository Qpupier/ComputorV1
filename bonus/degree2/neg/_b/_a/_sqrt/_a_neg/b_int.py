# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    b_int.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 12:05:42 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 13:45:45 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	delta_neg_b_a_sqrt_aneg_bint_sqrtint(var, b, delta_sqrt, p) :
	str_b = __utils__.ft_round(b, p)
	str_sqrt_delta = __utils__.ft_round(delta_sqrt, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + " + str_sqrt_delta + "i")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - " + str_sqrt_delta + "i")
	return str_b + " - " + str_sqrt_delta + "i", str_b + " + " + str_sqrt_delta + "i"

def	delta_neg_b_a_sqrt_aneg_bint_notsqrtint(var, a, b, delta_sqrt, p) :
	str_b = __utils__.ft_round(b, p)
	mult = __bonus__.irreducible_mult(int(delta_sqrt), int(a), p)
	if mult > 1 :
		delta_sqrt = int(delta_sqrt * mult)
		a = int(a * mult)
		print()
		print("<=>	" + var + "_1 = " + str_b + " + " + __utils__.ft_round(delta_sqrt, 0) + "i / " + __utils__.ft_round(a, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - " + __utils__.ft_round(delta_sqrt, 0) + "i / " + __utils__.ft_round(a, 0))
	primes1 = __bonus__.primes(delta_sqrt)
	primes2 = __bonus__.primes(a)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	if delete :
		str_num = __bonus__.print_frac(primes1, delete, True)
		str_den = __bonus__.print_frac(primes2, delete, False)
		print()
		print("<=>	" + var + "_1 = " + str_b + " + " + str_num + "i / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - " + str_num + "i / " + str_den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_b + " + " + str_num + "i / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - " + str_num + "i / " + str_den)
		delta_sqrt, a = __bonus__.irreducible(primes1, primes2)
		if len(primes1) > 1 or len(primes2) > 1 :
			str_delta = __utils__.ft_round(delta_sqrt, 0)
			if str_delta == "1" :
				str_delta = ""
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + str_delta + "i / " + __utils__.ft_round(a, 0))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_delta + "i / " + __utils__.ft_round(a, 0))
	str1 = str_b + " + " + __utils__.ft_round(delta_sqrt, 0) + "i / " + __utils__.ft_round(a, 0)
	str2 = str_b + " - " + __utils__.ft_round(delta_sqrt, 0) + "i / " + __utils__.ft_round(a, 0)
	arround_d = __utils__.ft_round(delta_sqrt / a, 15) + "i"
	print("\033[35m")
	if len(arround_d[arround_d.find('.') + 1:]) < 15 :
		print("<=>	" + var + "_1 = " + str_b + " + " + arround_d)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + str_b + " - " + arround_d)
		str1 = str_b + " + " + arround_d
		str2 = str_b + " - " + arround_d
	else :
		print("<=>	" + var + "_1 ≈ " + str_b + " + " + arround_d)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + str_b + " - " + arround_d)
	return str2, str1

def	delta_neg_b_a_sqrt_aneg_bint(var, a, b, delta_sqrt, p) :
	str_b = __utils__.ft_round(b, p)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + " + __utils__.ft_round(delta_sqrt, p) + "i / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - " + __utils__.ft_round(delta_sqrt, p) + "i / " + str_a)
	tmp_delta_sqrt = delta_sqrt / a
	if tmp_delta_sqrt == int(tmp_delta_sqrt) :
		delta_sqrt = tmp_delta_sqrt
		return delta_neg_b_a_sqrt_aneg_bint_sqrtint(var, b, delta_sqrt, p)
	return delta_neg_b_a_sqrt_aneg_bint_notsqrtint(var, a, b, delta_sqrt, p)
