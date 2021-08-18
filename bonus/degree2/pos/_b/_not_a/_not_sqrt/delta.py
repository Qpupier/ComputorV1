# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    delta.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 16:26:35 by qpupier           #+#    #+#              #
#    Updated: 2021/08/18 11:42:29 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from bonus import utils as __bonus__
from bonus.degree2.pos._b._not_a._not_sqrt._delta import not_squares as __not_squares__
from bonus.degree2.pos._b._not_a._not_sqrt._delta import squares as __squares__

def	delta_pos_notb_nota_notsqrt_delta(var, b, delta, sqrt_delta, p) :
	squares, delta_num = __bonus__.reduce_sqrt(delta)
	if not squares :
		return __not_squares__.delta_pos_notb_nota_notsqrt_delta_notsquares(var, b, delta, sqrt_delta, p)
	return __squares__.delta_pos_notb_nota_notsqrt_delta_squares(var, b, squares, delta_num, p)
