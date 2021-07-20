# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree2_neg_notb.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/06 18:09:37 by qpupier           #+#    #+#              #
#    Updated: 2021/07/19 18:05:14 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__
import bonus.degree2.neg.notb.a as __a__
import bonus.degree2.neg.notb.nota as __not_a__

def	delta_neg_notb(var, a, delta, p) :
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	if __utils__.ft_round(a, p) == "1" :
		print()
		print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta, p))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = i√" + __utils__.ft_round(delta, p))
		return __not_a__.delta_neg_notb_nota(var, delta)
	return __a__.delta_neg_notb_a(var, a, delta, p)
