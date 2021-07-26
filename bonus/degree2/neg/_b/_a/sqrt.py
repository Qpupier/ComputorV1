# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sqrt.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 11:32:55 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 13:53:50 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.degree2.neg._b._a._sqrt.a_neg as __a_neg__
import bonus.degree2.neg._b._a._sqrt.a_pos as __a_pos__

def	delta_neg_b_a_sqrt(var, a, b, delta_sqrt, p) :
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - " + __utils__.ft_round(delta_sqrt, p) + "i) / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + " + __utils__.ft_round(delta_sqrt, p) + "i) / " + __utils__.ft_round(a, p))
	if a < 0 :
		return __a_neg__.delta_neg_b_a_sqrt_aneg(var, a, b, delta_sqrt, p)
	return __a_pos__.delta_neg_b_a_sqrt_apos(var, a, b, delta_sqrt, p)
