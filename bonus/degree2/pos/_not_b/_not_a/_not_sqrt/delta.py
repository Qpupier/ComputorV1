# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    delta.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 19:48:49 by qpupier           #+#    #+#              #
#    Updated: 2021/07/27 16:39:35 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def delta_pos_notb_nota_notsqrt_delta(var, delta, delta_sqrt) :
	squares, delta_num = __bonus__.reduce_sqrt(delta)
	str_num = __utils__.ft_round(delta_num, 0)
	if not squares :
		arround = __utils__.ft_round(delta_sqrt, 14)
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
			str1 = "-√" + str_num
			str2 = "√" + str_num
		return str1, str2
	sq = __bonus__.print_squares(squares, delta_num)
	print()
	print("<=>	" + var + "_1 = -√" + sq)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + sq)
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = -√(" + __utils__.ft_round(tmp, 0) + " * " + str_num + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = √(" + __utils__.ft_round(tmp, 0) + " * " + str_num + ")")
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(tmp, 0) + "√" + str_num)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(tmp, 0) + "√" + str_num)
	squares = __utils__.ft_sqrt(tmp)
	str_squares = __utils__.ft_round(squares, 0)
	str1 = "-" + str_squares + "√" + str_num
	str2 = str_squares + "√" + str_num
	print()
	print("<=>	" + var + "_1 = " + str1)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str2)
	arround = __utils__.ft_round(squares * __utils__.ft_sqrt(delta_num), 14)
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
		str1 = "-" + str_squares + "√" + __utils__.ft_round(delta_num, 0)
		str2 = str_squares + "√" + __utils__.ft_round(delta_num, 0)
	return str1, str2
