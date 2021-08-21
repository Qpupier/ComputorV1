# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    delta_den.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/18 13:51:04 by qpupier           #+#    #+#              #
#    Updated: 2021/08/21 17:55:30 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__
from bonus.degree2.pos._b._not_a._not_sqrt._not_delta._delta_den import not_squares as __not_squares__
from bonus.degree2.pos._b._not_a._not_sqrt._not_delta._delta_den import squares as __squares__

def	delta_pos_b_nota_notsqrt_notdelta_deltaden(var, b, delta_num, delta_den, p) :
	str_b = __utils__.ft_round(b, p)
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - √" + str_num + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + √" + str_num + " / " + str_den)
	squares, delta_num = __bonus__.reduce_sqrt(delta_num)
	if not squares :
		return __not_squares__.delta_pos_b_nota_notsqrt_notdelta_delta_den_notsquares(var, b, delta_num, delta_den, p)
	return __squares__.delta_pos_b_nota_notsqrt_notdelta_delta_den_squares(var, b, squares, delta_num, delta_den, p)
