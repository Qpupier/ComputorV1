# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    squares.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/23 20:00:26 by qpupier           #+#    #+#              #
#    Updated: 2021/08/23 20:44:00 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__
from bonus.degree2.pos._b._a._not_sqrt._squares import not_b as __not_b__
from bonus.degree2.pos._b._a._not_sqrt._squares import b as __b__

def	delta_pos_b_a_notsqrt_delta_squares(var, b, squares, delta, a, p) :
	str_b = __utils__.ft_round(b, p)
	str_num = __utils__.ft_round(delta, 0)
	str_a = __utils__.ft_round(a, p)
	sq = __bonus__.print_squares(squares, delta)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + sq + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + sq + ") / " + str_a)
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - √(" + __utils__.ft_round(tmp, 0) + " * " + str_num + ")) / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + √(" + __utils__.ft_round(tmp, 0) + " * " + str_num + ")) / " + str_a)
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + __utils__.ft_round(tmp, 0) + "√" + str_num + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + __utils__.ft_round(tmp, 0) + "√" + str_num + ") / " + str_a)
	squares = __utils__.ft_sqrt(tmp)
	str_squares = __utils__.ft_round(squares, 0) + "√" + str_num
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - " + str_squares + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + " + str_squares + ") / " + str_a)
	if b == int(b) :
		return __b__.delta_pos_b_nota_notsqrt_delta_squares_b(var, a, b, squares, delta, p)
	return __not_b__.delta_pos_b_nota_notsqrt_delta_squares_notb(var, a, b, squares, delta, str_squares, p)
