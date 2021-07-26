# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree2_neg.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/06 18:13:16 by qpupier           #+#    #+#              #
#    Updated: 2021/07/26 14:12:22 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus.degree2.neg import not_b as __not_b__
from bonus.degree2.neg import b as __b__

def	delta_neg(var, a, b, delta, p) :
	print()
	print("Discriminant is negative, there are 2 complex solutions :")
	print()
	print("\033[32m")
	print("Steps :")
	print()
	print("	" + var + "_1 = (-b - i√-Δ) / 2a")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (-b + i√-Δ) / 2a")
	if b < 0 :
		print()
		print("<=>	" + var + "_1 = (-(" + __utils__.ft_round(b, p) + ") - i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (-(" + __utils__.ft_round(b, p) + ") + i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	b *= -1
	str_b = __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	if str_b == "-0" :
		str_b = "0"
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + i√-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	delta *= -1
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - i√" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + i√" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	a *= 2
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - i√" + __utils__.ft_round(delta, p) + ") / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + i√" + __utils__.ft_round(delta, p) + ") / " + __utils__.ft_round(a, p))
	if b :
		result = __b__.delta_neg_b(var, a, b, delta, p)
	else :
		result = __not_b__.delta_neg_notb(var, a, delta, p)
	print("\033[0m")
	return result
