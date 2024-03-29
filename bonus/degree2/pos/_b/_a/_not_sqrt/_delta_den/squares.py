# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    squares.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/21 18:57:14 by qpupier           #+#    #+#              #
#    Updated: 2021/08/24 16:20:05 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_b_a_notsqrt_notdelta_delta_den_squares(var, b, squares, delta, delta_den, a, p) :
	str_b = __utils__.ft_round(b, p)
	str_delta = __utils__.ft_round(delta, 0)
	sq = __bonus__.print_squares(squares, delta)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + sq + " / " + str_delta_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + sq + " / " + str_delta_den + ") / " + str_a)
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - √(" + __utils__.ft_round(tmp, 0) + " * " + str_delta + ") / " + str_delta_den + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + √(" + __utils__.ft_round(tmp, 0) + " * " + str_delta + ") / " + str_delta_den + ") / " + str_a)
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + __utils__.ft_round(tmp, 0) + "√" + str_delta + " / " + str_delta_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + __utils__.ft_round(tmp, 0) + "√" + str_delta + " / " + str_delta_den + ") / " + str_a)
	squares = __utils__.ft_sqrt(tmp)
	str_squares = __utils__.ft_round(squares, 0) + "√" + str_delta
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - " + str_squares + " / " + str_delta_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + " + str_squares + " / " + str_delta_den + ") / " + str_a)
	primes1 = __bonus__.primes(squares)
	primes2 = __bonus__.primes(delta_den)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	num = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(num) > 1 or len(den) > 1 :
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - " + num + "√" + str_delta + " / " + den + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + " + num + "√" + str_delta + " / " + den + ") / " + str_a)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		if str_num == "1" :
			str_num = ""
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - " + str_num + "√" + str_delta + " / " + str_den + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + " + str_num + "√" + str_delta + " / " + str_den + ") / " + str_a)
		if len(primes1) > 1 or len(primes2) > 1 :
			num, den = __bonus__.irreducible(primes1, primes2)
			str_num = __utils__.ft_round(num, 0)
			if str_num == "1" :
				str_num = ""
			str_den = __utils__.ft_round(den, 0)
			print()
			print("<=>	" + var + "_1 = (" + str_b + " - " + str_num + "√" + str_delta + " / " + str_den + ") / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = (" + str_b + " + " + str_num + "√" + str_delta + " / " + str_den + ") / " + str_a)
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
		squares = num
		delta_den = den
		str_delta_den = __utils__.ft_round(delta_den, 0)
	k = squares
	str_k = __utils__.ft_round(k, 0)
	if str_k == "1" :
		str_k = ""
	if b == int(b) :
		num = b
		den = 1
		str_num = __utils__.ft_round(num, 0)
		print()
		print("<=>	" + var + "_1 = ((" + str_num + "\033[31m * " + str_delta_den + "\033[32m) / \033[31m" + str_delta_den + "\033[32m" + " - " + str_k + "√" + str_delta + " / " + str_delta_den + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = ((" + str_num + "\033[31m * " + str_delta_den + "\033[32m) / \033[31m" + str_delta_den + "\033[32m" + " + " + str_k + "√" + str_delta + " / " + str_delta_den + ") / " + str_a)
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
			print("<=>	" + var + "_1 = (" + str_num + " / " + str_den + " - √" + str_delta + " / " + str_delta_den + ") / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = (" + str_num + " / " + str_den + " + √" + str_delta + " / " + str_delta_den + ") / " + str_a)
			print()
			print("<=>	" + var + "_1 = (" + str_num + "\033[31m * " + str_delta_den + "\033[32m) / (" + str_den + "\033[31m * " + str_delta_den + "\033[32m)" + " - \033[31m" + str_den + "\033[32m√" + str_delta + " / (" + str_delta_den + "\033[31m * " + str_den + "\033[32m)")
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = (" + str_num + "\033[31m * " + str_delta_den + "\033[32m) / (" + str_den + "\033[31m * " + str_delta_den + "\033[32m)" + " + \033[31m" + str_den + "\033[32m√" + str_delta + " / (" + str_delta_den + "\033[31m * " + str_den + "\033[32m)")
			num *= delta_den
			k *= den
			den *= delta_den
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	str_k = __utils__.ft_round(k, 0)
	if str_k == "1" :
		str_k = ""
	str_delta = __utils__.ft_round(delta, 0)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = (" + str_num + " / " + str_den + " - " + str_k + "√" + str_delta + " / " + str_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_num + " / " + str_den + " + " + str_k + "√" + str_delta + " / " + str_den + ") / " + str_a)
	print()
	print("<=>	" + var + "_1 = (" + str_num + " - " + str_k + "√" + str_delta + ") / " + str_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_num + " + " + str_k + "√" + str_delta + ") / " + str_den + " / " + str_a)
	print()
	print("<=>	" + var + "_1 = (" + str_num + " - " + str_k + "√" + str_delta + ") / (" + str_den + " * " + str_a + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_num + " + " + str_k + "√" + str_delta + ") / (" + str_den + " * " + str_a + ")")
	a *= den
	str_den = __utils__.ft_round(a, 0)
	str1 = "(" + str_num + " - " + str_k + "√" + str_delta + ") / " + str_den
	str2 = "(" + str_num + " + " + str_k + "√" + str_delta + ") / " + str_den
	print()
	print("<=>	" + var + "_1 = " + str1)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str2)
	arround1 = __utils__.ft_round((num - k * __utils__.ft_sqrt(delta)) / a, 14)
	arround2 = __utils__.ft_round((num + k * __utils__.ft_sqrt(delta)) / a, 14)
	fact = 1
	if k != 1 :
		primes1 = __bonus__.primes(num)
		primes2 = __bonus__.primes(k)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		str_num = __bonus__.print_fact(primes1, delete, False)
		str_k = __bonus__.print_fact(primes2, delete, False)
		if delete :
			print()
			print("<=>	" + var + "_1 = (" + str_num + " - " + str_k + "√" + str_delta + ") / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = (" + str_num + " + " + str_k + "√" + str_delta + ") / " + str_den)
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
				print()
				print("<=>	" + var + "_1 = (" + str_fact + str_num + " - " + str_fact + str_k + "√" + str_delta + ") / " + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = (" + str_fact + str_num + " + " + str_fact + str_k + "√" + str_delta + ") / " + str_den)
			str_num = __utils__.ft_round(num, 0)
			str_k = __utils__.ft_round(k, 0)
			if str_k == "1" :
				str_k = ""
			print()
			print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ") / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ") / " + str_den)
		else :
			fact = 1
			str_num = __utils__.ft_round(num, 0)
			str_k = __utils__.ft_round(k, 0)
			if str_k == "1" :
				str_k = ""
	if '.' in __utils__.ft_round(a, p) or fact != 1 :
		mult = __bonus__.irreducible_mult(fact, a, p)
		fact = int(__utils__.ft_round(fact * mult, 0))
		a = int(__utils__.ft_round(a * mult, 0))
		str_fact = __utils__.ft_round(fact, 0)
		if str_fact == "1" :
			str_fact = ""
		str_a = __utils__.ft_round(a, 0)
		print()
		print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ") / " + str_a)
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
			print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ") / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ") / " + str_a)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_fact = __bonus__.print_frac(primes1, None, True)
			if str_fact == "1" :
				str_fact = ""
			str_a = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ") / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ") / " + str_a)
			if len(primes1) > 1 or len(primes2) > 1 :
				fact, a = __bonus__.irreducible(primes1, primes2)
				str_fact = __utils__.ft_round(fact, 0)
				if str_fact == "1" :
					str_fact = ""
				str_a = __utils__.ft_round(a, 0)
				print()
				print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ") / " + str_a)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ") / " + str_a)
			else :
				fact = 1 if not primes1 else primes1[0]
				a = 1 if not primes2 else primes2[0]
				str_fact = __utils__.ft_round(fact, 0)
				if str_fact == "1" :
					str_fact = ""
				str_a = __utils__.ft_round(a, 0)
		str1 = str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ") / " + str_a
		str2 = str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ") / " + str_a
		arround1 = __utils__.ft_round(fact * (num - k * __utils__.ft_sqrt(delta)) / a, 14)
		arround2 = __utils__.ft_round(fact * (num + k * __utils__.ft_sqrt(delta)) / a, 14)
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
			if str_fact or str_a :
				str1 = str_fact + "(" + str_num + " + " + str_k + "√" + str_delta + ")" + str_a
				str2 = str_fact + "(" + str_num + " - " + str_k + "√" + str_delta + ")" + str_a
			else :
				str1 = str_num + " + " + str_k + "√" + str_delta
				str2 = str_num + " - " + str_k + "√" + str_delta
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
