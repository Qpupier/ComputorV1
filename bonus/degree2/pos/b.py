# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    b.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 19:11:56 by qpupier           #+#    #+#              #
#    Updated: 2021/08/17 12:10:00 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from bonus.degree2.pos._b import not_a as __not_a__
from bonus.degree2.pos._b import a as __a__

def	delta_pos_b(var, a, b, delta, p) :
	if a == 1 :
		return __not_a__.delta_pos_b_nota(var, b, delta, p)
	return __a__.delta_pos_b_a(var, a, b, delta, p)
