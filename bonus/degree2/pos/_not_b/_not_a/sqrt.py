# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sqrt.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 19:35:26 by qpupier           #+#    #+#              #
#    Updated: 2021/07/27 16:45:05 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__

def	delta_pos_notb_nota_sqrt(var, sqrt_delta) :
	str1 = "-" + __utils__.ft_round(sqrt_delta, 0)
	str2 = __utils__.ft_round(sqrt_delta, 0)
	print()
	print("<=>	" + var + "_1 = " + str1)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + str2)
	return str1, str2
