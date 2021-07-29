# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_b.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 19:15:56 by qpupier           #+#    #+#              #
#    Updated: 2021/07/29 18:36:41 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus.degree2.pos._not_b import not_a as __not_a__
from bonus.degree2.pos._not_b import a as __a__

def	delta_pos_notb(var, a, delta, p) :
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	if a == 1 :
		return __not_a__.delta_pos_notb_nota(var, delta, p)
	return __a__.delta_pos_notb_a(var, a, delta, p)
	print("TODO NOW")
	return "", ""
