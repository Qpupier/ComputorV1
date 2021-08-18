# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    b.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/08/17 17:37:53 by qpupier           #+#    #+#              #
#    Updated: 2021/08/18 12:09:30 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
from bonus import utils as __bonus__

def	delta_pos_notb_nota_notsqrt_delta_squares_b(var, b, k, delta_den) :
	primes1 = __bonus__.primes(b)
	primes2 = __bonus__.primes(k)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	str_b = __bonus__.print_fact(primes1, delete, False)
	str_k = __bonus__.print_fact(primes2, delete, False)
	str_delta = "√" + __utils__.ft_round(delta_den, 0)
	if delete :
		print()
		print("<=>	" + var + "_1 = " + str_b + " - " + str_k + str_delta)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_b + " + " + str_k + str_delta)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		fact, fact = __bonus__.irreducible(None, delete)
		str_fact = "\033[37m" + __utils__.ft_round(fact, 0) + "\033[32m"
		b, k = __bonus__.irreducible(primes1, primes2)
		if len(delete) > 1 or len(primes1) > 1 or len(primes2) > 1 :
			str_b = " * " + __utils__.ft_round(b, 0)
			str_k = " * " + __utils__.ft_round(k, 0)
			if str_k == " * 1" :
				str_k = ""
			str1 = str_fact + str_b + " - " + str_fact + str_k + str_delta
			str2 = str_fact + str_b + " + " + str_fact + str_k + str_delta
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
		str_b = __utils__.ft_round(b, 0)
		str_k = __utils__.ft_round(k, 0)
		if str_k == "1" :
			str_k = ""
		str1 = str_fact + "(" + str_b + " - " + str_k + str_delta + ")"
		str2 = str_fact + "(" + str_b + " + " + str_k + str_delta + ")"
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
	else :
		fact = 1
		str_b = __utils__.ft_round(b, 0)
		str_k = __utils__.ft_round(k, 0)
		if str_k == "1" :
			str_k = ""
		str1 = str_b + " - " + str_k + str_delta
		str2 = str_b + " + " + str_k + str_delta
	str1 = str1.replace("\033[37m", "").replace("\033[32m", "")
	str2 = str2.replace("\033[37m", "").replace("\033[32m", "")
	arround1 = __utils__.ft_round(fact * (b - k * __utils__.ft_sqrt(delta_den)), 14)
	arround2 = __utils__.ft_round(fact * (b + k * __utils__.ft_sqrt(delta_den)), 14)
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 14 :
		print("<=>	" + var + "_1 = " + arround1)
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 = " + arround2)
		str1 = arround1
		str2 = arround2
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		print("	" + var + "_2 ≈ " + arround2)
	return str1, str2
