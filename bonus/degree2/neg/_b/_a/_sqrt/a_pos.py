# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a_pos.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 11:59:51 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 13:53:18 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.degree2.neg._b._a._sqrt._a_pos.b_not_int as __b_not_int__
import bonus.degree2.neg._b._a._sqrt._a_pos.b_int as __b_int__

def delta_neg_b_a_sqrt_apos(var, a, b, delta_sqrt, p) :
	str_b = __utils__.ft_round(b, p)
	str_a = __utils__.ft_round(a, p)
	str_delta_sqrt = __utils__.ft_round(delta_sqrt, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " / " + str_a + " - " + str_delta_sqrt + "i / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " / " + str_a + " + " + str_delta_sqrt + "i / " + str_a)
	tmp_b = b / a
	if tmp_b == int(tmp_b) :
		b = tmp_b
		return __b_int__.delta_neg_b_a_sqrt_apos_bint(var, a, b, delta_sqrt, p)
	return __b_not_int__.delta_neg_b_a_sqrt_apos_notbint(var, a, b, delta_sqrt, p)
