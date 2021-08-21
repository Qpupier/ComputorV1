# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 12:06:05 by qpupier           #+#    #+#              #
#    Updated: 2021/08/21 18:14:05 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__
from bonus.degree2.pos._b._a import not_sqrt as __not_sqrt__
from bonus.degree2.pos._b._a import sqrt as __sqrt__

def	delta_pos_b_a(var, a, b, delta, p) :
	sqrt_delta = __utils__.ft_sqrt(delta)
	if sqrt_delta == int(sqrt_delta) :
		return __sqrt__.delta_pos_b_a_sqrt(var, b, sqrt_delta, a, p)
	return __not_sqrt__.delta_pos_b_a_notsqrt(var, b, delta, sqrt_delta, a, p)
