# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    b_not_int.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 11:51:09 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 11:57:31 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	delta_neg_b_a_notsqrt_apos_bnotint_deltaint(var, a, b, str_b, delta, p) :
	squares, delta_num = __bonus__.reduce_sqrt(delta)
	a2 = a
	str_a2 = __utils__.ft_round(a2, 0)
	if not squares :
		tmp_a2 = 1 / a2
		if tmp_a2 == int(tmp_a2) :
			a2 = tmp_a2
			str_a2 = __utils__.ft_round(a2, 0)
			str_delta = __utils__.ft_round(delta, 0)
			print()
			print("<=>	" + var + "_1 = " + str_b + " - " + str_a2 + "i√" + str_delta)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " + " + str_a2 + "i√" + str_delta)
			arround_b = __utils__.ft_round(b, 14)
			arround_i = __utils__.ft_round(a2 * __utils__.ft_sqrt(delta), 14) + "i"
			print("\033[35m")
			print("<=>	" + var + "_1 ≈ " + arround_b + " - " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround_b + " + " + arround_i)
			if len(arround_b[arround_b.find('.') + 1:]) < 14 :
				str_b = arround_b
			str1 = str_b + " - " + str_a2 + "i√" + __utils__.ft_round(delta_num, 0)
			str2 = str_b + " + " + str_a2 + "i√" + __utils__.ft_round(delta_num, 0)
			return str1, str2
		if a2 == int(a2) :
			arround_b = __utils__.ft_round(b, 14)
			arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta) / a2, 14) + "i"
			print("\033[35m")
			print("<=>	" + var + "_1 ≈ " + arround_b + " - " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround_b + " + " + arround_i)
			if len(arround_b[arround_b.find('.') + 1:]) < 14 :
				str_b = arround_b
			str1 = str_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2
			str2 = str_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2
			return str1, str2
		mult = __bonus__.irreducible_mult(1, a2, p)
		delta_num = int(mult)
		a2 = int(a2 * mult)
		str_delta = __utils__.ft_round(delta, 0)
		str_delta_num = __utils__.ft_round(delta_num, 0)
		str_a2 = __utils__.ft_round(a2, 0)
		print()
		print("<=>	" + var + "_1 = " + str_b + " - " + str_delta_num + "i√" + str_delta + " / " + str_a2)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + " + str_delta_num + "i√" + str_delta + " / " + str_a2)
		primes1 = __bonus__.primes(delta_num)
		primes2 = __bonus__.primes(a2)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		if delete and delete != [1] :
			str_num = __bonus__.print_frac(primes1, delete, True)
			str_den = __bonus__.print_frac(primes2, delete, False)
			str_i = str_num + "i√" + str_delta + " / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str_b + " - " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " + " + str_i)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_num = __bonus__.print_frac(primes1, None, True)
			if str_num == "1" :
				str_num = ""
			str_den = __bonus__.print_frac(primes2, None, False)
			str_i = str_num + "i√" + str_delta + " / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str_b + " - " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " + " + str_i)
			delta_num, a2 = __bonus__.irreducible(primes1, primes2)
			str_i = __utils__.ft_round(delta_num, 0)
			if str_i == "1" :
				str_i = ""
			str_a2 = __utils__.ft_round(a2, 0)
			str_i += "i√" + str_delta + " / " + str_a2
			if len(primes1) > 1 or len(primes2) > 1 :
				print()
				print("<=>	" + var + "_1 = " + str_b + " - " + str_i)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_b + " + " + str_i)
		arround_b = __utils__.ft_round(b, 14)
		arround_i = __utils__.ft_round(delta_num * __utils__.ft_sqrt(delta) / a2, 14) + "i"
		str_delta_num = __utils__.ft_round(delta_num, 0)
		if str_delta_num == "1" :
			str_delta_num = ""
		print("\033[35m")
		print("<=>	" + var + "_1 ≈ " + arround_b + " - " + arround_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 ≈ " + arround_b + " + " + arround_i)
		if len(arround_b[arround_b.find('.') + 1:]) < 14 :
				str_b = arround_b
		str1 = str_b + " - " + str_delta_num + "i√" + str_delta + " / " + str_a2
		str2 = str_b + " + " + str_delta_num + "i√" + str_delta + " / " + str_a2
		return str1, str2
	sq = __bonus__.print_squares(squares, delta_num)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + sq + " / " + str_a2)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + sq + " / " + str_a2)
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = " + str_b + " - i√(" + __utils__.ft_round(tmp, 0) + " * " + __utils__.ft_round(delta_num, 0) + ") / " + str_a2)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + i√(" + __utils__.ft_round(tmp, 0) + " * " + __utils__.ft_round(delta_num, 0) + ") / " + str_a2)
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + __utils__.ft_round(tmp, 0) + "√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + __utils__.ft_round(tmp, 0) + "√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2)
	squares = __utils__.ft_sqrt(tmp)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - " + __utils__.ft_round(squares, 0) + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + " + __utils__.ft_round(squares, 0) + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2)
	tmp_a2 = squares / a2
	str_delta_num = __utils__.ft_round(delta_num, 0)
	if tmp_a2 == int(tmp_a2) :
		a2 = tmp_a2
		str_a2 = __utils__.ft_round(a2, 0)
		if str_a2 == "1" :
			str_a2 = ""
		print()
		print("<=>	" + var + "_1 = " + str_b + " - " + str_a2 + "i√" + str_delta_num)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + " + str_a2 + "i√" + str_delta_num)
		arround_b = __utils__.ft_round(b, 14)
		arround_i = __utils__.ft_round(a2 * __utils__.ft_sqrt(delta_num), 14) + "i"
		print("\033[35m")
		print("<=>	" + var + "_1 ≈ " + arround_b + " - " + arround_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 ≈ " + arround_b + " + " + arround_i)
		if len(arround_b[arround_b.find('.') + 1:]) < 14 :
				str_b = arround_b
		str1 = str_b + " - " + str_a2 + "i√" + str_delta_num
		str2 = str_b + " + " + str_a2 + "i√" + str_delta_num
		return str1, str2
	primes_square = __bonus__.primes(squares)
	primes_den = __bonus__.primes(a2)
	if len(primes_square) > 1 or len(primes_den) > 1 :
		num_d = squares
		den_d = a2
		delete = []
		__bonus__.reduce_fraction(primes_square, primes_den, delete)
		str_num = __bonus__.print_frac(primes_square, delete, True)
		str_den = __bonus__.print_frac(primes_den, delete, False)
		if delete :
			print()
			print("<=>	" + var + "_1 = " + str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			__bonus__.fraction_delete(primes_square, delete.copy())
			__bonus__.fraction_delete(primes_den, delete.copy())
			str_num = __bonus__.print_frac(primes_square, [], True)
			if str_num == "1" or str_num == "-1" :
				str_num = str_num[:-1]
			str_den = __bonus__.print_frac(primes_den, [], False)
			if not str_den :
				str_den = "1"
			print()
			print("<=>	" + var + "_1 = " + str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			num_d, den_d = __bonus__.irreducible(primes_square, primes_den)
			str_num = __utils__.ft_round(num_d, 0) if num_d != 1 else ""
			str_den = " / " + __utils__.ft_round(den_d, 0)
			if str_den == " / 1" :
				str_den = ""
				print()
				print("<=>	" + var + "_1 = " + str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + str_den)
			if len(primes_square) > 1 or len(primes_den) > 1 :
				print()
				print("<=>	" + var + "_1 = " + str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + str_den)
	else :
		num_d = squares
		den_d = a2
	str_num_d = __utils__.ft_round(num_d, 0)
	str_den = " / " + __utils__.ft_round(den_d, 0)
	if str_den == " / 1" :
		str_den = ""
	arround_b = __utils__.ft_round(b, 14)
	arround_i = __utils__.ft_round(num_d * __utils__.ft_sqrt(delta_num) / den_d, 14) + "i"
	print("\033[35m")
	print("<=>	" + var + "_1 ≈ " + arround_b + " - " + arround_i)
	print("	\33[33mor\033[35m")
	print("<=>	" + var + "_2 ≈ " + arround_b + " + " + arround_i)
	if num_d == 1 :
		str_num_d = ""
	elif num_d == -1 :
		str_num_d = "-"
	if len(arround_b[arround_b.find('.') + 1:]) < 14 :
			str_b = arround_b
	str1 = str_b + " - " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + str_den
	str2 = str_b + " + " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + str_den
	return str1, str2

def	delta_neg_b_a_notsqrt_apos_bnotint_deltanotint_deltaden(var, a, b, str_b, delta, sqrt_delta_den, p) :
	str_delta = __utils__.ft_round(delta, 0)
	str_a = __utils__.ft_round(a, p)
	str_sqrt_delta_den = __utils__.ft_round(sqrt_delta_den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + str_delta + " / (" + str_a + " * " + str_sqrt_delta_den + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + str_delta + " / (" + str_a + " * " + str_sqrt_delta_den + ")")
	a *= sqrt_delta_den
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + str_delta + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + str_delta + " / " + str_a)
	return delta_neg_b_a_notsqrt_apos_bnotint_deltaint(var, a, b, str_b, delta, p)

def	delta_neg_b_a_notsqrt_apos_bnotint_deltanotint_notdeltaden(var, a, str_b, delta, delta_den, p) :
	str_delta = __utils__.ft_round(delta, 0)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + str_delta + "√" + str_delta_den + " / (" + str_a + " * " + str_delta_den + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + str_delta + "√" + str_delta_den + " / (" + str_a + " * " + str_delta_den + ")")
	a *= delta_den
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + str_delta + "√" + str_delta_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + str_delta + "√" + str_delta_den + " / " + str_a)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√(" + str_delta + " * " + str_delta_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√(" + str_delta + " * " + str_delta_den + ") / " + str_a)
	delta *= delta_den
	str_delta = __utils__.ft_round(delta, 0)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + str_delta + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + str_delta + " / " + str_a)
	return delta_neg_b_a_notsqrt_apos_bnotint_deltaint(var, a, str_b, delta, p)

def	delta_neg_b_a_notsqrt_apos_bnotint_deltanotint(var, a, b, str_b, delta, p) :
	str_a = __utils__.ft_round(a, p)
	delta_den = 1
	mult = __bonus__.irreducible_mult(delta, delta_den, p)
	delta = int(delta * mult)
	delta_den = int(delta_den * mult)
	str_delta = __utils__.ft_round(delta, 0)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√(" + str_delta + " / " + str_delta_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√(" + str_delta + " / " + str_delta_den + ") / " + str_a)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + str_delta + " / √" + str_delta_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + str_delta + " / √" + str_delta_den + " / " + str_a)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + str_delta + " / " + str_a + "√" + str_delta_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + str_delta + " / " + str_a + "√" + str_delta_den)
	sqrt_delta_den = __utils__.ft_sqrt(delta_den)
	if sqrt_delta_den == int(sqrt_delta_den) :
		return delta_neg_b_a_notsqrt_apos_bnotint_deltanotint_deltaden(var, a, b, str_b, delta, sqrt_delta_den, p)
	return delta_neg_b_a_notsqrt_apos_bnotint_deltanotint_notdeltaden(var, a, str_b, delta, delta_den, p)

def	delta_neg_b_a_notsqrt_apos_bnotint(var, a, b, delta, p) :
	mult = __bonus__.irreducible_mult(int(b), int(a), p)
	a1 = a
	str_b = __utils__.ft_round(b, 0)
	str_a = __utils__.ft_round(a1, p)
	str_a1 = __utils__.ft_round(a1, 0)
	str_i = "i√" + __utils__.ft_round(delta, p) + " / " + str_a
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
	if delta == int(delta) :
		return delta_neg_b_a_notsqrt_apos_bnotint_deltaint(var, a, b / a1, str_b, delta, p)
	return delta_neg_b_a_notsqrt_apos_bnotint_deltanotint(var, a, b / a1, str_b, delta, p)
