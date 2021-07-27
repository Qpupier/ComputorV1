# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    delta_den.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 20:42:10 by qpupier           #+#    #+#              #
#    Updated: 2021/07/27 16:28:17 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_notb_nota_notsqrt_notdelta_deltaden(var, delta_num, delta_den) :
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + " / " + str_den)
	squares, delta_num = __bonus__.reduce_sqrt(delta_num)
	str_num = __utils__.ft_round(delta_num, 0)
	if not squares :
		arround = __utils__.ft_round(__utils__.ft_sqrt(delta_num) / delta_den, 14)
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
			str1 = "-√" + str_num + " / " + str_den
			str2 = "√" + str_num + " / " + str_den
		return str1, str2
	sq = __bonus__.print_squares(squares, delta_num)
	print()
	print("<=>	" + var + "_1 = -√" + sq + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + sq + " / " + str_den)
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = -√(" + __utils__.ft_round(tmp, 0) + " * " + str_den + ") / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = √(" + __utils__.ft_round(tmp, 0) + " * " + str_den + ") / " + str_den)
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(tmp, 0) + "√" + str_num + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(tmp, 0) + "√" + str_num + " / " + str_den)
	squares = __utils__.ft_sqrt(tmp)
	print()
	print("<=>	" + var + "_1 = -" + __utils__.ft_round(squares, 0) + "√" + str_num + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + __utils__.ft_round(squares, 0) + "√" + str_num + " / " + str_den)
	tmp_den = squares / delta_den
	if tmp_den == int(tmp_den) :
		delta_den = tmp_den
		str_den = __utils__.ft_round(delta_den, 0)
		if str_den == "1" :
			str_den = ""
		print()
		print("<=>	" + var + "_1 = -" + str_den + "√" + str_num)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_den + "√" + str_num)
		arround = __utils__.ft_round(delta_den * __utils__.ft_sqrt(delta_num), 14)
		print("\033[35m")
		if len(arround[arround.find('.') + 1:]) < 15:
			print("<=>	" + var + "_1 = -" + arround)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + arround)
			str1 = "-" + arround
			str2 = arround
		else :
			print("<=>	" + var + "_1 ≈ -" + arround)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround)
			str1 = "-" + str_den + "√" + str_num
			str2 = str_den + "√" + str_num
		return str1, str2
	primes_square = __bonus__.primes(squares)
	primes_den = __bonus__.primes(delta_den)
	if len(primes_square) > 1 or len(primes_den) > 1 :
		num_d = squares
		den_d = delta_den
		delete = []
		__bonus__.reduce_fraction(primes_square, primes_den, delete)
		str_num = __bonus__.print_frac(primes_square, delete, True)
		str_den = __bonus__.print_frac(primes_den, delete, False)
		if delete :
			print()
			print("<=>	" + var + "_1 = -" + str_num + "√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + "√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			__bonus__.fraction_delete(primes_square, delete.copy())
			__bonus__.fraction_delete(primes_den, delete.copy())
			str_num = __bonus__.print_frac(primes_square, [], True)
			if str_num == "1" or str_num == "-1" :
				str_num = str_num[:-1]
			str_den = __bonus__.print_frac(primes_den, [], False)
			if not str_den :
				str_den = "1"
			print()
			print("<=>	" + var + "_1 = -" + str_num + "√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + "√" + __utils__.ft_round(delta_num, 0) + " / " + str_den)
			num_d, den_d = __bonus__.irreducible(primes_square, primes_den)
			str_num = __utils__.ft_round(num_d, 0) if num_d != 1 else ""
			str_den = " / " + __utils__.ft_round(den_d, 0)
			if len(primes_square) > 1 or len(primes_den) > 1 :
				print()
				print("<=>	" + var + "_1 = -" + str_num + "√" + __utils__.ft_round(delta_num, 0) + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_num + "√" + __utils__.ft_round(delta_num, 0) + str_den)
			if str_den == " / 1" :
				str_den = ""
				print()
				print("<=>	" + var + "_1 = -" + str_num + "√" + __utils__.ft_round(delta_num, 0) + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_num + "√" + __utils__.ft_round(delta_num, 0) + str_den)
	else :
		num_d = squares
		den_d = delta_den
	str_num_d = __utils__.ft_round(num_d, 0)
	str_den = " / " + __utils__.ft_round(den_d, 0)
	if str_den == " / 1" :
		str_den = ""
	arround = __utils__.ft_round(num_d * __utils__.ft_sqrt(delta_num) / den_d, 14)
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
		if num_d == 1 :
			str_num_d = ""
		elif num_d == -1 :
			str_num_d = "-"
		str1 = "-" + str_num_d + "√" + __utils__.ft_round(delta_num, 0) + str_den
		str2 = str_num_d + "√" + __utils__.ft_round(delta_num, 0) + str_den
	return str1, str2
