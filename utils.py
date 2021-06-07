# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 17:58:11 by qpupier           #+#    #+#              #
#    Updated: 2021/06/07 18:34:47 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from math import sqrt
def	ft_round(n, p) :
	r = round(n, p)
	if r == int(r) :
		r = int(r)
	return str(r)

def	ft_sqrt(nb, prec) :
	return sqrt(nb)
