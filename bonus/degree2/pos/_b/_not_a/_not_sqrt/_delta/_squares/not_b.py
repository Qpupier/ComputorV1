# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_b.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 17:37:42 by qpupier           #+#    #+#              #
#    Updated: 2021/08/18 14:26:23 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_b_nota_notsqrt_delta_squares_notb(var, b, k, delta_den, str_squares, p) :
	mult = __bonus__.irreducible_mult(b, 1, p)
	num = int(__utils__.ft_round(b * mult, 0))
	den = int(__utils__.ft_round(mult, 0))
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - " + str_squares)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + " / " + str_den + " + " + str_squares)
	primes1 = __bonus__.primes(num)
	primes2 = __bonus__.primes(den)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	num = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(num) > 1 or len(den) > 1 :
		print()
		print("<=>	" + var + "_1 = " + num + " / " + den + " - " + str_squares)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + " / " + den + " + " + str_squares)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - " + str_squares)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den + " + " + str_squares)
		if len(primes1) > 1 or len(primes2) > 1 :
			num, den = __bonus__.irreducible(primes1, primes2)
			str_num = __utils__.ft_round(num, 0)
			str_den = __utils__.ft_round(den, 0)
			print()
			print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - " + str_squares)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + " / " + str_den + " + " + str_squares)
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
	primes1 = __bonus__.primes(num)
	primes2 = __bonus__.primes(k)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	str_num = __bonus__.print_fact(primes1, delete, False)
	str_k = __bonus__.print_fact(primes2, delete, False)
	str_delta = "√" + __utils__.ft_round(delta_den, 0)
	if delete :
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - " + str_k + str_delta)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den + " + " + str_k + str_delta)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		fact, fact = __bonus__.irreducible(None, delete)
		str_fact = "\033[37m" + __utils__.ft_round(fact, 0) + "\033[32m"
		num, k = __bonus__.irreducible(primes1, primes2)
		if len(delete) > 1 or len(primes1) > 1 or len(primes2) > 1 :
			str_num = " * " + __utils__.ft_round(num, 0)
			str_k = " * " + __utils__.ft_round(k, 0)
			if str_k == " * 1" :
				str_k = ""
			str1 = str_fact + str_num + " / " + str_den + " - " + str_fact + str_k + str_delta
			str2 = str_fact + str_num + " / " + str_den + " + " + str_fact + str_k + str_delta
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
		str_num = __utils__.ft_round(num, 0)
		str_k = __utils__.ft_round(k, 0)
		if str_k == "1" :
			str_k = ""
		str1 = str_fact + "(" + str_num + " / " + str_den + " - " + str_k + str_delta + ")"
		str2 = str_fact + "(" + str_num + " / " + str_den + " + " + str_k + str_delta + ")"
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
	else :
		fact = 1
		str_num = __utils__.ft_round(num, 0)
		str_k = __utils__.ft_round(k, 0)
		if str_k == "1" :
			str_k = ""
		str1 = str_num + " / " + str_den + " - " + str_k + str_delta
		str2 = str_num + " / " + str_den + " + " + str_k + str_delta
	str1 = str1.replace("\033[37m", "").replace("\033[32m", "")
	str2 = str2.replace("\033[37m", "").replace("\033[32m", "")
	arround1 = __utils__.ft_round(fact * (num / den - k * __utils__.ft_sqrt(delta_den)), 14)
	arround2 = __utils__.ft_round(fact * (num / den + k * __utils__.ft_sqrt(delta_den)), 14)
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
