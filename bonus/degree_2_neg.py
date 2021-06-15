# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree_2_neg.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/14 16:04:15 by qpupier           #+#    #+#              #
#    Updated: 2021/06/15 20:47:23 by qpupier          ###   ########lyon.fr    #
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
	print("<=>	" + var + "_1 = -√" + sq + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + sq + " / " + __utils__.ft_round(delta_den, 0))
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = -√(" + __utils__.ft_round(tmp, 15) + " * " + __utils__.ft_round(delta_num, 15) + ") / " + __utils__.ft_round(delta_den, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = √(" + __utils__.ft_round(tmp, 15) + " * " + __utils__.ft_round(delta_num, 15) + ") / " + __utils__.ft_round(delta_den, 0))
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(tmp, 15) + "√" + __utils__.ft_round(delta_num, 15) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(tmp, 15) + "√" + __utils__.ft_round(delta_num, 15) + " / " + __utils__.ft_round(delta_den, 0))
	squares = __utils__.ft_sqrt(tmp)
	print()
	print("<=>	" + var + "_1 = -" + __utils__.ft_round(squares, 15) + "√" + __utils__.ft_round(delta_num, 15) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + __utils__.ft_round(squares, 15) + "√" + __utils__.ft_round(delta_num, 15) + " / " + __utils__.ft_round(delta_den, 0))
	primes_square = __bonus__.primes(squares)
	primes_den = __bonus__.primes(delta_den)
	delete = []
	__bonus__.reduce_fraction(primes_square, primes_den, delete)
	str_num = __bonus__.print_frac(primes_square, delete, True)
	str_den = __bonus__.print_frac(primes_den, delete, False)
	print()
	print("<=>	" + var + "_1 = -" + str_num + "√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + "√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
	__bonus__.fraction_delete(primes_square, delete.copy())
	__bonus__.fraction_delete(primes_den, delete.copy())
	str_num = __bonus__.print_frac(primes_square, [], True)
	str_den = __bonus__.print_frac(primes_den, [], False)
	if not str_den :
		str_den = "1"
	print()
	print("<=>	" + var + "_1 = -" + str_num + "√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + "√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
	num, den = __bonus__.irreducible(primes_square, primes_den)
	str_num = __utils__.ft_round(num, 15) if num != 1 else ""
	str_den = __utils__.ft_round(den, 15)
	if len(primes_square) > 1 or len(primes_den) > 1 :
		print()
		print("<=>	" + var + "_1 = -" + str_num + "√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + "√" + __utils__.ft_round(delta_num, 15) + " / " + str_den)
	if str_den == "1" :
		print()
		print("<=>	" + var + "_1 = -" + str_num + "√" + __utils__.ft_round(delta_num, 15))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + "√" + __utils__.ft_round(delta_num, 15))
		arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta_num), 15)
		arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta_num), 15)
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 11 :
			print("<=>	" + var + "_1 = " + arround1)
			str1 = arround1
		else :
			print("<=>	" + var + "_1 ≈ " + arround1)
			str1 = "-" + str_num + "√" + __utils__.ft_round(delta_num, 15)
		print("	\33[33mor\033[35m")
		if len(arround2[arround2.find('.') + 1:]) < 11 :
			print("	" + var + "_2 = " + arround2)
			str2 = arround2
		else :
			print("	" + var + "_2 ≈ " + arround2)
			str2 = str_num + "√" + __utils__.ft_round(delta_num, 15)
		return str1, str2
	arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta_num) / den, 15)
	arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta_num) / den, 15)
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 11 :
		print("<=>	" + var + "_1 = " + arround1)
		str1 = arround1
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
		str1 = "-" + str_num + "√" + __utils__.ft_round(delta_num, 15) + " / " + str_den
	print("	\33[33mor\033[35m")
	if len(arround2[arround2.find('.') + 1:]) < 11 :
		print("	" + var + "_2 = " + arround2)
		str2 = arround2
	else :
		print("	" + var + "_2 ≈ " + arround2)
		str2 = str_num + "√" + __utils__.ft_round(delta_num, 15) + " / " + str_den
	return str1, str2

def	delta_neg_notb_nota_discriminant(var, delta) :
	if delta == int(delta) :
		delta = __bonus__.reduce_sqrt(delta)
		print("TODO NOW")
		return
	mult = __bonus__.irreducible_mult(delta, 1)
	delta_num = int(delta * mult)
	delta_den = int(mult)
	print()
	print("<=>	" + var + "_1 = -√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ")")
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0))
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print()
	print("<=>	" + var + "_1 = -√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0))
	delta_num *= delta_den
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0))
	squares, delta_num = __bonus__.reduce_sqrt(delta_num)
	if squares :
		return delta_neg_notb_nota_discriminant_squares(var, squares, delta_num, delta_den)
	arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta_num) / delta_den, 15)
	arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta_num) / delta_den, 15)
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 11 :
		print("<=>	" + var + "_1 = " + arround1)
		str1 = arround1
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
		str1 = "-√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0)
	print("	\33[33mor\033[35m")
	if len(arround2[arround2.find('.') + 1:]) < 11 :
		print("	" + var + "_2 = " + arround2)
		str2 = arround2
	else :
		print("	" + var + "_2 ≈ " + arround2)
		str2 = "√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0)
	return str1, str2

def	delta_neg_notb_nota(var, delta) :
	if __utils__.ft_sqrt(delta) == int(__utils__.ft_sqrt(delta)) :
		delta = __utils__.ft_sqrt(delta)
		print()
		print("<=>	" + var + "_1 = -" + __utils__.ft_round(delta, 11))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + __utils__.ft_round(delta, 11))
		str1 = __utils__.ft_round(-delta, 15)
		str2 = __utils__.ft_round(delta, 15)
		return str1, str2
	return delta_neg_notb_nota_discriminant(var, delta)

def	delta_neg_notb(var, a, delta, p) :
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	if __utils__.ft_round(a, p) == "1" :
		print()
		print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta, p))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = √" + __utils__.ft_round(delta, p))
		return delta_neg_notb_nota(var, delta)
	print("TODO")
	# delta_neg_notb_a()

def	delta_neg(var, a, b, delta, p) :
	print()
	print("Discriminant is negative, there are 2 complex solutions :")
	print()
	print("\033[32m")
	print("Steps :")
	print()
	print("	" + var + "_1 = (-b - √-Δ) / 2a")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (-b + √-Δ) / 2a")
	if b < 0 :
		print()
		print("<=>	" + var + "_1 = (-(" + __utils__.ft_round(b, p) + ") - √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (-(" + __utils__.ft_round(b, p) + ") + √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
		b *= -1
		str_b = __utils__.ft_round(b, p)
	else :
		str_b = "-" + __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	if str_b == "-0" :
		str_b = "0"
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	delta *= -1
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	a *= 2
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + __utils__.ft_round(delta, p) + ") / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + __utils__.ft_round(delta, p) + ") / " + __utils__.ft_round(a, p))
	if b :
		# delta_neg_b()
		print("TO DO")
	else :
		result = delta_neg_notb(var, a, delta, p)
	print("\033[0m")
	return result
