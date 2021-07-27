# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 11:36:50 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 14:07:11 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	delta_neg_b_a_notsqrt_aneg_not_delta(var, b, str_b, delta) :
	delta_num = delta
	squares, delta_num = __bonus__.reduce_sqrt(delta_num)
	if not squares :
		arround_b = __utils__.ft_round(b, 14)
		arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta), 14) + "i"
		print("\033[35m")
		if len(arround_b[arround_b.find('.') + 1:]) < 14 and len(arround_i[arround_i.find('.') + 1:]) < 15:
			print("<=>	" + var + "_1 = " + arround_b + " + " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + arround_b + " - " + arround_i)
			str1 = arround_b + " + " + arround_i
			str2 = arround_b + " - " + arround_i
		else :
			print("<=>	" + var + "_1 ≈ " + arround_b + " + " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround_b + " - " + arround_i)
			if len(arround_b[arround_b.find('.') + 1:]) < 14 :
				str1 = arround_b + " + i√" + __utils__.ft_round(delta_num, 0)
				str2 = arround_b + " - i√" + __utils__.ft_round(delta_num, 0)
			elif len(arround_i[arround_i.find('.') + 1:]) < 15 :
				str1 = str_b + " + " + arround_i
				str2 = str_b + " - " + arround_i
			else :
				str1 = str_b + " + i√" + __utils__.ft_round(delta_num, 0)
				str2 = str_b + " - i√" + __utils__.ft_round(delta_num, 0)
		return str2, str1
	sq = __bonus__.print_squares(squares, delta_num)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + sq)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + sq)
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = " + str_b + " + i√(" + __utils__.ft_round(tmp, 0) + " * " + __utils__.ft_round(delta_num, 0) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - i√(" + __utils__.ft_round(tmp, 0) + " * " + __utils__.ft_round(delta_num, 0) + ")")
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + __utils__.ft_round(tmp, 0) + "√" + __utils__.ft_round(delta_num, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + __utils__.ft_round(tmp, 0) + "√" + __utils__.ft_round(delta_num, 0))
	squares = __utils__.ft_sqrt(tmp)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + " + __utils__.ft_round(squares, 0) + "i√" + __utils__.ft_round(delta_num, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - " + __utils__.ft_round(squares, 0) + "i√" + __utils__.ft_round(delta_num, 0))
	arround_b = __utils__.ft_round(b, 14)
	arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta), 14) + "i"
	print("\033[35m")
	if len(arround_b[arround_b.find('.') + 1:]) < 14 and len(arround_i[arround_i.find('.') + 1:]) < 15:
		print("<=>	" + var + "_1 = " + arround_b + " + " + arround_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + arround_b + " - " + arround_i)
		str1 = arround_b + " + " + arround_i
		str2 = arround_b + " - " + arround_i
	else :
		print("<=>	" + var + "_1 ≈ " + arround_b + " + " + arround_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 ≈ " + arround_b + " - " + arround_i)
		str_num = __utils__.ft_round(squares, 0)
		if len(arround_b[arround_b.find('.') + 1:]) < 14 :
			str1 = arround_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0)
			str2 = arround_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0)
		elif len(arround_i[arround_i.find('.') + 1:]) < 15 :
			str1 = str_b + " + " + arround_i
			str2 = str_b + " - " + arround_i
		else :
			str1 = str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0)
			str2 = str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0)
	return str2, str1

def	delta_neg_b_a_notsqrt_aneg_not_notdelta_deltaden(var, b, str_b, delta, delta_num, delta_den_sqrt) :
	delta_num_sqrt = __utils__.ft_sqrt(delta_num)
	if delta_num_sqrt == int(delta_num_sqrt) :
		print()
		print("<=>	" + var + "_1 = " + str_b + " + " + __utils__.ft_round(delta_num_sqrt, 0) + "i / " + __utils__.ft_round(delta_den_sqrt, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - " + __utils__.ft_round(delta_num_sqrt, 0) + "i / " + __utils__.ft_round(delta_den_sqrt, 0))
		primes1 = __bonus__.primes(delta_num_sqrt)
		primes2 = __bonus__.primes(delta_den_sqrt)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		new_num = __bonus__.print_frac(primes1, delete, True)
		new_den = __bonus__.print_frac(primes2, delete, False)
		if delete and (len(new_num) > 1 or len(new_den) > 1) :
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + new_num + "i / " + new_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + new_num + "i / " + new_den)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_new_num = __bonus__.print_frac(primes1, None, True)
			str_new_den = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + str_new_num + "i / " + str_new_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_new_num + "i / " + str_new_den)
			if len(primes1) > 1 or len(primes2) > 1 :
				new_num, new_den = __bonus__.irreducible(primes1, primes2)
				print()
				print("<=>	" + var + "_1 = " + str_b + " + " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0))
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_b + " - " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0))
			else :
				new_num = 1 if not primes1 else primes1[0]
				new_den = 1 if not primes2 else primes2[0]
		else :
			new_num = delta_num_sqrt
			new_den = delta_den_sqrt
		arround_b = __utils__.ft_round(b, 14)
		arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta), 14) + "i"
		print("\033[35m")
		if len(arround_b[arround_b.find('.') + 1:]) < 14 and len(arround_i[arround_i.find('.') + 1:]) < 15:
			print("<=>	" + var + "_1 = " + arround_b + " + " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + arround_b + " - " + arround_i)
			str1 = arround_b + " + " + arround_i
			str2 = arround_b + " - " + arround_i
		else :
			print("<=>	" + var + "_1 ≈ " + arround_b + " + " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround_b + " - " + arround_i)
			if len(arround_b[arround_b.find('.') + 1:]) < 14 :
				str1 = arround_b + " + " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0)
				str2 = arround_b + " - " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0)
			elif len(arround_i[arround_i.find('.') + 1:]) < 15 :
				str1 = str_b + " + " + arround_i
				str2 = str_b + " - " + arround_i
			else :
				str1 = str_b + " + " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0)
				str2 = str_b + " - " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0)
		return str2, str1
	squares, delta_num = __bonus__.reduce_sqrt(delta_num)
	if not squares :
		arround_b = __utils__.ft_round(b, 14)
		arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta), 14) + "i"
		print("\033[35m")
		if len(arround_b[arround_b.find('.') + 1:]) < 14 and len(arround_i[arround_i.find('.') + 1:]) < 15:
			print("<=>	" + var + "_1 = " + arround_b + " + " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + arround_b + " - " + arround_i)
			str1 = arround_b + " + " + arround_i
			str2 = arround_b + " - " + arround_i
		else :
			print("<=>	" + var + "_1 ≈ " + arround_b + " + " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround_b + " - " + arround_i)
			if len(arround_b[arround_b.find('.') + 1:]) < 14 :
				str1 = arround_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0)
				str2 = arround_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0)
			elif len(arround_i[arround_i.find('.') + 1:]) < 15 :
				str1 = str_b + " + " + arround_i
				str2 = str_b + " - " + arround_i
			else :
				str1 = str_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0)
				str2 = str_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0)
		return str2, str1
	sq = __bonus__.print_squares(squares, delta_num)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + sq + " / " + __utils__.ft_round(delta_den_sqrt, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + sq + " / " + __utils__.ft_round(delta_den_sqrt, 0))
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = " + str_b + " + i√(" + __utils__.ft_round(tmp, 0) + " * " + __utils__.ft_round(delta_num, 0) + ") / " + __utils__.ft_round(delta_den_sqrt, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - i√(" + __utils__.ft_round(tmp, 0) + " * " + __utils__.ft_round(delta_num, 0) + ") / " + __utils__.ft_round(delta_den_sqrt, 0))
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + __utils__.ft_round(tmp, 0) + "√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + __utils__.ft_round(tmp, 0) + "√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
	squares = __utils__.ft_sqrt(tmp)
	primes_square = __bonus__.primes(squares)
	primes_den = __bonus__.primes(delta_den_sqrt)
	if len(primes_square) > 1 or len(primes_den) > 1 :
		print()
		print("<=>	" + var + "_1 = " + str_b + " + " + __utils__.ft_round(squares, 0) + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - " + __utils__.ft_round(squares, 0) + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
	num_d = squares
	den_d = delta_den_sqrt
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
		str_den = __utils__.ft_round(den_d, 0)
		if len(primes_square) > 1 or len(primes_den) > 1 :
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
	arround_b = __utils__.ft_round(b, 14)
	arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta), 14) + "i"
	print("\033[35m")
	if len(arround_b[arround_b.find('.') + 1:]) < 14 and len(arround_i[arround_i.find('.') + 1:]) < 15:
		print("<=>	" + var + "_1 = " + arround_b + " + " + arround_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + arround_b + " - " + arround_i)
		str1 = arround_b + " + " + arround_i
		str2 = arround_b + " - " + arround_i
	else :
		print("<=>	" + var + "_1 ≈ " + arround_b + " + " + arround_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 ≈ " + arround_b + " - " + arround_i)
		str_num_d = __utils__.ft_round(num_d, 0)
		if num_d == 1 :
			str_num_d = ""
		elif num_d == -1 :
			str_num_d = "-"
		if len(arround_b[arround_b.find('.') + 1:]) < 14 :
			str1 = arround_b + " + " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(den_d, 0)
			str2 = arround_b + " - " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(den_d, 0)
		elif len(arround_i[arround_i.find('.') + 1:]) < 15 :
			str1 = str_b + " + " + arround_i
			str2 = str_b + " - " + arround_i
		else :
			str1 = str_b + " + " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(den_d, 0)
			str2 = str_b + " - " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(den_d, 0)
	return str2, str1

def	delta_neg_b_a_notsqrt_aneg_not_notdelta(var, b, str_b, delta, p) :
	mult = __bonus__.irreducible_mult(delta, 1, p)
	delta_num = int(delta * mult)
	delta_den = int(mult)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ")")
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0))
	delta_den_sqrt = __utils__.ft_sqrt(delta_den)
	if delta_den_sqrt == int(delta_den_sqrt) :
		print()
		print("<=>	" + var + "_1 = " + str_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
		return delta_neg_b_a_notsqrt_aneg_not_notdelta_deltaden(var, b, str_b, delta, delta_num, delta_den_sqrt)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0))
	delta_num *= delta_den
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0))
	return delta_neg_b_a_notsqrt_aneg_not_notdelta_deltaden(var, b, str_b, delta, delta_num, delta_den)

def	delta_neg_b_a_notsqrt_aneg_not(var, b, delta, p) :
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " + i√" + __utils__.ft_round(delta, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - i√" + __utils__.ft_round(delta, p))
	str_i = "i√" + __utils__.ft_round(delta, p)
	a1 = 1
	if b == int(b) :
		str_b = __utils__.ft_round(b, 0)
	else :
		str_b = __utils__.ft_round(b, p)
		mult = __bonus__.irreducible_mult(b, 1, p)
		str_a1 = __utils__.ft_round(a1, 0)
		if mult > 1 :
			b = int(b * mult)
			a1 = int(a1 * mult)
			str_b = __utils__.ft_round(b, p) + " / " + __utils__.ft_round(a1, p)
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_i)
		primes1 = __bonus__.primes(b)
		primes2 = __bonus__.primes(a1)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		if delete and delete != [1] :
			str_num = __bonus__.print_frac(primes1, delete, True)
			str_den = __bonus__.print_frac(primes2, delete, False)
			str_b = str_num + " / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_i)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_num = __bonus__.print_frac(primes1, None, True)
			str_den = __bonus__.print_frac(primes2, None, False)
			str_b = str_num + " / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_i)
			b, a1 = __bonus__.irreducible(primes1, primes2)
			str_b = __utils__.ft_round(b, 0)
			str_a1 = __utils__.ft_round(a1, 0)
			str_b += " / " + str_a1
			if len(primes1) > 1 or len(primes2) > 1 :
				print()
				print("<=>	" + var + "_1 = " + str_b + " + " + str_i)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_b + " - " + str_i)
	if delta == int(delta) :
		return delta_neg_b_a_notsqrt_aneg_not_delta(var, b / a1, str_b, delta)
	return delta_neg_b_a_notsqrt_aneg_not_notdelta(var, b / a1, str_b, delta, p)