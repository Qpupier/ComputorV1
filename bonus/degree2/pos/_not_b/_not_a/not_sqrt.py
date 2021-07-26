# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    not_sqrt.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 19:35:37 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 19:52:29 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from bonus.degree2.pos._not_b._not_a._not_sqrt import not_delta as __not_delta__
from bonus.degree2.pos._not_b._not_a._not_sqrt import delta as __delta__

def	delta_pos_notb_nota_notsqrt(var, delta, sqrt_delta, p) :
	if delta == int(delta) :
		return __delta__.delta_pos_notb_nota_notsqrt_delta(var, delta, sqrt_delta)
	return __not_delta__.delta_pos_notb_nota_notsqrt_notdelta(var, delta, sqrt_delta, p)
	squares, delta_num = __bonus__.reduce_sqrt(delta)
	# a2 = a
	# str_a2 = __utils__.ft_round(a2, 0)
	if not squares :
	# 	tmp_a2 = 1 / a2
	# 	if tmp_a2 == int(tmp_a2) :
	# 		a2 = tmp_a2
	# 		str_a2 = __utils__.ft_round(a2, 0)
	# 		str_delta = __utils__.ft_round(delta, 0)
	# 		print()
	# 		print("<=>	" + var + "_1 = " + str_b + " + " + str_a2 + "i√" + str_delta)
	# 		print("	\33[33mor\033[32m")
	# 		print("	" + var + "_2 = " + str_b + " - " + str_a2 + "i√" + str_delta)
			arround = __utils__.ft_round(sqrt_delta, 14)
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
				str1 = "-√" + __utils__.ft_round(delta, 0)
				str2 = "√" + __utils__.ft_round(delta, 0)
			return str1, str2
	# 	if a2 == int(a2) :
	# 		arround = __utils__.ft_round(__utils__.ft_sqrt(delta) / a2, 14) + "i"
	# 		print("\033[35m")
	# 		if len(arround[arround.find('.') + 1:]) < 15:
	# 			print("<=>	" + var + "_1 = " + str_b + " + " + arround)
	# 			print("	\33[33mor\033[35m")
	# 			print("<=>	" + var + "_2 = " + str_b + " - " + arround)
	# 			str1 = str_b + " + " + arround
	# 			str2 = str_b + " - " + arround
	# 		else :
	# 			print("<=>	" + var + "_1 ≈ " + str_b + " + " + arround)
	# 			print("	\33[33mor\033[35m")
	# 			print("<=>	" + var + "_2 ≈ " + str_b + " - " + arround)
	# 			str1 = str_b + " + i√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2
	# 			str2 = str_b + " - i√" + __utils__.ft_round(delta_num, 0) + " / " + str_a2
	# 		return str2, str1
	return "", ""
