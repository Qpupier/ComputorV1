# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    den.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/21 16:11:33 by qpupier           #+#    #+#              #
#    Updated: 2021/08/21 17:06:30 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_b_nota_notsqrt_notdelta_delta_den_squares_den(var, num, squares, delta_num, den) :
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	str_squares = __utils__.ft_round(squares, 0)
	str_delta = __utils__.ft_round(delta_num, 0)
	print()
	print("<=>	" + var + "_1 = (" + str_num + " - " + str_squares + "√" + str_delta + ") / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_num + " + " + str_squares + "√" + str_delta + ") / " + str_den)
	primes1 = __bonus__.primes(num)
	primes2 = __bonus__.primes(squares)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	str_num = __bonus__.print_fact(primes1, delete, False)
	str_squares = __bonus__.print_fact(primes2, delete, False)
	str_delta = "√" + __utils__.ft_round(delta_num, 0)
	if delete :
		print()
		print("<=>	" + var + "_1 = (" + str_num + " - " + str_squares + str_delta + ") / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_num + " + " + str_squares + str_delta + ") / " + str_den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		fact, fact = __bonus__.irreducible(None, delete)
		str_fact = "\033[37m" + __utils__.ft_round(fact, 0) + "\033[32m"
		num, squares = __bonus__.irreducible(primes1, primes2)
		if len(delete) > 1 or len(primes1) > 1 or len(primes2) > 1 :
			str_num = " * " + __utils__.ft_round(num, 0)
			str_squares = " * " + __utils__.ft_round(squares, 0)
			if str_squares == " * 1" :
				str_squares = ""
			str1 = "(" + str_fact + str_num + " - " + str_fact + str_squares + str_delta + ") / " + str_den
			str2 = "(" + str_fact + str_num + " + " + str_fact + str_squares + str_delta + ") / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
		str_num = __utils__.ft_round(num, 0)
		str_squares = __utils__.ft_round(squares, 0)
		if str_squares == "1" :
			str_squares = ""
		str1 = str_fact + "(" + str_num + " - " + str_squares + str_delta + ") / " + str_den
		str2 = str_fact + "(" + str_num + " + " + str_squares + str_delta + ") / " + str_den
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
	else :
		fact = 1
		str_num = __utils__.ft_round(num, 0)
		str_squares = __utils__.ft_round(squares, 0)
		if str_squares == "1" :
			str_squares = ""
		str1 = "(" + str_num + " - " + str_squares + str_delta + ") / " + str_den
		str2 = "(" + str_num + " + " + str_squares + str_delta + ") / " + str_den
		arround1 = __utils__.ft_round((num - squares * __utils__.ft_sqrt(delta_num)) / den, 14)
		arround2 = __utils__.ft_round((num + squares * __utils__.ft_sqrt(delta_num)) / den, 14)
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
	primes1 = __bonus__.primes(fact)
	primes2 = __bonus__.primes(den)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	old_fact = fact
	old_den = den
	fact = __bonus__.print_frac(primes1, delete, True)
	den = __bonus__.print_frac(primes2, delete, False)
	if len(fact) > 1 or len(den) > 1 :
		print()
		print("<=>	" + var + "_1 = " + fact + "(" + str_num + " - " + str_squares + str_delta + ") / " + den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + fact + "(" + str_num + " + " + str_squares + str_delta + ") / " + den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_fact = __bonus__.print_frac(primes1, None, True)
		if str_fact == "1" :
			str_fact = ""
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_squares + str_delta + ") / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_squares + str_delta + ") / " + str_den)
		if len(primes1) > 1 or len(primes2) > 1 :
			fact, den = __bonus__.irreducible(primes1, primes2)
			str_fact = __bonus__.print_frac(primes1, None, True)
			if str_fact == "1" :
				str_fact = ""
			str_den = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = " + str_fact + "(" + str_num + " - " + str_squares + str_delta + ") / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_fact + "(" + str_num + " + " + str_squares + str_delta + ") / " + str_den)
		else :
			fact = 1 if not primes1 else primes1[0]
			den = 1 if not primes2 else primes2[0]
	else :
		fact = old_fact
		den = old_den
	str1  =str_fact + "(" + str_num + " - " + str_squares + str_delta + ") / " + str_den
	str2 = str_fact + "(" + str_num + " + " + str_squares + str_delta + ") / " + str_den
	arround1 = __utils__.ft_round(fact * (num - squares * __utils__.ft_sqrt(delta_num)) / den, 14)
	arround2 = __utils__.ft_round(fact * (num + squares * __utils__.ft_sqrt(delta_num)) / den, 14)
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
