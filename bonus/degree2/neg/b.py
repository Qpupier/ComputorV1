# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    b.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/14 15:04:11 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 13:54:32 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import bonus.degree2.neg._b.not_a as __not_a__
import bonus.degree2.neg._b.a as __a__

def	delta_neg_b(var, a, b, delta, p) :
	if a == 1 :
		return __not_a__.delta_neg_b_nota(var, b, delta, p)
	return __a__.delta_neg_b_a(var, a, b, delta, p)
