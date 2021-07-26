# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    b_int.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 11:37:04 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 19:54:11 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	delta_neg_b_a_notsqrt_aneg_bint_deltaint(var, a, str_b, delta, p) :
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
			print("<=>	" + var + "_1 = " + str_b + " + " + str_a2 + "i√" + str_delta)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_a2 + "i√" + str_delta)
			arround_i = __utils__.ft_round(a2 * __utils__.ft_sqrt(delta), 14) + "i"
			print("\033[35m")
			if len(arround_i[arround_i.find('.') + 1:]) < 15:
				print("<=>	" + var + "_1 = " + str_b + " + " + arround_i)
				print("	\33[33mor\033[35m")
				print("<=>	" + var + "_2 = " + str_b + " - " + arround_i)
				str1 = str_b + " + " + arround_i
				str2 = str_b + " - " + arround_i
			else :
				print("<=>	" + var + "_1 ≈ " + str_b + " + " + arround_i)
				print("	\33[33mor\033[35m")
				print("<=>	" + var + "_2 ≈ " + str_b + " - " + arround_i)
				str1 = str_b + " + " + str_a2 + "i√" + __utils__.ft_round(delta_num, 0)
				str2 = str_b + " - " + str_a2 + "i√" + __utils__.ft_round(delta_num, 0)
			return str2, str1
		if a2 == int(a2) :
			arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta) / a2, 14) + "i"
			print("\033[35m")
			if len(arround_i[arround_i.find('.') + 1:]) < 15:
				print("<=>	" + var + "_1 = " + str_b + " + " + arround_i)
				print("	\33[33mor\033[35m")
				print("<=>	" + var + "_2 = " + str_b + " - " + arround_i)
				str1 = str_b + " + " + arround_i
				str2 = str_b + " - " + arround_i
			else :
				print("<=>	" + var + "_1 ≈ " + str_b + " + " + arround_i)
				print("	\33[33mor\033[35m")
				print("<=>	" + var + "_2 ≈ " + str_b + " - " + arround_i)
				str1 = str_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2
				str2 = str_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2
			return str2, str1
		mult = __bonus__.irreducible_mult(1, a2, p)
		delta_num = int(mult)
		a2 = int(a2 * mult)
		str_delta = __utils__.ft_round(delta, 0)
		str_delta_num = __utils__.ft_round(delta_num, 0)
		str_a2 = __utils__.ft_round(a2, 0)
		print()
		print("<=>	" + var + "_1 = " + str_b + " + " + str_delta_num + "i√" + str_delta + " / " + str_a2)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - " + str_delta_num + "i√" + str_delta + " / " + str_a2)
		primes1 = __bonus__.primes(delta_num)
		primes2 = __bonus__.primes(a2)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		if delete and delete != [1] :
			str_num = __bonus__.print_frac(primes1, delete, True)
			str_den = __bonus__.print_frac(primes2, delete, False)
			str_i = str_num + "i√" + str_delta + " / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_i)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_num = __bonus__.print_frac(primes1, None, True)
			if str_num == "1" :
				str_num = ""
			str_den = __bonus__.print_frac(primes2, None, False)
			str_i = str_num + "i√" + str_delta + " / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_i)
			delta_num, a2 = __bonus__.irreducible(primes1, primes2)
			str_i = __utils__.ft_round(delta_num, 0)
			if str_i == "1" :
				str_i = ""
			str_a2 = __utils__.ft_round(a2, 0)
			str_i += "i√" + str_delta + " / " + str_a2
			if len(primes1) > 1 or len(primes2) > 1 :
				print()
				print("<=>	" + var + "_1 = " + str_b + " + " + str_i)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_b + " - " + str_i)
		arround_i = __utils__.ft_round(delta_num * __utils__.ft_sqrt(delta) / a2, 14) + "i"
		str_delta_num = __utils__.ft_round(delta_num, 0)
		if str_delta_num == "1" :
			str_delta_num = ""
		print("\033[35m")
		if len(arround_i[arround_i.find('.') + 1:]) < 15:
			print("<=>	" + var + "_1 = " + str_b + " + " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + str_b + " - " + arround_i)
			str1 = str_b + " + " + arround_i
			str2 = str_b + " - " + arround_i
		else :
			print("<=>	" + var + "_1 ≈ " + str_b + " + " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + str_b + " - " + arround_i)
			str1 = str_b + " + " + str_delta_num + "i√" + str_delta + " / " + str_a2
			str2 = str_b + " - " + str_delta_num + "i√" + str_delta + " / " + str_a2
		return str2, str1
	sq = __bonus__.print_squares(squares, delta_num)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + sq + " / " + str_a2)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + sq + " / " + str_a2)
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = " + str_b + " + i√(" + __utils__.ft_round(tmp, 0) + " * " + __utils__.ft_round(delta_num, 0) + ") / " + str_a2)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - i√(" + __utils__.ft_round(tmp, 0) + " * " + __utils__.ft_round(delta_num, 0) + ") / " + str_a2)
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + __utils__.ft_round(tmp, 0) + "√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + __utils__.ft_round(tmp, 0) + "√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2)
	squares = __utils__.ft_sqrt(tmp)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + " + __utils__.ft_round(squares, 0) + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - " + __utils__.ft_round(squares, 0) + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2)
	tmp_a2 = squares / a2
	str_delta_num = __utils__.ft_round(delta_num, 0)
	if tmp_a2 == int(tmp_a2) :
		a2 = tmp_a2
		str_a2 = __utils__.ft_round(a2, 0)
		if str_a2 == "1" :
			str_a2 = ""
		print()
		print("<=>	" + var + "_1 = " + str_b + " + " + str_a2 + "i√" + str_delta_num)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - " + str_a2 + "i√" + str_delta_num)
		arround_i = __utils__.ft_round(a2 * __utils__.ft_sqrt(delta_num), 14) + "i"
		print("\033[35m")
		if len(arround_i[arround_i.find('.') + 1:]) < 15:
			print("<=>	" + var + "_1 = " + str_b + " + " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + str_b + " - " + arround_i)
			str1 = str_b + " + " + arround_i
			str2 = str_b + " - " + arround_i
		else :
			print("<=>	" + var + "_1 ≈ " + str_b + " + " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + str_b + " - " + arround_i)
			str1 = str_b + " + " + str_a2 + "i√" + str_delta_num
			str2 = str_b + " - " + str_a2 + "i√" + str_delta_num
		return str2, str1
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
			print("<=>	" + var + "_1 = " + str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			__bonus__.fraction_delete(primes_square, delete.copy())
			__bonus__.fraction_delete(primes_den, delete.copy())
			str_num = __bonus__.print_frac(primes_square, [], True)
			if str_num == "1" or str_num == "-1" :
				str_num = str_num[:-1]
			str_den = __bonus__.print_frac(primes_den, [], False)
			if not str_den :
				str_den = "1"
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			num_d, den_d = __bonus__.irreducible(primes_square, primes_den)
			str_num = __utils__.ft_round(num_d, 0) if num_d != 1 else ""
			str_den = " / " + __utils__.ft_round(den_d, 0)
			if str_den == " / 1" :
				str_den = ""
				print()
				print("<=>	" + var + "_1 = " + str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + str_den)
			if len(primes_square) > 1 or len(primes_den) > 1 :
				print()
				print("<=>	" + var + "_1 = " + str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + str_den)
	else :
		num_d = squares
		den_d = a2
	str_num_d = __utils__.ft_round(num_d, 0)
	str_den = " / " + __utils__.ft_round(den_d, 0)
	if str_den == " / 1" :
		str_den = ""
	arround_i = __utils__.ft_round(num_d * __utils__.ft_sqrt(delta_num) / den_d, 14) + "i"
	print("\033[35m")
	if len(arround_i[arround_i.find('.') + 1:]) < 14 :
		print("<=>	" + var + "_1 = " + str_b + " + " + arround_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + str_b + " - " + arround_i)
		str1 = str_b + " + " + arround_i
		str2 = str_b + " - " + arround_i
	else :
		print("<=>	" + var + "_1 ≈ " + str_b + " + " + arround_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 ≈ " + str_b + " - " + arround_i)
		if num_d == 1 :
			str_num_d = ""
		elif num_d == -1 :
			str_num_d = "-"
		str1 = str_b + " + " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + str_den
		str2 = str_b + " - " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + str_den
	return str2, str1

def	delta_neg_b_a_notsqrt_aneg_bint_deltanotint_deltaden(var, a, str_b, delta, sqrt_delta_den, p) :
	str_delta = __utils__.ft_round(delta, 0)
	str_a = __utils__.ft_round(a, p)
	str_sqrt_delta_den = __utils__.ft_round(sqrt_delta_den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + str_delta + " / (" + str_a + " * " + str_sqrt_delta_den + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + str_delta + " / (" + str_a + " * " + str_sqrt_delta_den + ")")
	a *= sqrt_delta_den
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + str_delta + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + str_delta + " / " + str_a)
	return delta_neg_b_a_notsqrt_aneg_bint_deltaint(var, a, str_b, delta, p)

def	delta_neg_b_a_notsqrt_aneg_bint_deltanotint_notdeltaden(var, a, str_b, delta, delta_den, p) :
	str_delta = __utils__.ft_round(delta, 0)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + str_delta + "√" + str_delta_den + " / (" + str_a + " * " + str_delta_den + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + str_delta + "√" + str_delta_den + " / (" + str_a + " * " + str_delta_den + ")")
	a *= delta_den
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + str_delta + "√" + str_delta_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + str_delta + "√" + str_delta_den + " / " + str_a)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√(" + str_delta + " * " + str_delta_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√(" + str_delta + " * " + str_delta_den + ") / " + str_a)
	delta *= delta_den
	str_delta = __utils__.ft_round(delta, 0)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + str_delta + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + str_delta + " / " + str_a)
	return delta_neg_b_a_notsqrt_aneg_bint_deltaint(var, a, str_b, delta, p)

def	delta_neg_b_a_notsqrt_aneg_bint_deltanotint(var, a, str_b, delta, p) :
	str_a = __utils__.ft_round(a, p)
	delta_den = 1
	mult = __bonus__.irreducible_mult(delta, delta_den, p)
	delta = int(delta * mult)
	delta_den = int(delta_den * mult)
	str_delta = __utils__.ft_round(delta, 0)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√(" + str_delta + " / " + str_delta_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√(" + str_delta + " / " + str_delta_den + ") / " + str_a)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + str_delta + " / √" + str_delta_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + str_delta + " / √" + str_delta_den + " / " + str_a)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + str_delta + " / " + str_a + "√" + str_delta_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + str_delta + " / " + str_a + "√" + str_delta_den)
	sqrt_delta_den = __utils__.ft_sqrt(delta_den)
	if sqrt_delta_den == int(sqrt_delta_den) :
		return delta_neg_b_a_notsqrt_aneg_bint_deltanotint_deltaden(var, a, str_b, delta, sqrt_delta_den, p)
	return delta_neg_b_a_notsqrt_aneg_bint_deltanotint_notdeltaden(var, a, str_b, delta, delta_den, p)

def	delta_neg_b_a_notsqrt_aneg_bint(var, a, b, delta, p) :
	b /= a
	str_b = __utils__.ft_round(b, 0)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + __utils__.ft_round(delta, p) + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + __utils__.ft_round(delta, p) + " / " + str_a)
	if delta == int(delta) :
		return delta_neg_b_a_notsqrt_aneg_bint_deltaint(var, a, str_b, delta, p)
	return delta_neg_b_a_notsqrt_aneg_bint_deltanotint(var, a, str_b, delta, p)
