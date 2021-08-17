# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_sqrt.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 15:15:28 by qpupier           #+#    #+#              #
#    Updated: 2021/08/17 16:28:36 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from bonus.degree2.pos._b._not_a._not_sqrt import not_delta as __not_delta__
from bonus.degree2.pos._b._not_a._not_sqrt import delta as __delta__

def	delta_pos_b_nota_notsqrt(var, b, delta, sqrt_delta, p) :
	if delta == int(delta) :
		return __delta__.delta_pos_notb_nota_notsqrt_delta(var, b, delta, sqrt_delta)
	return __not_delta__.delta_pos_notb_nota_notsqrt_notdelta(var, b, delta, p)