# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_sqrt.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 11:30:29 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 13:53:37 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import bonus.degree2.neg._b._a._not_sqrt.a_neg as __a_neg__
import bonus.degree2.neg._b._a._not_sqrt.a_pos as __a_pos__

def	delta_neg_b_a_notsqrt(var, a, b, delta, p) :
	if a < 0 :
		return __a_neg__.delta_neg_b_a_notsqrt_aneg(var, a, b, delta, p)
	return __a_pos__.delta_neg_b_a_notsqrt_apos(var, a, b, delta, p)
