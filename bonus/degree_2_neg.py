# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree_2_neg.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/14 16:04:11 by qpupier           #+#    #+#              #
#    Updated: 2021/06/26 17:36:16 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	print_squares(squares, delta) :
	sq = "("
	for each in squares :
		if sq != "(" :
			sq += " * "
		sq += __utils__.ft_round(each * each, 15)
	sq += " * " + __utils__.ft_round(delta, 15) + ")"
	return sq

def	delta_neg_notb_nota_discriminant_squares(var, squares, delta_num, delta_den) :
	sq = print_squares(squares, delta_num)
	print()
	print("<=>	" + var + "_1 = -i√" + sq + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + sq + " / " + __utils__.ft_round(delta_den, 0))
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = -i√(" + __utils__.ft_round(tmp, 15) + " * " + __utils__.ft_round(delta_num, 15) + ") / " + __utils__.ft_round(delta_den, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = i√(" + __utils__.ft_round(tmp, 15) + " * " + __utils__.ft_round(delta_num, 15) + ") / " + __utils__.ft_round(delta_den, 0))
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(tmp, 15) + "√" + __utils__.ft_round(delta_num, 15) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(tmp, 15) + "√" + __utils__.ft_round(delta_num, 15) + " / " + __utils__.ft_round(delta_den, 0))
	squares = __utils__.ft_sqrt(tmp)
	primes_square = __bonus__.primes(squares)
	primes_den = __bonus__.primes(delta_den)
	if len(primes_square) > 1 or len(primes_den) > 1 :
		print()
		print("<=>	" + var + "_1 = -" + __utils__.ft_round(squares, 15) + "i√" + __utils__.ft_round(delta_num, 15) + " / " + __utils__.ft_round(delta_den, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + __utils__.ft_round(squares, 15) + "i√" + __utils__.ft_round(delta_num, 15) + " / " + __utils__.ft_round(delta_den, 0))
	delete = []
	__bonus__.reduce_fraction(primes_square, primes_den, delete)
	str_num = __bonus__.print_frac(primes_square, delete, True)
	str_den = __bonus__.print_frac(primes_den, delete, False)
	print()
	print("<=>	" + var + "_1 = -" + str_num + "i√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + "i√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
	__bonus__.fraction_delete(primes_square, delete.copy())
	__bonus__.fraction_delete(primes_den, delete.copy())
	str_num = __bonus__.print_frac(primes_square, [], True)
	str_den = __bonus__.print_frac(primes_den, [], False)
	if not str_den :
		str_den = "1"
	print()
	print("<=>	" + var + "_1 = -" + str_num + "i√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + "i√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
	num, den = __bonus__.irreducible(primes_square, primes_den)
	str_num = __utils__.ft_round(num, 15) if num != 1 else ""
	str_den = __utils__.ft_round(den, 15)
	if len(primes_square) > 1 or len(primes_den) > 1 :
		print()
		print("<=>	" + var + "_1 = -" + str_num + "i√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + "i√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
	arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta_num) / den, 15) + "i"
	arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta_num) / den, 15) + "i"
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 9 :
		print("<=>	" + var + "_1 = " + arround1)
		str1 = arround1
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
		str1 = "-" + str_num + "i√" + __utils__.ft_round(delta_num, 15) + " / " + str_den
	print("	\33[33mor\033[35m")
	if len(arround2[arround2.find('.') + 1:]) < 9 :
		print("	" + var + "_2 = " + arround2)
		str2 = arround2
	else :
		print("	" + var + "_2 ≈ " + arround2)
		str2 = str_num + "i√" + __utils__.ft_round(delta_num, 15) + " / " + str_den
	return str1, str2

def	delta_neg_notb_nota_discriminant_int(var, delta) :
	sq, delta = __bonus__.reduce_sqrt(delta)
	if sq :
		result = __bonus__.str_lst_sq(sq, delta)
		print()
		print("<=>	" + var + "_1 = -i√" + result)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = i√" + result)
		if len(sq) > 1 :
			sq = __bonus__.irreducible_sq(sq)
			result = __bonus__.str_lst_sq(sq, delta)
			print()
			print("<=>	" + var + "_1 = -i√" + result)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = i√" + result)
		print()
		print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(sq[0] * sq[0], 0) + "√" + __utils__.ft_round(delta, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = i√" + __utils__.ft_round(sq[0] * sq[0], 0) + "√" + __utils__.ft_round(delta, 0))
		str1 = "-" + __utils__.ft_round(sq[0], 0) + "i√" + __utils__.ft_round(delta, 0)
		str2 = __utils__.ft_round(sq[0], 0) + "i√" + __utils__.ft_round(delta, 0)
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		arround1 = __utils__.ft_round(-sq[0] * __utils__.ft_sqrt(delta), 15) + "i"
		arround2 = __utils__.ft_round(sq[0] * __utils__.ft_sqrt(delta), 15) + "i"
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 9 :
			print("<=>	" + var + "_1 = " + arround1)
			str1 = arround1
		else :
			print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		if len(arround2[arround2.find('.') + 1:]) < 9 :
			print("	" + var + "_2 = " + arround2)
			str2 = arround2
		else :
			print("	" + var + "_2 ≈ " + arround2)
		return str1, str2
	str1 = "-i√" + __utils__.ft_round(delta, 0)
	str2 = "i√" + __utils__.ft_round(delta, 0)
	arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta), 15) + "i"
	arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta), 15) + "i"
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 9 :
		print("<=>	" + var + "_1 = " + arround1)
		str1 = arround1
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
	print("	\33[33mor\033[35m")
	if len(arround2[arround2.find('.') + 1:]) < 9 :
		print("	" + var + "_2 = " + arround2)
		str2 = arround2
	else :
		print("	" + var + "_2 ≈ " + arround2)
	return str1, str2

def	delta_neg_notb_nota_discriminant(var, delta) :
	if delta == int(delta) :
		return delta_neg_notb_nota_discriminant_int(var, delta)
	mult = __bonus__.irreducible_mult(delta, 1, 15)
	delta_num = int(delta * mult)
	delta_den = int(mult)
	print()
	print("<=>	" + var + "_1 = -i√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ")")
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0))
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print()
	print("<=>	" + var + "_1 = -i√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0))
	delta_num *= delta_den
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0))
	squares, delta_num = __bonus__.reduce_sqrt(delta_num)
	if squares :
		return delta_neg_notb_nota_discriminant_squares(var, squares, delta_num, delta_den)
	str1 = "-i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0)
	str2 = "i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0)
	arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta_num) / delta_den, 15) + "i"
	arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta_num) / delta_den, 15) + "i"
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 15 :
		print("<=>	" + var + "_1 = " + arround1)
		str1 = arround1
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
	print("	\33[33mor\033[35m")
	if len(arround2[arround2.find('.') + 1:]) < 15 :
		print("	" + var + "_2 = " + arround2)
		str2 = arround2
	else :
		print("	" + var + "_2 ≈ " + arround2)
	return str1, str2

def	delta_neg_notb_nota(var, delta) :
	if __utils__.ft_sqrt(delta) == int(__utils__.ft_sqrt(delta)) :
		delta = __utils__.ft_sqrt(delta)
		print()
		print("<=>	" + var + "_1 = -" + __utils__.ft_round(delta, 15))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + __utils__.ft_round(delta, 15))
		str1 = __utils__.ft_round(-delta, 15)
		str2 = __utils__.ft_round(delta, 15)
		return str1, str2
	return delta_neg_notb_nota_discriminant(var, delta)

def	delta_neg_notb_a_discriminant(var, a, delta, p) :
	if a == int(a) :
		a = int(a)
		p = 0
	delta = __utils__.ft_sqrt(delta)
	print()
	print("<=>	" + var + "_1 = -" + __utils__.ft_round(delta, 0) + "i / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + __utils__.ft_round(delta, 0) + "i / " + __utils__.ft_round(a, p))
	mult = __bonus__.irreducible_mult(delta, a, p)
	if mult > 1 :
		delta = int(delta * mult)
		a = int(a * mult)
		print()
		print("<=>	" + var + "_1 = -" + __utils__.ft_round(delta, 0) + "i / " + __utils__.ft_round(a, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + __utils__.ft_round(delta, 0) + "i / " + __utils__.ft_round(a, 0))
	primes1 = __bonus__.primes(delta)
	primes2 = __bonus__.primes(a)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	if delete :
		str_num = __bonus__.print_frac(primes1, delete, True)
		str_den = __bonus__.print_frac(primes2, delete, False)
		print()
		print("<=>	" + var + "_1 = -" + str_num + "i / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + "i / " + str_den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = -" + str_num + "i / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + "i / " + str_den)
		delta, a = __bonus__.irreducible(primes1, primes2)
		if len(primes1) > 1 or len(primes2) > 1 :
			str_delta = __utils__.ft_round(delta, 0)
			if str_delta == "1" :
				str_delta = ""
			print()
			print("<=>	" + var + "_1 = -" + str_delta + "i / " + __utils__.ft_round(a, 0))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_delta + "i / " + __utils__.ft_round(a, 0))
	if delta / a == int(delta / a) :
		delta = int(delta / a)
		if delta == -1 :
			str1 = "i"
			str2 = "-i"
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			return str1, str2
		if delta == 1 :
			str1 = "-i"
			str2 = "i"
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			return str1, str2
		str1 = "-" + __utils__.ft_round(delta, 0) + "i"
		str2 = __utils__.ft_round(delta, 0) + "i"
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		return str1, str2
	str_delta1 = __utils__.ft_round(-delta, 0)
	if str_delta1 == "-1" :
		str_delta1 = "-"
	if str_delta1 == "1" :
		str_delta1 = ""
	str_delta2 = __utils__.ft_round(delta, 0)
	if str_delta2 == "-1" :
		str_delta2 = "-"
	if str_delta2 == "1" :
		str_delta2 = ""
	str1 = str_delta1 + "i / " + __utils__.ft_round(a, 0)
	str2 = str_delta2 + "i / " + __utils__.ft_round(a, 0)
	if a < 0 :
		delta *= -1
		a *= -1
		str_delta1 = __utils__.ft_round(-delta, 0)
		if str_delta1 == "-1" :
			str_delta1 = "-"
		if str_delta1 == "1" :
			str_delta1 = ""
		str_delta2 = __utils__.ft_round(delta, 0)
		if str_delta2 == "-1" :
			str_delta2 = "-"
		if str_delta2 == "1" :
			str_delta2 = ""
		str1 = str_delta1 + "i / " + __utils__.ft_round(a, 0)
		str2 = str_delta2 + "i / " + __utils__.ft_round(a, 0)
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
	arround1 = __utils__.ft_round(-delta / a, 15) + "i"
	arround2 = __utils__.ft_round(delta / a, 15) + "i"
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 15 :
		print("<=>	" + var + "_1 = " + arround1)
		str1 = arround1
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
	print("	\33[33mor\033[35m")
	if len(arround2[arround2.find('.') + 1:]) < 15 :
		print("	" + var + "_2 = " + arround2)
		str2 = arround2
	else :
		print("	" + var + "_2 ≈ " + arround2)
	if delta < 0 :
		return str2, str1
	return str1, str2

def delta_neg_notb_a_discriminant_float(var, a, delta, p) :
	mult = __bonus__.irreducible_mult(delta, 1, p)
	delta_num = int(delta * mult)
	delta_den = int(mult)
	print()
	print("<=>	" + var + "_1 = -i√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(a, p))
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print()
	print("<=>	" + var + "_1 = -i√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	delta_num *= delta_den
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + " / (" + __utils__.ft_round(delta_den, 0) + " * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + " / (" + __utils__.ft_round(delta_den, 0) + " * " + __utils__.ft_round(a, p) + ")")
	delta = delta_num
	a *= delta_den
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, 0))
	sq, delta = __bonus__.reduce_sqrt(delta)
	if sq :
		result = __bonus__.str_lst_sq(sq, delta)
		print()
		print("<=>	" + var + "_1 = -i√" + result + " / " + __utils__.ft_round(a, p))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = i√" + result + " / " + __utils__.ft_round(a, p))
		if len(sq) > 1 :
			sq = __bonus__.irreducible_sq(sq)
			result = __bonus__.str_lst_sq(sq, delta)
			print()
			print("<=>	" + var + "_1 = -i√" + result + " / " + __utils__.ft_round(a, p))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = i√" + result + " / " + __utils__.ft_round(a, p))
		print()
		print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(sq[0] * sq[0], 0) + "√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = i√" + __utils__.ft_round(sq[0] * sq[0], 0) + "√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
		primes1 = __bonus__.primes(sq[0])
		primes2 = __bonus__.primes(a)
		if len(primes1) > 1 or len(primes2) > 1 :
			print()
			print("<=>	" + var + "_1 = -" + __utils__.ft_round(sq[0], 0) + "i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + __utils__.ft_round(sq[0], 0) + "i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		num = __bonus__.print_frac(primes1, delete, True)
		den = __bonus__.print_frac(primes2, delete, False)
		print()
		print("<=>	" + var + "_1 = -" + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		num = __bonus__.print_frac(primes1, None, True)
		den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = -" + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
		num, den = __bonus__.irreducible(primes1, primes2)
		str_num = "" if num == 1 else __utils__.ft_round(num, 15)
		str_den = __utils__.ft_round(den, 15)
		if str_num or den < 0 :
			print()
			print("<=>	" + var + "_1 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
		if den == -1 :
			den *= -1
			str_den = __utils__.ft_round(den, 15)
			print()
			print("<=>	" + var + "_1 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			str1 = str_num + "i√" + __utils__.ft_round(delta, 0)
			str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(num * __utils__.ft_sqrt(delta), 15) + "i"
			arround2 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta), 15) + "i"
			print("\033[35m")
			if len(arround1[arround1.find('.') + 1:]) < 15 :
				print("<=>	" + var + "_1 = " + arround1)
				str1 = arround1
			else :
				print("<=>	" + var + "_1 ≈ " + arround1)
			print("	\33[33mor\033[35m")
			if len(arround2[arround2.find('.') + 1:]) < 15 :
				print("	" + var + "_2 = " + arround2)
				str2 = arround2
			else :
				print("	" + var + "_2 ≈ " + arround2)
			return str2, str1
		if den == 1 :
			str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
			str2 = str_num + "i√" + __utils__.ft_round(delta, 0)
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta), 15) + "i"
			arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta), 15) + "i"
			print("\033[35m")
			if len(arround1[arround1.find('.') + 1:]) < 15 :
				print("<=>	" + var + "_1 = " + arround1)
				str1 = arround1
			else :
				print("<=>	" + var + "_1 ≈ " + arround1)
			print("	\33[33mor\033[35m")
			if len(arround2[arround2.find('.') + 1:]) < 15 :
				print("	" + var + "_2 = " + arround2)
				str2 = arround2
			else :
				print("	" + var + "_2 ≈ " + arround2)
			return str1, str2
		if den < 0 :
			str_den = __utils__.ft_round(-den, 15)
			str1 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(num * __utils__.ft_sqrt(delta) / -den, 15) + "i"
			arround2 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta) / -den, 15) + "i"
		else :
			str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			str2 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta) / den, 15) + "i"
			arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta) / den, 15) + "i"
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 15 :
			print("<=>	" + var + "_1 = " + arround1)
			str1 = arround1
		else :
			print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		if len(arround2[arround2.find('.') + 1:]) < 15 :
			print("	" + var + "_2 = " + arround2)
			str2 = arround2
		else :
			print("	" + var + "_2 ≈ " + arround2)
		if den < 0 :
			return str2, str1
		return str1, str2
	str_num = ""
	str_den = __utils__.ft_round(a, 15)
	if a == -1 :
		a *= -1
		str_den = __utils__.ft_round(a, 15)
		print()
		print("<=>	" + var + "_1 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
		str1 = str_num + "i√" + __utils__.ft_round(delta, 0)
		str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		arround1 = __utils__.ft_round(__utils__.ft_sqrt(delta), 15) + "i"
		arround2 = __utils__.ft_round(-__utils__.ft_sqrt(delta), 15) + "i"
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 15 :
			print("<=>	" + var + "_1 = " + arround1)
			str1 = arround1
		else :
			print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		if len(arround2[arround2.find('.') + 1:]) < 15 :
			print("	" + var + "_2 = " + arround2)
			str2 = arround2
		else :
			print("	" + var + "_2 ≈ " + arround2)
		return str2, str1
	if a == 1 :
		str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
		str2 = str_num + "i√" + __utils__.ft_round(delta, 0)
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta), 15) + "i"
		arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta), 15) + "i"
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 15 :
			print("<=>	" + var + "_1 = " + arround1)
			str1 = arround1
		else :
			print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		if len(arround2[arround2.find('.') + 1:]) < 15 :
			print("	" + var + "_2 = " + arround2)
			str2 = arround2
		else :
			print("	" + var + "_2 ≈ " + arround2)
		return str1, str2
	if a < 0 :
		str_den = __utils__.ft_round(-a, 15)
		str1 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
		str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		arround1 = __utils__.ft_round(__utils__.ft_sqrt(delta) / -a, 15) + "i"
		arround2 = __utils__.ft_round(-__utils__.ft_sqrt(delta) / -a, 15) + "i"
	else :
		str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
		str2 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
		arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta) / a, 15) + "i"
		arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta) / a, 15) + "i"
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 15 :
		print("<=>	" + var + "_1 = " + arround1)
		str1 = arround1
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
	print("	\33[33mor\033[35m")
	if len(arround2[arround2.find('.') + 1:]) < 15 :
		print("	" + var + "_2 = " + arround2)
		str2 = arround2
	else :
		print("	" + var + "_2 ≈ " + arround2)
	if a < 0 :
		return str2, str1
	return str1, str2

def	delta_neg_notb_a(var, a, delta, p) :
	if __utils__.ft_sqrt(delta) == int(__utils__.ft_sqrt(delta)) :
		return delta_neg_notb_a_discriminant(var, a, delta, p)
	if delta == int(delta) :
		sq, delta = __bonus__.reduce_sqrt(delta)
		if sq :
			result = __bonus__.str_lst_sq(sq, delta)
			print()
			print("<=>	" + var + "_1 = -i√" + result + " / " + __utils__.ft_round(a, p))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = i√" + result + " / " + __utils__.ft_round(a, p))
			if len(sq) > 1 :
				sq = __bonus__.irreducible_sq(sq)
				result = __bonus__.str_lst_sq(sq, delta)
				print()
				print("<=>	" + var + "_1 = -i√" + result + " / " + __utils__.ft_round(a, p))
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = i√" + result + " / " + __utils__.ft_round(a, p))
			print()
			print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(sq[0] * sq[0], 0) + "√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = i√" + __utils__.ft_round(sq[0] * sq[0], 0) + "√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
			primes1 = __bonus__.primes(sq[0])
			primes2 = __bonus__.primes(a)
			if len(primes1) > 1 or len(primes2) > 1 :
				print()
				print("<=>	" + var + "_1 = -" + __utils__.ft_round(sq[0], 0) + "i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + __utils__.ft_round(sq[0], 0) + "i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
			delete = []
			__bonus__.reduce_fraction(primes1, primes2, delete)
			num = __bonus__.print_frac(primes1, delete, True)
			den = __bonus__.print_frac(primes2, delete, False)
			print()
			print("<=>	" + var + "_1 = -" + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			num = __bonus__.print_frac(primes1, None, True)
			den = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = -" + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
			num, den = __bonus__.irreducible(primes1, primes2)
			str_num = "" if num == 1 else __utils__.ft_round(num, 15)
			str_den = __utils__.ft_round(den, 15)
			if str_num or den < 0 :
				print()
				print("<=>	" + var + "_1 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			if den == -1 :
				den *= -1
				str_den = __utils__.ft_round(den, 15)
				print()
				print("<=>	" + var + "_1 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
				str1 = str_num + "i√" + __utils__.ft_round(delta, 0)
				str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
				print()
				print("<=>	" + var + "_1 = " + str1)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str2)
				arround1 = __utils__.ft_round(num * __utils__.ft_sqrt(delta), 15) + "i"
				arround2 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta), 15) + "i"
				print("\033[35m")
				if len(arround1[arround1.find('.') + 1:]) < 15 :
					print("<=>	" + var + "_1 = " + arround1)
					str1 = arround1
				else :
					print("<=>	" + var + "_1 ≈ " + arround1)
				print("	\33[33mor\033[35m")
				if len(arround2[arround2.find('.') + 1:]) < 15 :
					print("	" + var + "_2 = " + arround2)
					str2 = arround2
				else :
					print("	" + var + "_2 ≈ " + arround2)
				return str2, str1
			if den == 1 :
				str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
				str2 = str_num + "i√" + __utils__.ft_round(delta, 0)
				print()
				print("<=>	" + var + "_1 = " + str1)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str2)
				arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta), 15) + "i"
				arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta), 15) + "i"
				print("\033[35m")
				if len(arround1[arround1.find('.') + 1:]) < 15 :
					print("<=>	" + var + "_1 = " + arround1)
					str1 = arround1
				else :
					print("<=>	" + var + "_1 ≈ " + arround1)
				print("	\33[33mor\033[35m")
				if len(arround2[arround2.find('.') + 1:]) < 15 :
					print("	" + var + "_2 = " + arround2)
					str2 = arround2
				else :
					print("	" + var + "_2 ≈ " + arround2)
				return str1, str2
			if den < 0 :
				den *= -1
				str_den = __utils__.ft_round(den, 15)
				str1 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
				str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
				print()
				print("<=>	" + var + "_1 = " + str1)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str2)
				arround1 = __utils__.ft_round(num * __utils__.ft_sqrt(delta) / den, 15) + "i"
				arround2 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta) / den, 15) + "i"
			else :
				str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
				str2 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
				arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta) / den, 15) + "i"
				arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta) / den, 15) + "i"
			print("\033[35m")
			if len(arround1[arround1.find('.') + 1:]) < 15 :
				print("<=>	" + var + "_1 = " + arround1)
				str1 = arround1
			else :
				print("<=>	" + var + "_1 ≈ " + arround1)
			print("	\33[33mor\033[35m")
			if len(arround2[arround2.find('.') + 1:]) < 15 :
				print("	" + var + "_2 = " + arround2)
				str2 = arround2
			else :
				print("	" + var + "_2 ≈ " + arround2)
			if den < 0 :
				return str2, str1
			return str1, str2
		str_num = ""
		str_den = __utils__.ft_round(a, 15)
		if a == -1 :
			a *= -1
			str_den = __utils__.ft_round(a, 15)
			print()
			print("<=>	" + var + "_1 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			str1 = str_num + "i√" + __utils__.ft_round(delta, 0)
			str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(__utils__.ft_sqrt(delta), 15) + "i"
			arround2 = __utils__.ft_round(-__utils__.ft_sqrt(delta), 15) + "i"
			print("\033[35m")
			if len(arround1[arround1.find('.') + 1:]) < 15 :
				print("<=>	" + var + "_1 = " + arround1)
				str1 = arround1
			else :
				print("<=>	" + var + "_1 ≈ " + arround1)
			print("	\33[33mor\033[35m")
			if len(arround2[arround2.find('.') + 1:]) < 15 :
				print("	" + var + "_2 = " + arround2)
				str2 = arround2
			else :
				print("	" + var + "_2 ≈ " + arround2)
			return str2, str1
		if a == 1 :
			str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
			str2 = str_num + "i√" + __utils__.ft_round(delta, 0)
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta), 15) + "i"
			arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta), 15) + "i"
			print("\033[35m")
			if len(arround1[arround1.find('.') + 1:]) < 15 :
				print("<=>	" + var + "_1 = " + arround1)
				str1 = arround1
			else :
				print("<=>	" + var + "_1 ≈ " + arround1)
			print("	\33[33mor\033[35m")
			if len(arround2[arround2.find('.') + 1:]) < 15 :
				print("	" + var + "_2 = " + arround2)
				str2 = arround2
			else :
				print("	" + var + "_2 ≈ " + arround2)
			return str1, str2
		if a < 0 :
			str_den = __utils__.ft_round(-a, 15)
			str1 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(__utils__.ft_sqrt(delta) / -a, 15) + "i"
			arround2 = __utils__.ft_round(-__utils__.ft_sqrt(delta) / -a, 15) + "i"
		else :
			str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			str2 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta) / a, 15) + "i"
			arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta) / a, 15) + "i"
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 15 :
			print("<=>	" + var + "_1 = " + arround1)
			str1 = arround1
		else :
			print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		if len(arround2[arround2.find('.') + 1:]) < 15 :
			print("	" + var + "_2 = " + arround2)
			str2 = arround2
		else :
			print("	" + var + "_2 ≈ " + arround2)
		if a < 0 :
			return str2, str1
		return str1, str2
	return delta_neg_notb_a_discriminant_float(var, a, delta, p)

def	delta_neg_notb(var, a, delta, p) :
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	if __utils__.ft_round(a, p) == "1" :
		print()
		print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta, p))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = i√" + __utils__.ft_round(delta, p))
		return delta_neg_notb_nota(var, delta)
	return delta_neg_notb_a(var, a, delta, p)

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
	arround = __utils__.ft_round(num / den, 15)
	print("\033[35m")
	if len(arround[arround.find('.') + 1:]) < 15 :
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
	arround = __utils__.ft_round(num / den, 15)
	print("\033[35m")
	if len(arround[arround.find('.') + 1:]) < 15 :
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

def	delta_neg_b_nota(var, b, delta, p) :
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - i√" + __utils__.ft_round(delta, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + i√" + __utils__.ft_round(delta, p))
	delta_sqrt = __utils__.ft_sqrt(delta)
	if delta_sqrt == int(delta_sqrt) :
		return delta_neg_b_nota_notsqrt(var, b, delta_sqrt, p)
	print("TODO")
	return "", ""

def	delta_neg_b(var, a, b, delta, p) :
	if a == 1 :
		return delta_neg_b_nota(var, b, delta, p)
	print("TODO")
	return "", ""

def	delta_neg(var, a, b, delta, p) :
	print()
	print("Discriminant is negative, there are 2 complex solutions :")
	print()
	print("\033[32m")
	print("Steps :")
	print()
	print("	" + var + "_1 = (-b - i√-Δ) / 2a")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (-b + i√-Δ) / 2a")
	if b < 0 :
		print()
		print("<=>	" + var + "_1 = (-(" + __utils__.ft_round(b, p) + ") - i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (-(" + __utils__.ft_round(b, p) + ") + i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	b *= -1
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	if str_b == "-0" :
		str_b = "0"
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	delta *= -1
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - i√" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + i√" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	a *= 2
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - i√" + __utils__.ft_round(delta, p) + ") / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + i√" + __utils__.ft_round(delta, p) + ") / " + __utils__.ft_round(a, p))
	if b :
		result = delta_neg_b(var, a, b, delta, p)
	else :
		result = delta_neg_notb(var, a, delta, p)
	print("\033[0m")
	return result
