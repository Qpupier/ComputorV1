# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree2_pos.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 18:12:55 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 18:21:23 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos(var, a, b, delta, p) :
	print()
	print("Discriminant is positive, there are 2 real solutions :")
	print()
	print("\033[32m")
	print("Steps :")
	print()
	print("	" + var + "_1 = (-b - √Δ) / 2a")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (-b + √Δ) / 2a")
	if b < 0 :
		print()
		print("<=>	" + var + "_1 = (-(" + __utils__.ft_round(b, p) + ") - √" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (-(" + __utils__.ft_round(b, p) + ") + √" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	b *= -1
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	if str_b == "-0" :
		str_b = "0"
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - √" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + √" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	a *= 2
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + __utils__.ft_round(delta, p) + ") / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + __utils__.ft_round(delta, p) + ") / " + __utils__.ft_round(a, p))
	# if b :
	# 	result = __b__.delta_neg_b(var, a, b, delta, p)
	# else :
	# 	result = __not_b__.delta_neg_notb(var, a, delta, p)
	print("\033[0m")
	# return result
	return "", ""
