# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a_neg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 11:59:42 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 14:07:26 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.degree2.neg._b._a._sqrt._a_neg.not_ as __not__
import bonus.degree2.neg._b._a._sqrt._a_neg.b_not_int as __b_not_int__
import bonus.degree2.neg._b._a._sqrt._a_neg.b_int as __b_int__

def	delta_neg_b_a_sqrt_aneg(var, a, b, delta_sqrt, p) :
	str_b = __utils__.ft_round(b, p)
	str_a = __utils__.ft_round(a, p)
	str_delta_sqrt = __utils__.ft_round(delta_sqrt, p)
	if str_delta_sqrt == "1" :
		str_delta_sqrt = ""
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - " + str_delta_sqrt + "i) / " + str_a)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + " + str_delta_sqrt + "i) / " + str_a)
	a *=  -1
	str_a = __utils__.ft_round(a, p)
	print()
	print("<=>	" + var + "_1 = -(" + str_b + " - " + str_delta_sqrt + "i) / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = -(" + str_b + " + " + str_delta_sqrt + "i) / " + str_a)
	b *= -1
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " + " + str_delta_sqrt + "i) / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " - " + str_delta_sqrt + "i) / " + str_a)
	if str_a == "1" :
		return __not__.delta_neg_b_a_sqrt_aneg_not(var, b, delta_sqrt, p)
	print()
	print("<=>	" + var + "_1 = " + str_b + " / " + str_a + " + " + str_delta_sqrt + "i / " + str_a)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str_b + " / " + str_a + " - " + str_delta_sqrt + "i / " + str_a)
	tmp_b = b / a
	if tmp_b == int(tmp_b) :
		b = tmp_b
		return __b_int__.delta_neg_b_a_sqrt_aneg_bint(var, a, b, delta_sqrt, p)
	return __b_not_int__.delta_neg_b_a_sqrt_aneg_notbint(var, a, b, delta_sqrt, p)
