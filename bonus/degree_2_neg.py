# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree_2_neg.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/14 16:04:15 by qpupier           #+#    #+#              #
#    Updated: 2021/06/14 20:26:58 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	delta_neg_notb_nota(var, delta) :
	if __utils__.ft_sqrt(delta) == int(__utils__.ft_sqrt(delta)) :
		delta = __utils__.ft_sqrt(delta)
		print()
		print("<=>	" + var + "_1 = -" + __utils__.ft_round(delta, 11))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + __utils__.ft_round(delta, 11))
		return (-2, 2), (-2, 2)
	delta = __bonus__.reduce_sqrt(delta)
	print("TODO NOW")

def	delta_neg_notb(var, a, delta, p) :
	print()
	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = √" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	if __utils__.ft_round(a, p) == "1" :
		print()
		print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta, p))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = √" + __utils__.ft_round(delta, p))
		delta_neg_notb_nota(var, delta)
	else :
		print("TODO")
		# delta_neg_notb_a()
	# if b :
	# 	print("TODO")
	# else :
	# 	print()
	# 	print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	# 	print("	\33[33mor\033[32m")
	# 	print("	" + var + "_2 = √" + __utils__.ft_round(delta, p) + " / " + __utils__.ft_round(a, p))
	# 	if __utils__.ft_round(a, p) == "1" :
	# 		print()
	# 		print("<=>	" + var + "_1 = -√" + __utils__.ft_round(delta, p))
	# 		print("	\33[33mor\033[32m")
	# 		print("	" + var + "_2 = √" + __utils__.ft_round(delta, p))
	# 		print("TODO")
	# 	print("TODO")

def	delta_neg(var, a, b, delta, p) :
	print()
	print("Discriminant is negative, there are 2 complex solutions :")
	print()
	print("\033[32m")
	print("Steps :")
	print()
	print("	" + var + "_1 = (-b - √-Δ) / 2a")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (-b + √-Δ) / 2a")
	if b < 0 :
		print()
		print("<=>	" + var + "_1 = (-(" + __utils__.ft_round(b, p) + ") - √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (-(" + __utils__.ft_round(b, p) + ") + √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
		b *= -1
		str_b = __utils__.ft_round(b, p)
	else :
		str_b = "-" + __utils__.ft_round(b, p)
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	if str_b == "-0" :
		str_b = "0"
		print()
		print("<=>	" + var + "_1 = (" + str_b + " - √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = (" + str_b + " + √-(" + __utils__.ft_round(delta, p) + ")) / (2 * " + __utils__.ft_round(a, p) + ")")
	delta *= -1
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + __utils__.ft_round(delta, p) + ") / (2 * " + __utils__.ft_round(a, p) + ")")
	a *= 2
	print()
	print("<=>	" + var + "_1 = (" + str_b + " - √" + __utils__.ft_round(delta, p) + ") / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = (" + str_b + " + √" + __utils__.ft_round(delta, p) + ") / " + __utils__.ft_round(a, p))
	if b :
		# delta_neg_b()
		print("TO DO")
	else :
		delta_neg_notb(var, a, delta, p)
	print("\033[0m")
