# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_a.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 19:22:06 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 19:40:47 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus.degree2.pos._not_b._not_a import not_sqrt as __not_sqrt__
from bonus.degree2.pos._not_b._not_a import sqrt as __sqrt__

def	delta_pos_notb_nota(var, delta, p) :
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(delta, p))
	sqrt_delta = __utils__.ft_sqrt(delta)
	if sqrt_delta == int(sqrt_delta) :
		return __sqrt__.delta_pos_notb_nota_sqrt(var, sqrt_delta)
	return __not_sqrt__.delta_pos_notb_nota_notsqrt(var, delta, sqrt_delta, p)
