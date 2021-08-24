# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_squares.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/23 20:00:41 by qpupier           #+#    #+#              #
#    Updated: 2021/08/24 16:02:48 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_b_a_notsqrt_delta_notsquares(var, b, delta, a, p) :
	str_delta = __utils__.ft_round(delta, 0)
	str_a = __utils__.ft_round(a, p)
	num = b
	den = 1
	str_den = ""
	str_num = __utils__.ft_round(b, 0)
	if b != int(b) :
		mult = __bonus__.irreducible_mult(b, 1, p)
		num = int(__utils__.ft_round(b * mult, 0))
		den = int(__utils__.ft_round(mult, 0))
		str_num = __utils__.ft_round(num, 0)
		str_den = __utils__.ft_round(den, 0)
		print()
		print("<=>	" + var + "_1 = (" + str_num + " / " + str_den + " - √" + str_delta + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_num + " / " + str_den + " + √" + str_delta + ") / " + str_a)
		primes1 = __bonus__.primes(num)
		primes2 = __bonus__.primes(den)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		num = __bonus__.print_frac(primes1, delete, True)
		den = __bonus__.print_frac(primes2, delete, False)
		if len(num) > 1 or len(den) > 1 :
			print()
			print("<=>	" + var + "_1 = (" + num + " / " + den + " - √" + str_delta + ") / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = (" + num + " / " + den + " + √" + str_delta + ") / " + str_a)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_num = __bonus__.print_frac(primes1, None, True)
			str_den = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = (" + str_num + " / " + str_den + " - √" + str_delta + ") / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = (" + str_num + " / " + str_den + " + √" + str_delta + ") / " + str_a)
			if len(primes1) > 1 or len(primes2) > 1 :
				num, den = __bonus__.irreducible(primes1, primes2)
				str_num = __utils__.ft_round(num, 0)
				str_den = __utils__.ft_round(den, 0)
				print()
				print("<=>	" + var + "_1 = (" + str_num + " / " + str_den + " - √" + str_delta + ") / " + str_a)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = (" + str_num + " / " + str_den + " + √" + str_delta + ") / " + str_a)
			else :
				num = 1 if not primes1 else primes1[0]
				den = 1 if not primes2 else primes2[0]
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
		print()
		print("<=>	" + var + "_1 = (" + str_num + " / " + str_den + " - \033[31m" + str_den + "\033[32m√" + str_delta + " / \033[31m" + str_den + "\033[32m) / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_num + " / " + str_den + " + \033[31m" + str_den + "\033[32m√" + str_delta + " / \033[31m" + str_den + "\033[32m) / " + str_a)
		print()
		print("<=>	" + var + "_1 = (" + str_num + " - " + str_den + "√" + str_delta + ") / " + str_den + " / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_num + " + " + str_den + "√" + str_delta + ") / " + str_den + " / " + str_a)
		print()
		print("<=>	" + var + "_1 = (" + str_num + " - " + str_den + "√" + str_delta + ") / (" + str_den + " * " + str_a + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_num + " + " + str_den + "√" + str_delta + ") / (" + str_den + " * " + str_a + ")")
		a *= den
		str_a = __utils__.ft_round(a, p)
		print()
		print("<=>	" + var + "_1 = (" + str_num + " - " + str_den + "√" + str_delta + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_num + " + " + str_den + "√" + str_delta + ") / " + str_a)
	k = den
	b = num
	str_k = str_den
	str_b = str_num
	fact = 1
	if a != int(a) :
		mult = __bonus__.irreducible_mult(1, a, p)
		num = int(__utils__.ft_round(mult, 0))
		den = int(__utils__.ft_round(a * mult, 0))
		str_num = __utils__.ft_round(num, 0)
		str_den = __utils__.ft_round(den, 0)
		print()
		print("<=>	" + var + "_1 = " + str_num + "(" + str_b + " - " + str_k + "√" + str_delta + ") / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + "(" + str_b + " + " + str_k + "√" + str_delta + ") / " + str_den)
		primes1 = __bonus__.primes(num)
		primes2 = __bonus__.primes(den)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		num = __bonus__.print_frac(primes1, delete, True)
		den = __bonus__.print_frac(primes2, delete, False)
		if len(num) > 1 or len(den) > 1 :
			print()
			print("<=>	" + var + "_1 = " + num + "(" + str_b + " - " + str_k + "√" + str_delta + ") / " + den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + num + "(" + str_b + " + " + str_k + "√" + str_delta + ") / " + den)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_num = __bonus__.print_frac(primes1, None, True)
			str_den = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = " + str_num + "(" + str_b + " - " + str_k + "√" + str_delta + ") / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + "(" + str_b + " + " + str_k + "√" + str_delta + ") / " + str_den)
			if len(primes1) > 1 or len(primes2) > 1 :
				num, den = __bonus__.irreducible(primes1, primes2)
				str_num = __utils__.ft_round(num, 0)
				str_den = __utils__.ft_round(den, 0)
				print()
				print("<=>	" + var + "_1 = " + str_num + "(" + str_b + " - " + str_k + "√" + str_delta + ") / " + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_num + "(" + str_b + " + " + str_k + "√" + str_delta + ") / " + str_den)
			else :
				num = 1 if not primes1 else primes1[0]
				den = 1 if not primes2 else primes2[0]
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
		fact = num
		a = den
	str_fact = __utils__.ft_round(fact, 0)
	if str_fact == "1" :
		str_fact = ""
	str_a = __utils__.ft_round(a, 0)
	str1 = str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ") / " + str_a
	str2 = str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ") / " + str_a
	if a < 0 :
		fact *= -1
		a *= -1
		str_fact = __utils__.ft_round(fact, 0)
		if str_fact == "1" :
			str_fact = ""
		elif str_fact == "-1" :
			str_fact = "-"
		str_a = " / " + __utils__.ft_round(a, 0)
		str1 = str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ")" + str_a
		str2 = str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ")" + str_a
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		if str_a == " / 1" :
			str_a = ""
			str1 = str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ")"
			str2 = str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ")"
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
		if fact < 0 :
			fact *= -1
			str_fact = __utils__.ft_round(fact, 0)
			if str_fact == "1" :
				str_fact = ""
			num *= -1
			str_num = __utils__.ft_round(num, 0)
			str1 = str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ")" + str_a
			str2 = str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ")" + str_a
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(fact * (num + k * __utils__.ft_sqrt(delta)) / a, 14)
			arround2 = __utils__.ft_round(fact * (num - k * __utils__.ft_sqrt(delta)) / a, 14)
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
			return str2, str1
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
