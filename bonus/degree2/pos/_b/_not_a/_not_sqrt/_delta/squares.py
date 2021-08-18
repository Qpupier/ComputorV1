# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    squares.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 16:39:58 by qpupier           #+#    #+#              #
#    Updated: 2021/08/18 12:19:52 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__
from bonus.degree2.pos._b._not_a._not_sqrt._delta._squares import not_b as __not_b__
from bonus.degree2.pos._b._not_a._not_sqrt._delta._squares import b as __b__

def	delta_pos_notb_nota_notsqrt_delta_squares(var, b, squares, delta_num, p) :
	str_b = __utils__.ft_round(b, p)
	str_num = __utils__.ft_round(delta_num, 0)
	sq = __bonus__.print_squares(squares, delta_num)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - √" + sq)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + √" + sq)
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = " + str_b + " - √(" + __utils__.ft_round(tmp, 0) + " * " + str_num + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + √(" + __utils__.ft_round(tmp, 0) + " * " + str_num + ")")
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = " + str_b + " - √" + __utils__.ft_round(tmp, 0) + "√" + str_num)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + √" + __utils__.ft_round(tmp, 0) + "√" + str_num)
	squares = __utils__.ft_sqrt(tmp)
	str_squares = __utils__.ft_round(squares, 0) + "√" + str_num
	str1 = str_b + " - " + str_squares
	str2 = str_b + " + " + str_squares
	print()
	print("<=>	" + var + "_1 = " + str1)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str2)
	if b == int(b) :
		return __b__.delta_pos_notb_nota_notsqrt_delta_squares_b(var, b, squares, delta_num)
	return __not_b__.delta_pos_notb_nota_notsqrt_delta_squares_notb(var, b, squares, delta_num, str_squares, p)
