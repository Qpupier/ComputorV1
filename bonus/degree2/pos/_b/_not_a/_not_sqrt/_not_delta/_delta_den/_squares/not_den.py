# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_den.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/21 16:11:23 by qpupier           #+#    #+#              #
#    Updated: 2021/08/21 17:37:39 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from bonus.degree2.pos._b._not_a._not_sqrt._not_delta._delta_den._squares.den import delta_pos_b_nota_notsqrt_notdelta_delta_den_squares_den
import utils as __utils__

def	delta_pos_b_nota_notsqrt_notdelta_delta_den_squares_notden(var, num, den, k, delta_num, delta_den) :
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	str_k = __utils__.ft_round(k, 0)
	str_delta = __utils__.ft_round(delta_num, 0)
	str_delta_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = (" + str_num + "\033[31m * " + str_delta_den + "\033[32m) / (" + str_den + "\033[31m * " + str_delta_den + "\033[32m)" + " - (" + str_k + "\033[31m * " + str_den + "\033[32m)√" + str_delta + " / (" + str_delta_den + "\033[31m * " + str_den + "\033[32m)")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_num + "\033[31m * " + str_delta_den + "\033[32m) / (" + str_den + "\033[31m * " + str_delta_den + "\033[32m)" + " + (" + str_k + "\033[31m * " + str_den + "\033[32m)√" + str_delta + " / (" + str_delta_den + "\033[31m * " + str_den + "\033[32m)")
	num *= delta_den
	k *= den
	den *= delta_den
	str_num = __utils__.ft_round(num, 0)
	str_den = __utils__.ft_round(den, 0)
	str_k = __utils__.ft_round(k, 0)
	str_delta = __utils__.ft_round(delta_num, 0)
	print()
	print("<=>	" + var + "_1 = " + str_num + " / " + str_den + " - " + str_k + "√" + str_delta + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_num + " / " + str_den + " + " + str_k + "√" + str_delta + " / " + str_den)
	return delta_pos_b_nota_notsqrt_notdelta_delta_den_squares_den(var, num, k, delta_num, den)
	print("TODO NOW")
	return "", ""
