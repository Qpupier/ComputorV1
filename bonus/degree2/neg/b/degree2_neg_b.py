# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree2_neg_b.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/14 15:04:11 by qpupier           #+#    #+#              #
#    Updated: 2021/07/19 15:48:06 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	delta_neg_b_nota_notsqrt_notdelta(var, b, p) :
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i")
	str1 = str_b + " - i"
	str2 = str_b + " + i"
	if b == int(b) :
		return str1, str2
	mult = __bonus__.irreducible_mult(b, 1, p)
	b_num = int(b * mult)
	b_den = int(mult)
	print()
	print("<=>	" + var + "_1 = " + __utils__.ft_round(b_num, 0) + " / " + __utils__.ft_round(b_den, 0) + " - i")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + __utils__.ft_round(b_num, 0) + " / " + __utils__.ft_round(b_den, 0) + " + i")
	primes1 = __bonus__.primes(b_num)
	primes2 = __bonus__.primes(b_den)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	num = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(num) > 1 or len(den) > 1 :
		print()
		print("<=>	" + var + "_1 = " + num + " / " + den + " - i")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + " / " + den + " + i")
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - i")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den + " + i")
		if len(primes1) > 1 or len(primes2) > 1 :
			num, den = __bonus__.irreducible(primes1, primes2)
			print()
			print("<=>	" + var + "_1 = " + __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " - i")
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " + i")
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
	else :
		num = b_num
		den = b_den
	str1 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " - i"
	str2 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " + i"
	arround = __utils__.ft_round(num / den, 14)
	print("\033[35m")
	if len(arround[arround.find('.') + 1:]) < 14 :
		print("<=>	" + var + "_1 = " + arround + " - i")
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 = " + arround + " + i")
		str1 = arround + " - i"
		str2 = arround + " + i"
	else :
		print("<=>	" + var + "_1 ≈ " + arround + " - i")
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 ≈ " + arround + " + i")
	return str1, str2

def	delta_neg_b_nota_notsqrt(var, b, delta_sqrt, p) :
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - " + __utils__.ft_round(delta_sqrt, 0) + "i")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + " + __utils__.ft_round(delta_sqrt, 0) + "i")
	if delta_sqrt == 1 :
		return delta_neg_b_nota_notsqrt_notdelta(var, b, p)
	str1 = str_b + " - " + __utils__.ft_round(delta_sqrt, 0) + "i"
	str2 = str_b + " + " + __utils__.ft_round(delta_sqrt, 0) + "i"
	if b == int(b) :
		return str1, str2
	i1 = " - " + __utils__.ft_round(delta_sqrt, 0) + "i"
	i2 = " + " + __utils__.ft_round(delta_sqrt, 0) + "i"
	str1 = str_b + i1
	str2 = str_b + i2
	if b == int(b) :
		return str1, str2
	mult = __bonus__.irreducible_mult(b, 1, p)
	b_num = int(b * mult)
	b_den = int(mult)
	print()
	print("<=>	" + var + "_1 = " + __utils__.ft_round(b_num, 0) + " / " + __utils__.ft_round(b_den, 0) + i1)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + __utils__.ft_round(b_num, 0) + " / " + __utils__.ft_round(b_den, 0) + i2)
	primes1 = __bonus__.primes(b_num)
	primes2 = __bonus__.primes(b_den)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	num = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(num) > 1 or len(den) > 1 :
		print()
		print("<=>	" + var + "_1 = " + num + " / " + den + i1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + " / " + den + i2)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + i1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den + i2)
		if len(primes1) > 1 or len(primes2) > 1 :
			num, den = __bonus__.irreducible(primes1, primes2)
			print()
			print("<=>	" + var + "_1 = " + __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + i1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + i2)
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
	else :
		num = b_num
		den = b_den
	str1 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + i1
	str2 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + i2
	arround = __utils__.ft_round(num / den, 14)
	print("\033[35m")
	if len(arround[arround.find('.') + 1:]) < 14 :
		print("<=>	" + var + "_1 = " + arround + i1)
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 = " + arround + i2)
		str1 = arround + i1
		str2 = arround + i2
	else :
		print("<=>	" + var + "_1 ≈ " + arround + i1)
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 ≈ " + arround + i2)
	return str1, str2

def	delta_neg_b_nota_sqrt_deltaden(var, num, den, str_b, delta, delta_num, delta_den_sqrt) :
	delta_num_sqrt = __utils__.ft_sqrt(delta_num)
	if delta_num_sqrt == int(delta_num_sqrt) :
		print()
		print("<=>	" + var + "_1 = " + str_b + " - " + __utils__.ft_round(delta_num_sqrt, 0) + "i / " + __utils__.ft_round(delta_den_sqrt, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + " + __utils__.ft_round(delta_num_sqrt, 0) + "i / " + __utils__.ft_round(delta_den_sqrt, 0))
		primes1 = __bonus__.primes(delta_num_sqrt)
		primes2 = __bonus__.primes(delta_den_sqrt)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		new_num = __bonus__.print_frac(primes1, delete, True)
		new_den = __bonus__.print_frac(primes2, delete, False)
		if delete and (len(new_num) > 1 or len(new_den) > 1) :
			print()
			print("<=>	" + var + "_1 = " + str_b + " - " + new_num + "i / " + new_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " + " + new_num + "i / " + new_den)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_new_num = __bonus__.print_frac(primes1, None, True)
			str_new_den = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = " + str_b + " - " + str_new_num + "i / " + str_new_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " + " + str_new_num + "i / " + str_new_den)
			if len(primes1) > 1 or len(primes2) > 1 :
				new_num, new_den = __bonus__.irreducible(primes1, primes2)
				print()
				print("<=>	" + var + "_1 = " + str_b + " - " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0))
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_b + " + " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0))
			else :
				new_num = 1 if not primes1 else primes1[0]
				new_den = 1 if not primes2 else primes2[0]
		else :
			new_num = delta_num_sqrt
			new_den = delta_den_sqrt
		arround_b = __utils__.ft_round(num / den, 14)
		arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta), 14) + "i"
		print("\033[35m")
		if len(arround_b[arround_b.find('.') + 1:]) < 14 and len(arround_i[arround_i.find('.') + 1:]) < 15:
			print("<=>	" + var + "_1 = " + arround_b + " - " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + arround_b + " + " + arround_i)
			str1 = arround_b + " - " + arround_i
			str2 = arround_b + " + " + arround_i
		else :
			print("<=>	" + var + "_1 ≈ " + arround_b + " - " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround_b + " + " + arround_i)
			if len(arround_b[arround_b.find('.') + 1:]) < 14 :
				str1 = arround_b + " - " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0)
				str2 = arround_b + " + " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0)
			elif len(arround_i[arround_i.find('.') + 1:]) < 15 :
				str1 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " - " + arround_i
				str2 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " + " + arround_i
			else :
				str1 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " - " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0)
				str2 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " + " + __utils__.ft_round(new_num, 0) + "i / " + __utils__.ft_round(new_den, 0)
		return str1, str2
	squares, delta_num = __bonus__.reduce_sqrt(delta_num)
	if not squares :
		arround_b = __utils__.ft_round(num / den, 14)
		arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta), 14) + "i"
		print("\033[35m")
		if len(arround_b[arround_b.find('.') + 1:]) < 14 and len(arround_i[arround_i.find('.') + 1:]) < 15:
			print("<=>	" + var + "_1 = " + arround_b + " - " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + arround_b + " + " + arround_i)
			str1 = arround_b + " - " + arround_i
			str2 = arround_b + " + " + arround_i
		else :
			print("<=>	" + var + "_1 ≈ " + arround_b + " - " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround_b + " + " + arround_i)
			if len(arround_b[arround_b.find('.') + 1:]) < 14 :
				str1 = arround_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0)
				str2 = arround_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0)
			elif len(arround_i[arround_i.find('.') + 1:]) < 15 :
				str1 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " - " + arround_i
				str2 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " + " + arround_i
			else :
				str1 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0)
				str2 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0)
		return str1, str2
	sq = __bonus__.print_squares(squares, delta_num)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + sq + " / " + __utils__.ft_round(delta_den_sqrt, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + sq + " / " + __utils__.ft_round(delta_den_sqrt, 0))
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = " + str_b + " - i√(" + __utils__.ft_round(tmp, 0) + " * " + __utils__.ft_round(delta_num, 0) + ") / " + __utils__.ft_round(delta_den_sqrt, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + i√(" + __utils__.ft_round(tmp, 0) + " * " + __utils__.ft_round(delta_num, 0) + ") / " + __utils__.ft_round(delta_den_sqrt, 0))
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + __utils__.ft_round(tmp, 0) + "√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + __utils__.ft_round(tmp, 0) + "√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
	squares = __utils__.ft_sqrt(tmp)
	primes_square = __bonus__.primes(squares)
	primes_den = __bonus__.primes(delta_den_sqrt)
	if len(primes_square) > 1 or len(primes_den) > 1 :
		print()
		print("<=>	" + var + "_1 = " + str_b + " - " + __utils__.ft_round(squares, 0) + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + " + __utils__.ft_round(squares, 0) + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
	num_d = squares
	den_d = delta_den_sqrt
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
		str_den = __utils__.ft_round(den_d, 0)
		if len(primes_square) > 1 or len(primes_den) > 1 :
			print()
			print("<=>	" + var + "_1 = " + str_b + " - " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " + " + str_num + "i√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
	arround_b = __utils__.ft_round(num / den, 14)
	arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta), 14) + "i"
	print("\033[35m")
	if len(arround_b[arround_b.find('.') + 1:]) < 14 and len(arround_i[arround_i.find('.') + 1:]) < 15:
		print("<=>	" + var + "_1 = " + arround_b + " - " + arround_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + arround_b + " + " + arround_i)
		str1 = arround_b + " - " + arround_i
		str2 = arround_b + " + " + arround_i
	else :
		print("<=>	" + var + "_1 ≈ " + arround_b + " - " + arround_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 ≈ " + arround_b + " + " + arround_i)
		str_num_d = __utils__.ft_round(num_d, 0)
		if num_d == 1 :
			str_num_d = ""
		elif num_d == -1 :
			str_num_d = "-"
		if len(arround_b[arround_b.find('.') + 1:]) < 14 :
			str1 = arround_b + " - " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(den_d, 0)
			str2 = arround_b + " + " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(den_d, 0)
		elif len(arround_i[arround_i.find('.') + 1:]) < 15 :
			str1 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " - " + arround_i
			str2 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " + " + arround_i
		else :
			str1 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " - " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(den_d, 0)
			str2 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " + " + str_num_d + "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(den_d, 0)
	return str1, str2

def	delta_neg_b_nota_sqrt(var, num, den, delta, p) :
	str_b = __utils__.ft_round(num, 0)
	if den != 1 :
		str_b += " / " + __utils__.ft_round(den, 0)
	if delta == int(delta) :
		arround_b = __utils__.ft_round(num / den, 14)
		arround_i = __utils__.ft_round(__utils__.ft_sqrt(delta), 14) + "i"
		print("\033[35m")
		if len(arround_b[arround_b.find('.') + 1:]) < 14 and len(arround_i[arround_i.find('.') + 1:]) < 15:
			print("<=>	" + var + "_1 = " + arround_b + " - " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + arround_b + " + " + arround_i)
			str1 = arround_b + " - " + arround_i
			str2 = arround_b + " + " + arround_i
		else :
			print("<=>	" + var + "_1 ≈ " + arround_b + " - " + arround_i)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround_b + " + " + arround_i)
			if len(arround_b[arround_b.find('.') + 1:]) < 14 :
				str1 = arround_b + " - i√" + __utils__.ft_round(delta, 0)
				str2 = arround_b + " + i√" + __utils__.ft_round(delta, 0)
			elif len(arround_i[arround_i.find('.') + 1:]) < 15 :
				str1 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " - " + arround_i
				str2 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " + " + arround_i
			else :
				str1 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " - i√" + __utils__.ft_round(delta, 0)
				str2 = __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + " + i√" + __utils__.ft_round(delta, 0)
		return str1, str2
	mult = __bonus__.irreducible_mult(delta, 1, p)
	delta_num = int(delta * mult)
	delta_den = int(mult)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ")")
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0))
	delta_den_sqrt = __utils__.ft_sqrt(delta_den)
	if delta_den_sqrt == int(delta_den_sqrt) :
		print()
		print("<=>	" + var + "_1 = " + str_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den_sqrt, 0))
		return delta_neg_b_nota_sqrt_deltaden(var, num, den, str_b, delta, delta_num, delta_den_sqrt)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0))
	delta_num *= delta_den
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0))
	return delta_neg_b_nota_sqrt_deltaden(var, num, den, str_b, delta, delta_num, delta_den)

def	delta_neg_b_nota(var, b, delta, p) :
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + __utils__.ft_round(delta, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + __utils__.ft_round(delta, p))
	delta_sqrt = __utils__.ft_sqrt(delta)
	if delta_sqrt == int(delta_sqrt) :
		return delta_neg_b_nota_notsqrt(var, b, delta_sqrt, p)
	if b != int(b) :
		i1 = " - i√" + __utils__.ft_round(delta, p)
		i2 = " + i√" + __utils__.ft_round(delta, p)
		mult = __bonus__.irreducible_mult(b, 1, p)
		b_num = int(b * mult)
		b_den = int(mult)
		print()
		print("<=>	" + var + "_1 = " + __utils__.ft_round(b_num, 0) + " / " + __utils__.ft_round(b_den, 0) + i1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + __utils__.ft_round(b_num, 0) + " / " + __utils__.ft_round(b_den, 0) + i2)
		primes1 = __bonus__.primes(b_num)
		primes2 = __bonus__.primes(b_den)
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		num = __bonus__.print_frac(primes1, delete, True)
		den = __bonus__.print_frac(primes2, delete, False)
		if len(num) > 1 or len(den) > 1 :
			print()
			print("<=>	" + var + "_1 = " + num + " / " + den + i1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + num + " / " + den + i2)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			str_num = __bonus__.print_frac(primes1, None, True)
			str_den = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = " + str_num + " / " + str_den + i1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + " / " + str_den + i2)
			if len(primes1) > 1 or len(primes2) > 1 :
				num, den = __bonus__.irreducible(primes1, primes2)
				print()
				print("<=>	" + var + "_1 = " + __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + i1)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + __utils__.ft_round(num, 0) + " / " + __utils__.ft_round(den, 0) + i2)
			else :
				num = 1 if not primes1 else primes1[0]
				den = 1 if not primes2 else primes2[0]
		else :
			num = b_num
			den = b_den
	else :
		num = b
		den = 1
	return delta_neg_b_nota_sqrt(var, num, den, delta, p)

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

def	delta_neg_b_a_sqrt_aneg_notbint_iint(var, str_b, arround_b, delta_sqrt, a) :
	i = delta_sqrt / a
	str_i = __utils__.ft_round(i ,0) + "i"
	if str_i == "1i" :
		print()
		print("<=>	" + var + "_1 = " + str_b + " + " + str_i)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - " + str_i)
		str_i = "i"
	print()
	print("<=>	" + var + "_1 = " + str_b + " + " + str_i)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " - " + str_i)
	str1 = str_b + " + " + str_i
	str2 = str_b + " - " + str_i
	print("\033[35m")
	if len(arround_b[arround_b.find('.') + 1:]) < 14 :
		print("<=>	" + var + "_1 = " + arround_b + " + " + str_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + arround_b + " - " + str_i)
		str1 = arround_b + " + " + str_i
		str2 = arround_b + " - " + str_i
	else :
		print("<=>	" + var + "_1 ≈ " + arround_b + " + " + str_i)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + arround_b + " - " + str_i)
	return str2, str1

def	delta_neg_b_a_sqrt_aneg_notbint_inotint(var, str_b, arround_b, i, a, p) :
	mult = __bonus__.irreducible_mult(int(i), int(a), p)
	str_i = __utils__.ft_round(i, 0)
	str_a = __utils__.ft_round(a, 0)
	if mult > 1 or True:
		i = int(i * mult)
		a = int(a * mult)
		str_i = __utils__.ft_round(i, p)
		str_a = __utils__.ft_round(a, p)
		print()
		print("<=>	" + var + "_1 = " + str_b + " + " + str_i + "i / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - " + str_i + "i / " + str_a)
	primes1 = __bonus__.primes(i)
	primes2 = __bonus__.primes(a)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	if delete or True:
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
		i, a = __bonus__.irreducible(primes1, primes2)
		str_i = __utils__.ft_round(i, 0)
		str_a = __utils__.ft_round(a, 0)
		if len(primes1) > 1 or len(primes2) > 1 :
			print()
			print("<=>	" + var + "_1 = " + str_b + " + " + str_i + "i / " + str_a)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " - " + str_i + "i / " + str_a)
	if str_i == "1" :
		print()
		print("<=>	" + var + "_1 = " + str_b + " + " + str_i)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " - " + str_i)
		str_i = ""
	str_i += "i / " + str_a
	arround_i = __utils__.ft_round(i / a, p) + "i"
	equal_b = len(arround_b[arround_b.find('.') + 1:]) < 14
	equal_i = len(arround_i[arround_i.find('.') + 1:]) < 15
	print("\033[35m")
	if equal_b and equal_i :
		str1 = arround_b + " + " + arround_i
		str2 = arround_b + " - " + arround_i
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + str2)
	elif equal_b :
		str1 = arround_b + " + " + str_i
		str2 = arround_b + " - " + str_i
		print("<=>	" + var + "_1 ≈ " + str1)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + str2)
	elif equal_i :
		str1 = str_b + " + " + arround_i
		str2 = str_b + " - " + arround_i
		print("<=>	" + var + "_1 ≈ " + str1)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + str2)
	else :
		str1 = str_b + " + " + str_i
		str2 = str_b + " - " + str_i
		print("<=>	" + var + "_1 ≈ " + str1)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + str2)
	return str2, str1

def	delta_neg_b_a_sqrt_aneg_notbint(var, a, b, delta_sqrt, p) :
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
		print("<=>	" + var + "_1 = " + str_b + " / " + str_a1 + " + " + str_i)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " / " + str_a1 + " - " + str_i)
	primes1 = __bonus__.primes(b)
	primes2 = __bonus__.primes(a1)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	if delete :
		str_num = __bonus__.print_frac(primes1, delete, True)
		str_den = __bonus__.print_frac(primes2, delete, False)
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " + " + str_i)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den + " - " + str_i)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " + " + str_i)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den + " - " + str_i)
		b, a1 = __bonus__.irreducible(primes1, primes2)
		str_b = __utils__.ft_round(b, 0)
		str_a1 = __utils__.ft_round(a1, 0)
		if len(primes1) > 1 or len(primes2) > 1 :
			print()
			print("<=>	" + var + "_1 = " + str_b + " / " + str_a1 + " + " + str_i)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_b + " / " + str_a1 + " - " + str_i)
	str_b += " / " + str_a1
	tmp_i = delta_sqrt / a
	if tmp_i == int(tmp_i) :
		return delta_neg_b_a_sqrt_aneg_notbint_iint(var, str_b, __utils__.ft_round(b / a1, 15), delta_sqrt, a)
	return delta_neg_b_a_sqrt_aneg_notbint_inotint(var, str_b, __utils__.ft_round(b / a1, 15), delta_sqrt, a, p)
	print("TODO NOW") # Trouver dans quel cas on peut rentrer ici
	return "", ""

def	delta_neg_b_a_sqrt_aneg(var, a, b, delta_sqrt, p) :
	str_b = __utils__.ft_round(b, p)
	a *=  -1
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = -(" + str_b + " - " + __utils__.ft_round(delta_sqrt, p) + "i) / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = -(" + str_b + " + " + __utils__.ft_round(delta_sqrt, p) + "i) / " + str_a)
	b *= -1
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " + " + __utils__.ft_round(delta_sqrt, p) + "i) / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " - " + __utils__.ft_round(delta_sqrt, p) + "i) / " + str_a)
	print()
	print("<=>	" + var + "_1 = " + str_b + " / " + str_a + " + " + __utils__.ft_round(delta_sqrt, p) + "i / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " / " + str_a + " - " + __utils__.ft_round(delta_sqrt, p) + "i / " + str_a)
	tmp_b = b / a
	if tmp_b == int(tmp_b) :
		b = tmp_b
		return delta_neg_b_a_sqrt_aneg_bint(var, a, b, delta_sqrt, p)
	return delta_neg_b_a_sqrt_aneg_notbint(var, a, b, delta_sqrt, p)

def delta_neg_b_a_sqrt_apos(var, a, b, delta_sqrt, p) :
	print("TODO")
	return "", ""

def	delta_neg_b_a_sqrt(var, a, b, delta_sqrt, p) :
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - " + __utils__.ft_round(delta_sqrt, p) + "i) / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + " + __utils__.ft_round(delta_sqrt, p) + "i) / " + __utils__.ft_round(a, p))
	if a < 0 :
		return delta_neg_b_a_sqrt_aneg(var, a, b, delta_sqrt, p)
	return delta_neg_b_a_sqrt_apos(var, a, b, delta_sqrt, p)

def	delta_neg_b_a_notsqrt(var, a, b, delta, p) :
	print("TODO")
	return "", ""

def	delta_neg_b_a(var, a, b, delta, p) :
	delta_sqrt = __utils__.ft_sqrt(delta)
	if delta_sqrt == int(delta_sqrt) :
		return delta_neg_b_a_sqrt(var, a, b, delta_sqrt, p)
	return delta_neg_b_a_notsqrt(var, a, b, delta, p)

def	delta_neg_b(var, a, b, delta, p) :
	if a == 1 :
		return delta_neg_b_nota(var, b, delta, p)
	return delta_neg_b_a(var, a, b, delta, p)
