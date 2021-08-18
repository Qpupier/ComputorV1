# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_delta.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 16:26:33 by qpupier           #+#    #+#              #
#    Updated: 2021/08/18 13:53:43 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__
from bonus.degree2.pos._b._not_a._not_sqrt._not_delta import not_delta_den as __not_delta_den__
from bonus.degree2.pos._b._not_a._not_sqrt._not_delta import delta_den as __delta_den__

def	delta_pos_b_nota_notsqrt_notdelta(var, b, delta, p) :
	str_b = __utils__.ft_round(b, p)
	mult = __bonus__.irreducible_mult(delta, 1, p)
	delta_num = int(delta * mult)
	delta_den = int(mult)
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - √(" + str_num + " / " + str_den + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + √(" + str_num + " / " + str_den + ")")
	print()
	print("<=>	" + var + "_1 = " + str_b + " - √" + str_num + " / √" + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + √" + str_num + " / √" + str_den)
	delta_den_sqrt = __utils__.ft_sqrt(delta_den)
	if delta_den_sqrt == int(delta_den_sqrt) :
		return __delta_den__.delta_pos_b_nota_notsqrt_notdelta_deltaden(var, b, delta_num, delta_den_sqrt, p)
	return __not_delta_den__.delta_pos_b_nota_notsqrt_notdelta_notdeltaden(var, b, delta_num, delta_den, p)
