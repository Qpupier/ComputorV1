# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    nota.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/06 18:23:04 by qpupier           #+#    #+#              #
#    Updated: 2021/07/19 19:19:16 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	delta_neg_notb_nota_discriminant_squares(var, squares, delta_num, delta_den) :
	sq = __bonus__.print_squares(squares, delta_num)
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
	if str_num == "1" :
		str_num = ""
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
		str1 = __utils__.ft_round(-delta, 15) + "i"
		str2 = __utils__.ft_round(delta, 15) + "i"
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		return str1, str2
	return delta_neg_notb_nota_discriminant(var, delta)
