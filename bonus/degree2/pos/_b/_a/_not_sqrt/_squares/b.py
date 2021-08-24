# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    b.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/23 20:40:37 by qpupier           #+#    #+#              #
#    Updated: 2021/08/24 16:40:37 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_b_nota_notsqrt_delta_squares_b(var, a, b, k, delta, p) :
	primes1 = __bonus__.primes(b)
	primes2 = __bonus__.primes(k)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	str_b = __bonus__.print_fact(primes1, delete, False)
	str_k = __bonus__.print_fact(primes2, delete, False)
	str_delta = "√" + __utils__.ft_round(delta, 0)
	str_a = __utils__.ft_round(a, p)
	if delete :
		if b != k :
			print()
			print("<=>	" + var + "_1 = (" + str_b + " - " + str_k + str_delta + ") / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = (" + str_b + " + " + str_k + str_delta + ") / " + str_a)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		fact, fact = __bonus__.irreducible(None, delete)
		str_fact = "\033[37m" + __utils__.ft_round(fact, 0) + "\033[32m"
		b, k = __bonus__.irreducible(primes1, primes2)
		if len(delete) > 1 or len(primes1) > 1 or len(primes2) > 1 :
			str_b = " * " + __utils__.ft_round(b, 0)
			str_k = " * " + __utils__.ft_round(k, 0)
			if str_k == " * 1" :
				str_k = ""
			str1 = "(" + str_fact + str_b + " - " + str_fact + str_b + str_delta + ") / " + str_a
			str2 = "(" + str_fact + str_b + " + " + str_fact + str_b + str_delta + ") / " + str_a
			if b != k :
				print()
				print("<=>	" + var + "_1 = " + str1)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str2)
		str_b = __utils__.ft_round(b, 0)
		str_k = __utils__.ft_round(k, 0)
		if str_k == "1" :
			str_k = ""
		str1 = str_fact + "(" + str_b + " - " + str_k + str_delta + ") / " + str_a
		str2 = str_fact + "(" + str_b + " + " + str_k + str_delta + ") / " + str_a
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
	else :
		fact = 1
		str_b = __utils__.ft_round(b, 0)
		str_k = __utils__.ft_round(k, 0)
		if str_k == "1" :
			str_k = ""
		str1 = "(" + str_b + " - " + str_k + str_delta + ") / " + str_a
		str2 = "(" + str_b + " + " + str_k + str_delta + ") / " + str_a
	if fact != int(fact) or a != int(a) :
		mult = __bonus__.irreducible_mult(fact, a, p)
		num = int(__utils__.ft_round(fact * mult, 0))
		den = int(__utils__.ft_round(a * mult, 0))
		str_num = __utils__.ft_round(num, 0)
		str_den = __utils__.ft_round(den, 0)
		str1 = str_num + "(" + str_b + " - " + str_k + str_delta + ") / " + str_den
		str2 = str_num + "(" + str_b + " + " + str_k + str_delta + ") / " + str_den
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		fact = num
		a = den
	primes1 = __bonus__.primes(fact)
	primes2 = __bonus__.primes(a)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	num = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(num) > 1 or len(den) > 1 :
		str1 = num + "(" + str_b + " - " + str_k + str_delta + ") / " + den
		str2 = num + "(" + str_b + " + " + str_k + str_delta + ") / " + den
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		str1 = str_num + "(" + str_b + " - " + str_k + str_delta + ") / " + str_den
		str2 = str_num + "(" + str_b + " + " + str_k + str_delta + ") / " + str_den
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		if len(primes1) > 1 or len(primes2) > 1 :
			num, den = __bonus__.irreducible(primes1, primes2)
			str_num = __utils__.ft_round(num, 0)
			str_den = __utils__.ft_round(den, 0)
			str1 = str_num + "(" + str_b + " - " + str_k + str_delta + ") / " + str_den
			str2 = str_num + "(" + str_b + " + " + str_k + str_delta + ") / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
	else :
		num = 1 if not primes1 else primes1[0]
		den = 1 if not primes2 else primes2[0]
	fact = num
	a = den
	str1 = str1.replace("\033[37m", "").replace("\033[32m", "")
	str2 = str2.replace("\033[37m", "").replace("\033[32m", "")
	if a < 0 :
		fact *= -1
		a *= -1
		str_fact = __utils__.ft_round(fact, 0)
		if str_fact == "1" :
			str_fact = ""
		elif str_fact == "-1" :
			str_fact = "-"
		str_delta = str_delta[1:]
		str_a = " / " + __utils__.ft_round(a, 0)
		str1 = str_fact + "(" + str_b + " - " + str_k + "√" + str_delta + ")" + str_a
		str2 = str_fact + "(" + str_b + " + " + str_k + "√" + str_delta + ")" + str_a
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		if str_a == " / 1" :
			str_a = ""
			str1 = str_fact + "(" + str_b + " - " + str_k + "√" + str_delta + ")"
			str2 = str_fact + "(" + str_b + " + " + str_k + "√" + str_delta + ")"
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
		if fact < 0 :
			fact *= -1
			str_fact = __utils__.ft_round(fact, 0)
			if str_fact == "1" :
				str_fact = ""
			b *= -1
			str_b = __utils__.ft_round(b, 0)
			if str_fact or str_a :
				str1 = str_fact + "(" + str_b + " + " + str_k + "√" + str_delta + ")" + str_a
				str2 = str_fact + "(" + str_b + " - " + str_k + "√" + str_delta + ")" + str_a
			else :
				str1 = str_b + " + " + str_k + "√" + str_delta
				str2 = str_b + " - " + str_k + "√" + str_delta
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(fact * (b + k * __utils__.ft_sqrt(delta)) / a, 14)
			arround2 = __utils__.ft_round(fact * (b - k * __utils__.ft_sqrt(delta)) / a, 14)
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
	arround1 = __utils__.ft_round(fact * (b - k * __utils__.ft_sqrt(delta)) / a, 14)
	arround2 = __utils__.ft_round(fact * (b + k * __utils__.ft_sqrt(delta)) / a, 14)
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
