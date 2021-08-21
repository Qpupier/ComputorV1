# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_squares.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/21 18:57:22 by qpupier           #+#    #+#              #
#    Updated: 2021/08/21 20:35:10 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_b_a_notsqrt_notdelta_delta_den_notsquares(var, b, delta, delta_den, a, p) :
	str_delta_num = __utils__.ft_round(delta, 0)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	str_a = __utils__.ft_round(a, p)
	k = 1
	if b == int(b) :
		num = b
		den = 1
		str_num = __utils__.ft_round(num, 0)
		print()
		print("<=>	" + var + "_1 = ((" + str_num + "\033[31m * " + str_delta_den + "\033[32m) / \033[31m" + str_delta_den + "\033[32m" + " - √" + str_delta_num + " / " + str_delta_den + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = ((" + str_num + "\033[31m * " + str_delta_den + "\033[32m) / \033[31m" + str_delta_den + "\033[32m" + " + √" + str_delta_num + " / " + str_delta_den + ") / " + str_a)
		num *= delta_den
		den *= delta_den
	else :
		mult = __bonus__.irreducible_mult(b, 1, p)
		num = int(__utils__.ft_round(b * mult, 0))
		den = int(__utils__.ft_round(mult, 0))
		str_num = __utils__.ft_round(num, 0)
		str_den = __utils__.ft_round(den, 0)
		if den != delta_den :
			print()
			print("<=>	" + var + "_1 = (" + str_num + " / " + str_den + " - √" + str_delta_num + " / " + str_delta_den + ") / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = (" + str_num + " / " + str_den + " + √" + str_delta_num + " / " + str_delta_den + ") / " + str_a)
			print()
			print("<=>	" + var + "_1 = (" + str_num + "\033[31m * " + str_delta_den + "\033[32m) / (" + str_den + "\033[31m * " + str_delta_den + "\033[32m)" + " - \033[31m" + str_den + "\033[32m√" + str_delta_num + " / (" + str_delta_den + "\033[31m * " + str_den + "\033[32m)")
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = (" + str_num + "\033[31m * " + str_delta_den + "\033[32m) / (" + str_den + "\033[31m * " + str_delta_den + "\033[32m)" + " + \033[31m" + str_den + "\033[32m√" + str_delta_num + " / (" + str_delta_den + "\033[31m * " + str_den + "\033[32m)")
			num *= delta_den
			k = den
			den *= delta_den
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	str_k = __utils__.ft_round(k, 0)
	if str_k == "1" :
		str_k = ""
	str_delta_num = __utils__.ft_round(delta, 0)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = (" + str_num + " / " + str_den + " - " + str_k + "√" + str_delta_num + " / " + str_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_num + " / " + str_den + " + " + str_k + "√" + str_delta_num + " / " + str_den + ") / " + str_a)
	print()
	print("<=>	" + var + "_1 = (" + str_num + " - " + str_k + "√" + str_delta_num + ") / " + str_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_num + " + " + str_k + "√" + str_delta_num + ") / " + str_den + " / " + str_a)
	print()
	print("<=>	" + var + "_1 = (" + str_num + " - " + str_k + "√" + str_delta_num + ") / (" + str_den + " * " + str_a + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_num + " + " + str_k + "√" + str_delta_num + ") / (" + str_den + " * " + str_a + ")")
	a *= den
	str_den = __utils__.ft_round(a, 0)
	str1 = "(" + str_num + " - " + str_k + "√" + str_delta_num + ") / " + str_den
	str2 = "(" + str_num + " + " + str_k + "√" + str_delta_num + ") / " + str_den
	print()
	print("<=>	" + var + "_1 = " + str1)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str2)
	arround1 = __utils__.ft_round((num - k * __utils__.ft_sqrt(delta)) / a, 14)
	arround2 = __utils__.ft_round((num + k * __utils__.ft_sqrt(delta)) / a, 14)
	k = 3
	if k != 1 :
		print("TODO NOW")
		return "", ""
	if '.' in __utils__.ft_round(a, p) :
		mult = __bonus__.irreducible_mult(1, a, p)
		fact = int(__utils__.ft_round(mult, 0))
		a = int(__utils__.ft_round(a * mult, 0))
		str_fact = __utils__.ft_round(fact, 0)
		if str_fact == "1" :
			str_fact = ""
		str_a = __utils__.ft_round(a, 0)
		print()
		print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_k + "√" + str_delta_num + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_k + "√" + str_delta_num + ") / " + str_a)
		primes1 = __bonus__.primes(fact)
		primes2 = __bonus__.primes(a)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		str_fact = __bonus__.print_frac(primes1, delete, True)
		if str_fact == "1" :
			str_fact = ""
		str_a = __bonus__.print_frac(primes2, delete, False)
		if len(str_fact) > 1 or len(str_a) > 1 :
			print()
			print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_k + "√" + str_delta_num + ") / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_k + "√" + str_delta_num + ") / " + str_a)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_fact = __bonus__.print_frac(primes1, None, True)
			if str_fact == "1" :
				str_fact = ""
			str_a = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_k + "√" + str_delta_num + ") / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_k + "√" + str_delta_num + ") / " + str_a)
			if len(primes1) > 1 or len(primes2) > 1 :
				fact, a = __bonus__.irreducible(primes1, primes2)
				str_fact = __utils__.ft_round(fact, 0)
				if str_fact == "1" :
					str_fact = ""
				str_a = __utils__.ft_round(a, 0)
				print()
				print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_k + "√" + str_delta_num + ") / " + str_a)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_k + "√" + str_delta_num + ") / " + str_a)
			else :
				fact = 1 if not primes1 else primes1[0]
				a = 1 if not primes2 else primes2[0]
				str_fact = __utils__.ft_round(fact, 0)
				if str_fact == "1" :
					str_fact = ""
				str_a = __utils__.ft_round(a, 0)
		str1 = str_fact + "(" + str_num + " - " + str_k + "√" + str_delta_num + ") / " + str_a
		str2 = str_fact + "(" + str_num + " + " + str_k + "√" + str_delta_num + ") / " + str_a
		arround1 = __utils__.ft_round(fact * (num - k * __utils__.ft_sqrt(delta)) / a, 14)
		arround2 = __utils__.ft_round(fact * (num + k * __utils__.ft_sqrt(delta)) / a, 14)
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
