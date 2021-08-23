# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_sqrt.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/21 18:12:30 by qpupier           #+#    #+#              #
#    Updated: 2021/08/23 20:04:32 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus.degree2.pos._b._a._not_sqrt import not_delta as __not_delta__
from bonus.degree2.pos._b._a._not_sqrt import delta as __delta__

def	delta_pos_b_a_notsqrt(var, b, delta, sqrt_delta, a, p) :
	if not '.' in __utils__.ft_round(delta, p) :
		return __delta__.delta_pos_b_a_notsqrt_delta(var, b, int(delta), a, p)
	return __not_delta__.delta_pos_b_a_notsqrt_notdelta(var, b, delta, a, p)
