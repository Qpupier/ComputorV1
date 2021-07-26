# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_delta_den.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 20:42:01 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 20:57:22 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_notb_nota_notsqrt_notdelta_notdeltaden(var, delta_num, delta_den) :
	str_num = __utils__.ft_round(delta_num, 0)
	str_den = __utils__.ft_round(delta_den, 0)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + "√" + str_den + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + "√" + str_den + " / " + str_den)
	print()
	print("<=>	" + var + "_1 = -√(" + str_num + " * " + str_den + ") / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √(" + str_num + " * " + str_den + ") / " + str_den)
	delta_num *= delta_den
	str_num = __utils__.ft_round(delta_num, 0)
	print()
	print("<=>	" + var + "_1 = -√" + str_num + " / " + str_den)
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + str_num + " / " + str_den)
	squares, delta_num = __bonus__.reduce_sqrt(delta_num)
	if not squares :
		arround = __utils__.ft_round(__utils__.ft_sqrt(delta_num) / delta_den, 14)
		print("\033[35m")
		if len(arround[arround.find('.') + 1:]) < 14 :
			print("<=>	" + var + "_1 = -" + arround)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 = " + arround)
			str1 = "-" + arround
			str2 = arround
		else :
			print("<=>	" + var + "_1 ≈ -" + arround)
			print("	\33[33mor\033[35m")
			print("<=>	" + var + "_2 ≈ " + arround)
			str1 = "-√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0)
			str2 = "√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0)
		return str1, str2
	print("TODO NOW")
	return "", ""
