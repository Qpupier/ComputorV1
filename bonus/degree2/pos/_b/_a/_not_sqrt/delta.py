# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    delta.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/21 18:16:46 by qpupier           #+#    #+#              #
#    Updated: 2021/08/23 20:33:27 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from bonus import utils as __bonus__
from bonus.degree2.pos._b._a._not_sqrt import not_squares as __not_squares__
from bonus.degree2.pos._b._a._not_sqrt import squares as __squares__

def	delta_pos_b_a_notsqrt_delta(var, b, delta, a, p) :
	squares, delta = __bonus__.reduce_sqrt(delta)
	if not squares :
		return __not_squares__.delta_pos_b_a_notsqrt_delta_notsquares(var, b, delta, a, p)
	return __squares__.delta_pos_b_a_notsqrt_delta_squares(var, b, squares, delta, a, p)
