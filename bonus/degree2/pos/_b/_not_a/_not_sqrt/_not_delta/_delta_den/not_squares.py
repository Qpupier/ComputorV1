# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_squares.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/18 14:03:57 by qpupier           #+#    #+#              #
#    Updated: 2021/08/21 11:19:03 by qpupier          ###   ########lyon.fr    #
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
	mult = delta_den / den
	num *= mult
	den *= mult
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - √" + str_delta_num + " / " + str_delta_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + " / " + str_den + " + √" + str_delta_num + " / " + str_delta_den)
	print()
	print("<=>	" + var + "_1 = (" + str_num + " - √" + str_delta_num + ") / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_num + " + √" + str_delta_num + ") / " + str_den)
	str1 = "(" + str_num + " - √" + str_delta_num + ") / " + str_den
	str2 = "(" + str_num + " + √" + str_delta_num + ") / " + str_den
	arround1 = __utils__.ft_round((num - __utils__.ft_sqrt(delta_num)) / delta_den, 14)
	arround2 = __utils__.ft_round((num + __utils__.ft_sqrt(delta_num)) / delta_den, 14)
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
	return "", ""
