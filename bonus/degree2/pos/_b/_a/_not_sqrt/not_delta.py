# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_delta.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/21 18:16:53 by qpupier           #+#    #+#              #
#    Updated: 2021/08/23 19:17:30 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__
from bonus.degree2.pos._b._a._not_sqrt._delta_den import not_squares as __not_squares__
from bonus.degree2.pos._b._a._not_sqrt._delta_den import squares as __squares__

def	delta_pos_b_a_notsqrt_notdelta_deltaden(var, b, delta, delta_den, a, p) :
	str_b = __utils__.ft_round(b, p)
	str_num = __utils__.ft_round(delta, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + str_num + " / " + str_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + str_num + " / " + str_den + ") / " + str_a)
	squares, delta = __bonus__.reduce_sqrt(delta)
	if not squares :
		return __not_squares__.delta_pos_b_a_notsqrt_notdelta_delta_den_notsquares(var, b, delta, delta_den, a, p)
	return __squares__.delta_pos_b_a_notsqrt_notdelta_delta_den_squares(var, b, squares, delta, delta_den, a, p)

def	delta_pos_b_a_notsqrt_notdelta(var, b, delta, a, p) :
	str_b = __utils__.ft_round(b, p)
	mult = __bonus__.irreducible_mult(delta, 1, p)
	delta_num = int(__utils__.ft_round(delta * mult, 0))
	delta_den = int(mult)
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √(" + str_num + " / " + str_den + ")) / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √(" + str_num + " / " + str_den + ")) / " + str_a)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + str_num + " / √" + str_den + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + str_num + " / √" + str_den + ") / " + str_a)
	delta_den_sqrt = __utils__.ft_sqrt(delta_den)
	if delta_den_sqrt != int(delta_den_sqrt) :
		str_b = __utils__.ft_round(b, p)
		str_num = __utils__.ft_round(delta_num, 0)
		str_den = __utils__.ft_round(delta_den, 0)
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - √" + str_num + "√" + str_den + " / " + str_den + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + √" + str_num + "√" + str_den + " / " + str_den + ") / " + str_a)
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - √(" + str_num + " * " + str_den + ") / " + str_den + ") / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + √(" + str_num + " * " + str_den + ") / " + str_den + ") / " + str_a)
		delta_num *= delta_den
		return delta_pos_b_a_notsqrt_notdelta_deltaden(var, b, delta_num, delta_den, a, p)
	return delta_pos_b_a_notsqrt_notdelta_deltaden(var, b, delta_num, delta_den_sqrt, a, p)
