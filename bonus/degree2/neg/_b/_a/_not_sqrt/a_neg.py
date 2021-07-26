# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a_neg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 11:34:44 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 14:07:02 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.degree2.neg._b._a._not_sqrt._a_neg.not_ as __not__
import bonus.degree2.neg._b._a._not_sqrt._a_neg.b_not_int as __b_not_int__
import bonus.degree2.neg._b._a._not_sqrt._a_neg.b_int as __b_int__

def	delta_neg_b_a_notsqrt_aneg(var, a, b, delta, p) :
	str_b = __utils__.ft_round(b, p)
	a *= -1
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = -(" + str_b + " - i√" + __utils__.ft_round(delta, p) + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = -(" + str_b + " + i√" + __utils__.ft_round(delta, p) + ") / " + str_a)
	b *= -1
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " + i√" + __utils__.ft_round(delta, p) + ") / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " - i√" + __utils__.ft_round(delta, p) + ") / " + str_a)
	if a == 1 :
		return __not__.delta_neg_b_a_notsqrt_aneg_not(var, b, delta, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " / " + str_a + " + i√" + __utils__.ft_round(delta, p) + " / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " / " + str_a + " - i√" + __utils__.ft_round(delta, p) + " / " + str_a)
	b_a1 = b / a
	if b_a1 == int(b_a1) :
		return __b_int__.delta_neg_b_a_notsqrt_aneg_bint(var, a, b, delta, p)
	return __b_not_int__.delta_neg_b_a_notsqrt_aneg_bnotint(var, a, b, delta, p)
