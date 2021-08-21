# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    squares.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/18 14:03:46 by qpupier           #+#    #+#              #
#    Updated: 2021/08/21 17:53:53 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__
from bonus.degree2.pos._b._not_a._not_sqrt._not_delta._delta_den._squares import not_den as __not_den__
from bonus.degree2.pos._b._not_a._not_sqrt._not_delta._delta_den._squares import den as __den__

def	delta_pos_b_nota_notsqrt_notdelta_delta_den_squares(var, b, squares, delta_num, delta_den, p) :
	str_b = __utils__.ft_round(b, p)
	str_num = __utils__.ft_round(delta_num, 0)
	sq = __bonus__.print_squares(squares, delta_num)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - √" + sq + " / " + str_delta_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + √" + sq + " / " + str_delta_den)
	if len(squares) > 1 :
		tmp = 1
		for each in squares :
			tmp *= each * each
		print()
		print("<=>	" + var + "_1 = " + str_b + " - √(" + __utils__.ft_round(tmp, 0) + " * " + str_num + ") / " + str_delta_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + √(" + __utils__.ft_round(tmp, 0) + " * " + str_num + ") / " + str_delta_den)
	else :
		tmp = squares[0] * squares[0]
	print()
	print("<=>	" + var + "_1 = " + str_b + " - √" + __utils__.ft_round(tmp, 0) + "√" + str_num + " / " + str_delta_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + √" + __utils__.ft_round(tmp, 0) + "√" + str_num + " / " + str_delta_den)
	squares = __utils__.ft_sqrt(tmp)
	str_squares = __utils__.ft_round(squares, 0) + "√" + str_num + " / " + str_delta_den
	print()
	print("<=>	" + var + "_1 = " + str_b + " - " + str_squares)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + " + str_squares)
	tmp = squares / delta_den
	if b != int(b) :
		mult = __bonus__.irreducible_mult(b, 1, p)
		num = int(__utils__.ft_round(b * mult, 0))
		den = int(__utils__.ft_round(mult, 0))
		str_num = __utils__.ft_round(num, 0)
		str_den = __utils__.ft_round(den, 0)
		print()
		print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - " + str_squares)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + " / " + str_den + " + " + str_squares)
		if str_den == str_delta_den :
			return __den__.delta_pos_b_nota_notsqrt_notdelta_delta_den_squares_den(var, num, squares, delta_num, den)
		return __not_den__.delta_pos_b_nota_notsqrt_notdelta_delta_den_squares_notden(var, num, den, squares, delta_num, delta_den)
	return __not_den__.delta_pos_b_nota_notsqrt_notdelta_delta_den_squares_notden(var, b, 1, squares, delta_num, delta_den)
	print("TODO NOW")
	return "", ""
