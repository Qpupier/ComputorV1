# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 19:27:48 by qpupier           #+#    #+#              #
#    Updated: 2021/07/27 17:34:56 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_notb_a_notsqrt(var, delta, a, p) :
	print("TODO NOW")
	return "", ""

def	delta_pos_notb_a_sqrt(var, delta, a, p) :
	print("TODO")
	return "", ""

def	delta_pos_notb_a(var, a, delta, p) :
	sqrt_delta = __utils__.ft_sqrt(delta)
	if sqrt_delta == int(sqrt_delta) :
		return delta_pos_notb_a_sqrt(var, sqrt_delta, a, p)
	return delta_pos_notb_a_notsqrt(var, sqrt_delta, a, p)
