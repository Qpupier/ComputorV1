# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 11:13:26 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 13:53:59 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.degree2.neg._b._a.not_sqrt as __not_sqrt__
import bonus.degree2.neg._b._a.sqrt as __sqrt__

def	delta_neg_b_a(var, a, b, delta, p) :
	delta_sqrt = __utils__.ft_sqrt(delta)
	if delta_sqrt == int(delta_sqrt) :
		return __sqrt__.delta_neg_b_a_sqrt(var, a, b, delta_sqrt, p)
	return __not_sqrt__.delta_neg_b_a_notsqrt(var, a, b, delta, p)
