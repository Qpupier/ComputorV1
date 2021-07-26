# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    b_not_int.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 12:10:03 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 12:10:19 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	delta_neg_b_a_sqrt_apos_notbint_iint(var, str_b, arround_b, delta_sqrt, a) :
	i = delta_sqrt / a
	str_i = __utils__.ft_round(i ,0) + "i"
	if str_i == "1i" :
		print()
		print("<=>	" + var + "_1 = " + str_b + " - " + str_i)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + " + str_i)
		str_i = "i"
	print()
	print("<=>	" + var + "_1 = " + str_b + " - " + str_i)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + " + str_i)
	str1 = str_b + " - " + str_i
	str2 = str_b + " + " + str_i
	print("\033[35m")
	if len(arround_b[arround_b.find('.') + 1:]) < 14 :
		print("<=>	" + var + "_1 = " + arround_b + " - " + str_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + arround_b + " + " + str_i)
		str1 = arround_b + " - " + str_i
		str2 = arround_b + " + " + str_i
	else :
		print("<=>	" + var + "_1 ≈ " + arround_b + " - " + str_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + arround_b + " + " + str_i)
	return str1, str2

def	delta_neg_b_a_sqrt_apos_notbint_inotint(var, str_b, arround_b, i, a, p) :
	mult = __bonus__.irreducible_mult(int(i), int(a), p)
	str_i = __utils__.ft_round(i, 0)
	str_a = __utils__.ft_round(a, 0)
	if mult > 1 :
		i = int(i * mult)
		a = int(a * mult)
		str_i = __utils__.ft_round(i, p)
		str_a = __utils__.ft_round(a, p)
		print()
		print("<=>	" + var + "_1 = " + str_b + " - " + str_i + "i / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + " + str_i + "i / " + str_a)
	primes1 = __bonus__.primes(i)
	primes2 = __bonus__.primes(a)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	if delete :
		str_num = __bonus__.print_frac(primes1, delete, True)
		str_den = __bonus__.print_frac(primes2, delete, False)
		print()
		print("<=>	" + var + "_1 = " + str_b + " - " + str_num + "i / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + " + str_num + "i / " + str_den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_b + " - " + str_num + "i / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + " + str_num + "i / " + str_den)
		i, a = __bonus__.irreducible(primes1, primes2)
		str_i = __utils__.ft_round(i, 0)
		str_a = __utils__.ft_round(a, 0)
		if len(primes1) > 1 or len(primes2) > 1 :
			print()
			print("<=>	" + var + "_1 = " + str_b + " - " + str_i + "i / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " + " + str_i + "i / " + str_a)
	if str_i == "1" :
		print()
		print("<=>	" + var + "_1 = " + str_b + " - " + str_i)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + " + str_i)
		str_i = ""
	str_i += "i / " + str_a
	arround_i = __utils__.ft_round(i / a, p) + "i"
	equal_b = len(arround_b[arround_b.find('.') + 1:]) < 14
	equal_i = len(arround_i[arround_i.find('.') + 1:]) < 15
	print("\033[35m")
	if equal_b and equal_i :
		str1 = arround_b + " - " + arround_i
		str2 = arround_b + " + " + arround_i
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + str2)
	else :
		if equal_b :
			str1 = arround_b + " - " + str_i
			str2 = arround_b + " + " + str_i
		elif equal_i :
			str1 = str_b + " - " + arround_i
			str2 = str_b + " + " + arround_i
		else :
			str1 = str_b + " - " + str_i
			str2 = str_b + " + " + str_i
		print("<=>	" + var + "_1 ≈ " + str1)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + str2)
	return str1, str2

def	delta_neg_b_a_sqrt_apos_notbint(var, a, b, delta_sqrt, p) :
	mult = __bonus__.irreducible_mult(int(b), int(a), p)
	a1 = a
	str_b = __utils__.ft_round(b, 0)
	str_a1 = __utils__.ft_round(a1, 0)
	str_i = __utils__.ft_round(delta_sqrt, 0) + "i / " + __utils__.ft_round(a, 0)
	if mult > 1 :
		b = int(b * mult)
		a1 = int(a1 * mult)
		str_b = __utils__.ft_round(b, p)
		str_a1 = __utils__.ft_round(a1, p)
		print()
		print("<=>	" + var + "_1 = " + str_b + " / " + str_a1 + " - " + str_i)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " / " + str_a1 + " + " + str_i)
	primes1 = __bonus__.primes(b)
	primes2 = __bonus__.primes(a1)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	if delete :
		str_num = __bonus__.print_frac(primes1, delete, True)
		str_den = __bonus__.print_frac(primes2, delete, False)
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - " + str_i)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den + " + " + str_i)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - " + str_i)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den + " + " + str_i)
		b, a1 = __bonus__.irreducible(primes1, primes2)
		str_b = __utils__.ft_round(b, 0)
		str_a1 = __utils__.ft_round(a1, 0)
		if len(primes1) > 1 or len(primes2) > 1 :
			print()
			print("<=>	" + var + "_1 = " + str_b + " / " + str_a1 + " - " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " / " + str_a1 + " + " + str_i)
	str_b += " / " + str_a1
	tmp_i = delta_sqrt / a
	if tmp_i == int(tmp_i) :
		return delta_neg_b_a_sqrt_apos_notbint_iint(var, str_b, __utils__.ft_round(b / a1, 15), delta_sqrt, a)
	return delta_neg_b_a_sqrt_apos_notbint_inotint(var, str_b, __utils__.ft_round(b / a1, 15), delta_sqrt, a, p)
