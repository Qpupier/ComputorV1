# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 19:27:48 by qpupier           #+#    #+#              #
#    Updated: 2021/07/29 18:36:23 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_notb_nota_notsqrt_notdelta_notdeltaden_notsquares(var, delta_num, a, p) :
	if a == int(a) :
		str_a = " / " + __utils__.ft_round(a, 0)
		if str_a == " / 1" :
			str_a = ""
		arround = __utils__.ft_round(__utils__.ft_sqrt(delta_num) / a, 14)
		print("\033[35m")
		if len(arround[arround.find('.') + 1:]) < 14 :
			print("<=>	" + var + "_1 = -" + arround)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + arround)
			str1 = "-" + arround
			str2 = arround
		else :
			print("<=>	" + var + "_1 ≈ -" + arround)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround)
			str1 = "-√" + __utils__.ft_round(delta_num, 0) + str_a
			str2 = "√" + __utils__.ft_round(delta_num, 0) + str_a
		return str1, str2
	delta = delta_num
	mult = __bonus__.irreducible_mult(1, a, p)
	delta_num = int(__utils__.ft_round(mult, 0))
	delta_den = int(__utils__.ft_round(a * mult, 0))
	str_delta = __utils__.ft_round(delta, 0)
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = -" + str_num + "√" + str_delta + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + "√" + str_delta + " / " + str_den)
	primes1 = __bonus__.primes(delta_num)
	primes2 = __bonus__.primes(delta_den)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	num = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(num) > 1 or len(den) > 1 :
		print()
		print("<=>	" + var + "_1 = -" + num + "√" + str_delta + " / " + den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + "√" + str_delta + " / " + den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = -" + str_num + "√" + str_delta + " / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + "√" + str_delta + " / " + str_den)
		if len(primes1) > 1 or len(primes2) > 1 :
			num, den = __bonus__.irreducible(primes1, primes2)
			str_num = __utils__.ft_round(num, 0)
			str_den = __utils__.ft_round(den, 0)
			print()
			print("<=>	" + var + "_1 = -" + str_num + "√" + str_delta + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + "√" + str_delta + " / " + str_den)
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
	else :
		num = delta_num
		den = delta_den
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	arround = __utils__.ft_round(num / den * __utils__.ft_sqrt(delta), 14)
	print("\033[35m")
	if len(arround[arround.find('.') + 1:]) < 14 :
		print("<=>	" + var + "_1 = -" + arround)
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 = " + arround)
		str1 = "-" + arround
		str2 = arround
	else :
		print("<=>	" + var + "_1 ≈ -" + arround)
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 ≈ " + arround)
		str1 = "-" + str_num + "√" + str_delta + " / " + str_den
		str2 = str_num + "√" + str_delta + " / " + str_den
	return str1, str2

def	delta_pos_notb_nota_notsqrt_notdelta_notdeltaden_squares(var, delta_num, squares, a, p) :
	str_delta = __utils__.ft_round(delta_num, 0)
	str_a = __utils__.ft_round(a, p)
	sq = __bonus__.print_squares(squares, delta_num)
	print()
	print("<=>	" + var + "_1 = -√" + sq + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + sq + " / " + str_a)
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = -√(" + __utils__.ft_round(tmp, 0) + " * " + str_delta + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = √(" + __utils__.ft_round(tmp, 0) + " * " + str_delta + ") / " + str_a)
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(tmp, 0) + "√" + str_delta + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(tmp, 0) + "√" + str_delta + " / " + str_a)
	squares = __utils__.ft_sqrt(tmp)
	print()
	print("<=>	" + var + "_1 = -" + __utils__.ft_round(squares, 0) + "√" + str_delta + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + __utils__.ft_round(squares, 0) + "√" + str_delta + " / " + str_a)
	tmp_a = squares / a
	if tmp_a == int(tmp_a) :
		a = tmp_a
		str_a = __utils__.ft_round(a, 0)
		if str_a == "1" :
			str_a = ""
		print()
		print("<=>	" + var + "_1 = -" + str_a + "√" + str_delta)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_a + "√" + str_delta)
		arround = __utils__.ft_round(a * __utils__.ft_sqrt(delta_num), 14)
		print("\033[35m")
		if len(arround[arround.find('.') + 1:]) < 14 :
			print("<=>	" + var + "_1 = -" + arround)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + arround)
			str1 = "-" + arround
			str2 = arround
		else :
			print("<=>	" + var + "_1 ≈ -" + arround)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround)
			str1 = "-" + str_a + "√" + str_delta
			str2 = str_a + "√" + str_delta
		return str1, str2
	delta = delta_num
	mult = __bonus__.irreducible_mult(squares, a, p)
	delta_num = int(__utils__.ft_round(squares * mult, 0))
	delta_den = int(__utils__.ft_round(a * mult, 0))
	str_delta = __utils__.ft_round(delta, 0)
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = -" + str_num + "√" + str_delta + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + "√" + str_delta + " / " + str_den)
	primes_square = __bonus__.primes(delta_num)
	primes_den = __bonus__.primes(delta_den)
	if len(primes_square) > 1 or len(primes_den) > 1 :
		num_d = squares
		den_d = a
		delete = []
		__bonus__.reduce_fraction(primes_square, primes_den, delete)
		str_num = __bonus__.print_frac(primes_square, delete, True)
		str_den = __bonus__.print_frac(primes_den, delete, False)
		if delete :
			print()
			print("<=>	" + var + "_1 = -" + str_num + "√" + str_delta + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + "√" + str_delta + " / " + str_den)
			__bonus__.fraction_delete(primes_square, delete.copy())
			__bonus__.fraction_delete(primes_den, delete.copy())
			str_num = __bonus__.print_frac(primes_square, [], True)
			if str_num == "1" or str_num == "-1" :
				str_num = str_num[:-1]
			str_den = __bonus__.print_frac(primes_den, [], False)
			if not str_den :
				str_den = "1"
			print()
			print("<=>	" + var + "_1 = -" + str_num + "√" + str_delta + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + "√" + str_delta + " / " + str_den)
			num_d, den_d = __bonus__.irreducible(primes_square, primes_den)
			str_num = __utils__.ft_round(num_d, 0) if num_d != 1 else ""
			str_den = " / " + __utils__.ft_round(den_d, 0)
			if len(primes_square) > 1 or len(primes_den) > 1 :
				print()
				print("<=>	" + var + "_1 = -" + str_num + "√" + str_delta + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_num + "√" + str_delta + str_den)
			if str_den == " / 1" :
				str_den = ""
				print()
				print("<=>	" + var + "_1 = -" + str_num + "√" + str_delta + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_num + "√" + str_delta + str_den)
	else :
		num_d = squares
		den_d = delta_den
	str_num_d = __utils__.ft_round(num_d, 0)
	str_den = " / " + __utils__.ft_round(den_d, 0)
	if str_den == " / 1" :
		str_den = ""
	arround = __utils__.ft_round(num_d * __utils__.ft_sqrt(delta) / den_d, 14)
	print("\033[35m")
	if len(arround[arround.find('.') + 1:]) < 12 :
		print("<=>	" + var + "_1 = -" + arround)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 = " + arround)
		str1 = "-" + arround
		str2 = arround
	else :
		print("<=>	" + var + "_1 ≈ -" + arround)
		print("	\33[33mor\033[35m")
		print("<=>	" + var + "_2 ≈ " + arround)
		if num_d == 1 :
			str_num_d = ""
		elif num_d == -1 :
			str_num_d = "-"
		str1 = "-" + str_num_d + "√" + str_delta + str_den
		str2 = str_num_d + "√" + str_delta + str_den
	return str1, str2

def	delta_pos_notb_nota_notsqrt_notdelta_deltaden(var, delta_num, delta_den_sqrt, a, p) :
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den_sqrt, 0)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + " / " + str_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + " / " + str_den + " / " + str_a)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + " / (" + str_den + " * " + str_a + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + " / (" + str_den + " * " + str_a + ")")
	a *= delta_den_sqrt
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + " / " + str_a)
	squares, delta_num = __bonus__.reduce_sqrt(delta_num)
	str_num = __utils__.ft_round(delta_num, 0)
	if not squares :
		return delta_pos_notb_nota_notsqrt_notdelta_notdeltaden_notsquares(var, delta_num, a, p)
	return delta_pos_notb_nota_notsqrt_notdelta_notdeltaden_squares(var, delta_num, squares, a, p)

def	delta_pos_notb_nota_notsqrt_notdelta_notdeltaden(var, delta_num, delta_den, a, p) :
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + "√" + str_den + " / " + str_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + "√" + str_den + " / " + str_den + " / " + str_a)
	print()
	print("<=>	" + var + "_1 = -√(" + str_num + " * " + str_den + ") / " + str_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √(" + str_num + " * " + str_den + ") / " + str_den + " / " + str_a)
	delta_num *= delta_den
	str_num = __utils__.ft_round(delta_num, 0)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + " / " + str_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + " / " + str_den + " / " + str_a)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + " / (" + str_den + " * " + str_a + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + " / (" + str_den + " * " + str_a + ")")
	a *= delta_den
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + " / " + str_a)
	squares, delta_num = __bonus__.reduce_sqrt(delta_num)
	str_num = __utils__.ft_round(delta_num, 0)
	if not squares :
		return delta_pos_notb_nota_notsqrt_notdelta_notdeltaden_notsquares(var, delta_num, a, p)
	return delta_pos_notb_nota_notsqrt_notdelta_notdeltaden_squares(var, delta_num, squares, a, p)

def	delta_pos_notb_a_notsqrt_notdelta(var, delta, a, p) :
	mult = __bonus__.irreducible_mult(delta, 1, p)
	delta_num = int(__utils__.ft_round(delta * mult, 0))
	delta_den = int(__utils__.ft_round(mult, 0))
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = -√(" + str_num + " / " + str_den + ")" + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √(" + str_num + " / " + str_den + ")" + " / " + str_a)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + " / √" + str_den + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + " / √" + str_den + " / " + str_a)
	delta_den_sqrt = __utils__.ft_sqrt(delta_den)
	if delta_den_sqrt == int(delta_den_sqrt) :
		return delta_pos_notb_nota_notsqrt_notdelta_deltaden(var, delta_num, delta_den_sqrt, a, p)
	return delta_pos_notb_nota_notsqrt_notdelta_notdeltaden(var, delta_num, delta_den, a, p)

def	delta_pos_notb_a_notsqrt_delta(var, delta, a, p) :
	squares, delta_num = __bonus__.reduce_sqrt(delta)
	if not squares :
		return delta_pos_notb_nota_notsqrt_notdelta_notdeltaden_notsquares(var, delta_num, a, p)
	return delta_pos_notb_nota_notsqrt_notdelta_notdeltaden_squares(var, delta_num, squares, a, p)

def	delta_pos_notb_a_notsqrt(var, delta, a, p) :
	if delta == int(delta) :
		return delta_pos_notb_a_notsqrt_delta(var, delta, a, p)
	return delta_pos_notb_a_notsqrt_notdelta(var, delta, a, p)

def	delta_pos_notb_a_sqrt(var, delta, a, p) :
	print()
	print("<=>	" + var + "_1 = -" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
	tmp = delta / a
	if tmp == int(tmp) :
		str1 = "-" + __utils__.ft_round(tmp, 0)
		str2 = __utils__.ft_round(tmp, 0)
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		return str1, str2
	mult = __bonus__.irreducible_mult(delta, a, p)
	delta_num = int(__utils__.ft_round(delta * mult, 0))
	delta_den = int(__utils__.ft_round(a * mult, 0))
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = -" + str_num + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + " / " + str_den)
	primes1 = __bonus__.primes(delta_num)
	primes2 = __bonus__.primes(delta_den)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	num = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(num) > 1 or len(den) > 1 :
		print()
		print("<=>	" + var + "_1 = -" + num + " / " + den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + " / " + den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = -" + str_num + " / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den)
		if len(primes1) > 1 or len(primes2) > 1 :
			num, den = __bonus__.irreducible(primes1, primes2)
			str_num = __utils__.ft_round(num, 0)
			str_den = __utils__.ft_round(den, 0)
			print()
			print("<=>	" + var + "_1 = -" + str_num + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + " / " + str_den)
		else :
			num = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
	else :
		num = delta_num
		den = delta_den
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	arround = __utils__.ft_round(num / den * __utils__.ft_sqrt(delta), 14)
	print("\033[35m")
	if len(arround[arround.find('.') + 1:]) < 14 :
		print("<=>	" + var + "_1 = -" + arround)
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 = " + arround)
		str1 = "-" + arround
		str2 = arround
	else :
		print("<=>	" + var + "_1 ≈ -" + arround)
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 ≈ " + arround)
		str1 = "-" + str_num + " / " + str_den
		str2 = str_num + " / " + str_den
	return str1, str2

def	delta_pos_notb_a(var, a, delta, p) :
	sqrt_delta = __utils__.ft_sqrt(delta)
	if sqrt_delta == int(sqrt_delta) :
		return delta_pos_notb_a_sqrt(var, sqrt_delta, a, p)
	return delta_pos_notb_a_notsqrt(var, delta, a, p)
