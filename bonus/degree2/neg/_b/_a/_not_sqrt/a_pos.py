# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a_pos.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 11:35:14 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 14:07:19 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.degree2.neg._b._a._not_sqrt._a_pos.not_ as __not__
import bonus.degree2.neg._b._a._not_sqrt._a_pos.b_not_int as __b_not_int__
import bonus.degree2.neg._b._a._not_sqrt._a_pos.b_int as __b_int__

def	delta_neg_b_a_notsqrt_apos(var, a, b, delta, p) :
	str_b = __utils__.ft_round(b, p)
	str_a = __utils__.ft_round(a, p)
	if a == 1 :
		return __not__.delta_neg_b_a_notsqrt_apos_not(var, b, delta, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " / " + str_a + " - i√" + __utils__.ft_round(delta, p) + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " / " + str_a + " + i√" + __utils__.ft_round(delta, p) + " / " + str_a)
	b_a1 = b / a
	if b_a1 == int(b_a1) :
		return __b_int__.delta_neg_b_a_notsqrt_apos_bint(var, a, b, delta, p)
	return __b_not_int__.delta_neg_b_a_notsqrt_apos_bnotint(var, a, b, delta, p)
