# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_squares.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/18 14:03:57 by qpupier           #+#    #+#              #
#    Updated: 2021/08/18 14:45:27 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_b_nota_notsqrt_notdelta_delta_den_notsquares(var, b, delta_num, delta_den, p) :
	str_delta_num = __utils__.ft_round(delta_num, 0)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	if b == int(b) :
		str_b = __utils__.ft_round(b, 0)
		arround1 = __utils__.ft_round(b - __utils__.ft_sqrt(delta_num) / delta_den, 14)
		arround2 = __utils__.ft_round(b + __utils__.ft_sqrt(delta_num) / delta_den, 14)
		str1 = str_b + " - √" + str_delta_num + " / " + str_delta_den
		str2 = str_b + " + √" + str_delta_num + " / " + str_delta_den
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 13 :
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
	mult = __bonus__.irreducible_mult(b, 1, p)
	num = int(__utils__.ft_round(b * mult, 0))
	den = int(__utils__.ft_round(mult, 0))
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - √" + str_delta_num + " / " + str_delta_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + " / " + str_den + " + √" + str_delta_num + " / " + str_delta_den)
	if den == delta_den :
		print()
		print("<=>	" + var + "_1 = (" + str_num + " - √" + str_delta_num + ") / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_num + " + √" + str_delta_num + ") / " + str_den)
		str1 = "(" + str_num + " - √" + str_delta_num + ") / " + str_den
		str2 = "(" + str_num + " + √" + str_delta_num + ") / " + str_den
		arround1 = __utils__.ft_round(b - __utils__.ft_sqrt(delta_num) / delta_den, 14)
		arround2 = __utils__.ft_round(b + __utils__.ft_sqrt(delta_num) / delta_den, 14)
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 13 :
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
	print("TODO NOW")
	# primes1 = __bonus__.primes(num)
	# primes2 = __bonus__.primes(den)
	# delete = []
	# __bonus__.reduce_fraction(primes1, primes2, delete)
	# num = __bonus__.print_frac(primes1, delete, True)
	# den = __bonus__.print_frac(primes2, delete, False)
	# if len(num) > 1 or len(den) > 1 :
	# 	print()
	# 	print("<=>	" + var + "_1 = " + num + " / " + den + " - √" + str_delta_num + " / " + str_delta_den)
	# 	print("	\33[33mor\033[32m")
	# 	print("	" + var + "_2 = " + num + " / " + den + " + √" + str_delta_num + " / " + str_delta_den)
	# 	__bonus__.fraction_delete(primes1, delete.copy())
	# 	__bonus__.fraction_delete(primes2, delete.copy())
	# 	str_num = __bonus__.print_frac(primes1, None, True)
	# 	str_den = __bonus__.print_frac(primes2, None, False)
	# 	print()
	# 	print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - √" + str_delta_num + " / " + str_delta_den)
	# 	print("	\33[33mor\033[32m")
	# 	print("	" + var + "_2 = " + str_num + " / " + str_den + " + √" + str_delta_num + " / " + str_delta_den)
	# 	if len(primes1) > 1 or len(primes2) > 1 :
	# 		num, den = __bonus__.irreducible(primes1, primes2)
	# 		str_num = __utils__.ft_round(num, 0)
	# 		str_den = __utils__.ft_round(den, 0)
	# 		print()
	# 		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - √" + str_delta_num + " / " + str_delta_den)
	# 		print("	\33[33mor\033[32m")
	# 		print("	" + var + "_2 = " + str_num + " / " + str_den + " + √" + str_delta_num + " / " + str_delta_den)
	# 	else :
	# 		num = 1 if not primes1 else primes1[0]
	# 		den = 1 if not primes2 else primes2[0]
	return "", ""
