# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_a.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 12:08:41 by qpupier           #+#    #+#              #
#    Updated: 2021/08/21 18:06:20 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus.degree2.pos._b._not_a import not_sqrt as __not_sqrt__
from bonus.degree2.pos._b._not_a import sqrt as __sqrt__

def	delta_pos_b_nota(var, b, delta, p) :
	str_b = __utils__.ft_round(b, p)
	str_delta = __utils__.ft_round(delta, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " - √" + str_delta)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " + √" + str_delta)
	sqrt_delta = __utils__.ft_sqrt(delta)
	if sqrt_delta == int(sqrt_delta) :
		return __sqrt__.delta_pos_b_nota_sqrt(var, b, sqrt_delta, p)
	return __not_sqrt__.delta_pos_b_nota_notsqrt(var, b, delta, sqrt_delta, p)
