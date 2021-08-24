# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/06 18:23:47 by qpupier           #+#    #+#              #
#    Updated: 2021/08/24 15:28:57 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import utils as __utils__
import bonus.utils as __bonus__

def	delta_neg_notb_a_discriminant(var, a, delta, p) :
	if a == int(a) :
		a = int(a)
		p = 0
	delta = __utils__.ft_sqrt(delta)
	print()
	print("<=>	" + var + "_1 = -" + __utils__.ft_round(delta, 0) + "i / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = " + __utils__.ft_round(delta, 0) + "i / " + __utils__.ft_round(a, p))
	mult = __bonus__.irreducible_mult(delta, a, p)
	if mult > 1 :
		delta = int(delta * mult)
		a = int(a * mult)
		print()
		print("<=>	" + var + "_1 = -" + __utils__.ft_round(delta, 0) + "i / " + __utils__.ft_round(a, 0))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + __utils__.ft_round(delta, 0) + "i / " + __utils__.ft_round(a, 0))
	primes1 = __bonus__.primes(delta)
	primes2 = __bonus__.primes(a)
	delete = []
	__bonus__.reduce_fraction(primes1, primes2, delete)
	if delete :
		str_num = __bonus__.print_frac(primes1, delete, True)
		str_den = __bonus__.print_frac(primes2, delete, False)
		print()
		print("<=>	" + var + "_1 = -" + str_num + "i / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + "i / " + str_den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		str_num = __bonus__.print_frac(primes1, None, True)
		if str_num == "1" or str_num == "-1" :
			str_num = str_num[:-1]
		str_den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = -" + str_num + "i / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str_num + "i / " + str_den)
		delta, a = __bonus__.irreducible(primes1, primes2)
		if len(primes1) > 1 or len(primes2) > 1 :
			str_delta = __utils__.ft_round(delta, 0)
			if str_delta == "1" :
				str_delta = ""
			print()
			print("<=>	" + var + "_1 = -" + str_delta + "i / " + __utils__.ft_round(a, 0))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_delta + "i / " + __utils__.ft_round(a, 0))
	if delta / a == int(delta / a) :
		delta = int(delta / a)
		if delta == -1 :
			str1 = "i"
			str2 = "-i"
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			return str1, str2
		if delta == 1 :
			str1 = "-i"
			str2 = "i"
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			return str1, str2
		if delta < 0 :
			delta *= -1
			str1 = __utils__.ft_round(delta, 0) + "i"
			str2 = "-" + __utils__.ft_round(delta, 0) + "i"
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			return str2, str1
		str1 = "-" + __utils__.ft_round(delta, 0) + "i"
		str2 = __utils__.ft_round(delta, 0) + "i"
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		return str1, str2
	str_delta1 = __utils__.ft_round(-delta, 0)
	if str_delta1 == "-1" :
		str_delta1 = "-"
	if str_delta1 == "1" :
		str_delta1 = ""
	str_delta2 = __utils__.ft_round(delta, 0)
	if str_delta2 == "-1" :
		str_delta2 = "-"
	if str_delta2 == "1" :
		str_delta2 = ""
	str1 = str_delta1 + "i / " + __utils__.ft_round(a, 0)
	str2 = str_delta2 + "i / " + __utils__.ft_round(a, 0)
	if a < 0 :
		delta *= -1
		a *= -1
		str_delta1 = __utils__.ft_round(-delta, 0)
		if str_delta1 == "-1" :
			str_delta1 = "-"
		if str_delta1 == "1" :
			str_delta1 = ""
		str_delta2 = __utils__.ft_round(delta, 0)
		if str_delta2 == "-1" :
			str_delta2 = "-"
		if str_delta2 == "1" :
			str_delta2 = ""
		str1 = str_delta1 + "i / " + __utils__.ft_round(a, 0)
		str2 = str_delta2 + "i / " + __utils__.ft_round(a, 0)
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
	arround1 = __utils__.ft_round(-delta / a, 15) + "i"
	arround2 = __utils__.ft_round(delta / a, 15) + "i"
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 15 :
		print("<=>	" + var + "_1 = " + arround1)
		str1 = arround1
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
	print("	\33[33mor\033[35m")
	if len(arround2[arround2.find('.') + 1:]) < 15 :
		print("	" + var + "_2 = " + arround2)
		str2 = arround2
	else :
		print("	" + var + "_2 ≈ " + arround2)
	if delta < 0 :
		return str2, str1
	return str1, str2

def delta_neg_notb_a_discriminant_float(var, a, delta, p) :
	mult = __bonus__.irreducible_mult(delta, 1, p)
	delta_num = int(delta * mult)
	delta_den = int(mult)
	print()
	print("<=>	" + var + "_1 = -i√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√(" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(a, p))
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + " / √" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + "√" + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print()
	print("<=>	" + var + "_1 = -i√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√(" + __utils__.ft_round(delta_num, 0) + " * " + __utils__.ft_round(delta_den, 0) + ") / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	delta_num *= delta_den
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + " / " + __utils__.ft_round(delta_den, 0) + " / " + __utils__.ft_round(a, p))
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta_num, 0) + " / (" + __utils__.ft_round(delta_den, 0) + " * " + __utils__.ft_round(a, p) + ")")
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta_num, 0) + " / (" + __utils__.ft_round(delta_den, 0) + " * " + __utils__.ft_round(a, p) + ")")
	delta = delta_num
	a *= delta_den
	print()
	print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, 0))
	print("	\33[33mor\033[32m")
	print("	" + var + "_2 = i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, 0))
	sq, delta = __bonus__.reduce_sqrt(delta)
	if sq :
		result = __bonus__.str_lst_sq(sq, delta)
		print()
		print("<=>	" + var + "_1 = -i√" + result + " / " + __utils__.ft_round(a, p))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = i√" + result + " / " + __utils__.ft_round(a, p))
		if len(sq) > 1 :
			sq = __bonus__.irreducible_sq(sq)
			result = __bonus__.str_lst_sq(sq, delta)
			print()
			print("<=>	" + var + "_1 = -i√" + result + " / " + __utils__.ft_round(a, p))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = i√" + result + " / " + __utils__.ft_round(a, p))
		print()
		print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(sq[0] * sq[0], 0) + "√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = i√" + __utils__.ft_round(sq[0] * sq[0], 0) + "√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
		primes1 = __bonus__.primes(sq[0])
		primes2 = __bonus__.primes(a)
		if len(primes1) > 1 or len(primes2) > 1 :
			print()
			print("<=>	" + var + "_1 = -" + __utils__.ft_round(sq[0], 0) + "i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + __utils__.ft_round(sq[0], 0) + "i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
		delete = []
		__bonus__.reduce_fraction(primes1, primes2, delete)
		num = __bonus__.print_frac(primes1, delete, True)
		den = __bonus__.print_frac(primes2, delete, False)
		print()
		print("<=>	" + var + "_1 = -" + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
		__bonus__.fraction_delete(primes1, delete.copy())
		__bonus__.fraction_delete(primes2, delete.copy())
		num = __bonus__.print_frac(primes1, None, True)
		den = __bonus__.print_frac(primes2, None, False)
		print()
		print("<=>	" + var + "_1 = -" + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
		num, den = __bonus__.irreducible(primes1, primes2)
		str_num = "" if num == 1 else __utils__.ft_round(num, 15)
		str_den = __utils__.ft_round(den, 15)
		if str_num or den < 0 :
			print()
			print("<=>	" + var + "_1 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
		if den == -1 :
			den *= -1
			str_den = __utils__.ft_round(den, 15)
			print()
			print("<=>	" + var + "_1 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			str1 = str_num + "i√" + __utils__.ft_round(delta, 0)
			str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(num * __utils__.ft_sqrt(delta), 15) + "i"
			arround2 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta), 15) + "i"
			print("\033[35m")
			if len(arround1[arround1.find('.') + 1:]) < 15 :
				print("<=>	" + var + "_1 = " + arround1)
				str1 = arround1
			else :
				print("<=>	" + var + "_1 ≈ " + arround1)
			print("	\33[33mor\033[35m")
			if len(arround2[arround2.find('.') + 1:]) < 15 :
				print("	" + var + "_2 = " + arround2)
				str2 = arround2
			else :
				print("	" + var + "_2 ≈ " + arround2)
			return str2, str1
		if den == 1 :
			str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
			str2 = str_num + "i√" + __utils__.ft_round(delta, 0)
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta), 15) + "i"
			arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta), 15) + "i"
			print("\033[35m")
			if len(arround1[arround1.find('.') + 1:]) < 15 :
				print("<=>	" + var + "_1 = " + arround1)
				str1 = arround1
			else :
				print("<=>	" + var + "_1 ≈ " + arround1)
			print("	\33[33mor\033[35m")
			if len(arround2[arround2.find('.') + 1:]) < 15 :
				print("	" + var + "_2 = " + arround2)
				str2 = arround2
			else :
				print("	" + var + "_2 ≈ " + arround2)
			return str1, str2
		if den < 0 :
			str_den = __utils__.ft_round(-den, 15)
			str1 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(num * __utils__.ft_sqrt(delta) / -den, 15) + "i"
			arround2 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta) / -den, 15) + "i"
		else :
			str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			str2 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta) / den, 15) + "i"
			arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta) / den, 15) + "i"
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 15 :
			print("<=>	" + var + "_1 = " + arround1)
			str1 = arround1
		else :
			print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		if len(arround2[arround2.find('.') + 1:]) < 15 :
			print("	" + var + "_2 = " + arround2)
			str2 = arround2
		else :
			print("	" + var + "_2 ≈ " + arround2)
		if den < 0 :
			return str2, str1
		return str1, str2
	str_num = ""
	str_den = __utils__.ft_round(a, 15)
	if a == -1 :
		a *= -1
		str_den = __utils__.ft_round(a, 15)
		print()
		print("<=>	" + var + "_1 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
		str1 = str_num + "i√" + __utils__.ft_round(delta, 0)
		str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		arround1 = __utils__.ft_round(__utils__.ft_sqrt(delta), 15) + "i"
		arround2 = __utils__.ft_round(-__utils__.ft_sqrt(delta), 15) + "i"
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 15 :
			print("<=>	" + var + "_1 = " + arround1)
			str1 = arround1
		else :
			print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		if len(arround2[arround2.find('.') + 1:]) < 15 :
			print("	" + var + "_2 = " + arround2)
			str2 = arround2
		else :
			print("	" + var + "_2 ≈ " + arround2)
		return str2, str1
	if a == 1 :
		str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
		str2 = str_num + "i√" + __utils__.ft_round(delta, 0)
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta), 15) + "i"
		arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta), 15) + "i"
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 15 :
			print("<=>	" + var + "_1 = " + arround1)
			str1 = arround1
		else :
			print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		if len(arround2[arround2.find('.') + 1:]) < 15 :
			print("	" + var + "_2 = " + arround2)
			str2 = arround2
		else :
			print("	" + var + "_2 ≈ " + arround2)
		return str1, str2
	if a < 0 :
		str_den = __utils__.ft_round(-a, 15)
		str1 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
		str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
		print()
		print("<=>	" + var + "_1 = " + str1)
		print("	\33[33mor\033[32m")
		print("	" + var + "_2 = " + str2)
		arround1 = __utils__.ft_round(__utils__.ft_sqrt(delta) / -a, 15) + "i"
		arround2 = __utils__.ft_round(-__utils__.ft_sqrt(delta) / -a, 15) + "i"
	else :
		str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
		str2 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
		arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta) / a, 15) + "i"
		arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta) / a, 15) + "i"
	print("\033[35m")
	if len(arround1[arround1.find('.') + 1:]) < 15 :
		print("<=>	" + var + "_1 = " + arround1)
		str1 = arround1
	else :
		print("<=>	" + var + "_1 ≈ " + arround1)
	print("	\33[33mor\033[35m")
	if len(arround2[arround2.find('.') + 1:]) < 15 :
		print("	" + var + "_2 = " + arround2)
		str2 = arround2
	else :
		print("	" + var + "_2 ≈ " + arround2)
	if a < 0 :
		return str2, str1
	return str1, str2

def	delta_neg_notb_a(var, a, delta, p) :
	if __utils__.ft_sqrt(delta) == int(__utils__.ft_sqrt(delta)) :
		return delta_neg_notb_a_discriminant(var, a, delta, p)
	if delta == int(delta) :
		sq, delta = __bonus__.reduce_sqrt(delta)
		if sq :
			result = __bonus__.str_lst_sq(sq, delta)
			print()
			print("<=>	" + var + "_1 = -i√" + result + " / " + __utils__.ft_round(a, p))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = i√" + result + " / " + __utils__.ft_round(a, p))
			if len(sq) > 1 :
				sq = __bonus__.irreducible_sq(sq)
				result = __bonus__.str_lst_sq(sq, delta)
				print()
				print("<=>	" + var + "_1 = -i√" + result + " / " + __utils__.ft_round(a, p))
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = i√" + result + " / " + __utils__.ft_round(a, p))
			print()
			print("<=>	" + var + "_1 = -i√" + __utils__.ft_round(sq[0] * sq[0], 0) + "√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = i√" + __utils__.ft_round(sq[0] * sq[0], 0) + "√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
			primes1 = __bonus__.primes(sq[0])
			primes2 = __bonus__.primes(a)
			if len(primes1) > 1 or len(primes2) > 1 :
				print()
				print("<=>	" + var + "_1 = -" + __utils__.ft_round(sq[0], 0) + "i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + __utils__.ft_round(sq[0], 0) + "i√" + __utils__.ft_round(delta, 0) + " / " + __utils__.ft_round(a, p))
			delete = []
			__bonus__.reduce_fraction(primes1, primes2, delete)
			num = __bonus__.print_frac(primes1, delete, True)
			den = __bonus__.print_frac(primes2, delete, False)
			print()
			print("<=>	" + var + "_1 = -" + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
			__bonus__.fraction_delete(primes1, delete.copy())
			__bonus__.fraction_delete(primes2, delete.copy())
			num = __bonus__.print_frac(primes1, None, True)
			den = __bonus__.print_frac(primes2, None, False)
			print()
			print("<=>	" + var + "_1 = -" + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + num + "i√" + __utils__.ft_round(delta, 0) + " / " + den)
			num, den = __bonus__.irreducible(primes1, primes2)
			str_num = "" if num == 1 else __utils__.ft_round(num, 15)
			str_den = __utils__.ft_round(den, 15)
			if str_num or den < 0 :
				print()
				print("<=>	" + var + "_1 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			if den == -1 :
				den *= -1
				str_den = __utils__.ft_round(den, 15)
				print()
				print("<=>	" + var + "_1 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
				str1 = str_num + "i√" + __utils__.ft_round(delta, 0)
				str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
				print()
				print("<=>	" + var + "_1 = " + str1)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str2)
				arround1 = __utils__.ft_round(num * __utils__.ft_sqrt(delta), 15) + "i"
				arround2 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta), 15) + "i"
				print("\033[35m")
				if len(arround1[arround1.find('.') + 1:]) < 15 :
					print("<=>	" + var + "_1 = " + arround1)
					str1 = arround1
				else :
					print("<=>	" + var + "_1 ≈ " + arround1)
				print("	\33[33mor\033[35m")
				if len(arround2[arround2.find('.') + 1:]) < 15 :
					print("	" + var + "_2 = " + arround2)
					str2 = arround2
				else :
					print("	" + var + "_2 ≈ " + arround2)
				return str2, str1
			if den == 1 :
				str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
				str2 = str_num + "i√" + __utils__.ft_round(delta, 0)
				print()
				print("<=>	" + var + "_1 = " + str1)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str2)
				arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta), 15) + "i"
				arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta), 15) + "i"
				print("\033[35m")
				if len(arround1[arround1.find('.') + 1:]) < 15 :
					print("<=>	" + var + "_1 = " + arround1)
					str1 = arround1
				else :
					print("<=>	" + var + "_1 ≈ " + arround1)
				print("	\33[33mor\033[35m")
				if len(arround2[arround2.find('.') + 1:]) < 15 :
					print("	" + var + "_2 = " + arround2)
					str2 = arround2
				else :
					print("	" + var + "_2 ≈ " + arround2)
				return str1, str2
			if den < 0 :
				den *= -1
				str_den = __utils__.ft_round(den, 15)
				str1 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
				str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
				print()
				print("<=>	" + var + "_1 = " + str1)
				print("	\33[33mor\033[32m")
				print("	" + var + "_2 = " + str2)
				arround1 = __utils__.ft_round(num * __utils__.ft_sqrt(delta) / den, 15) + "i"
				arround2 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta) / den, 15) + "i"
			else :
				str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
				str2 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
				arround1 = __utils__.ft_round(-num * __utils__.ft_sqrt(delta) / den, 15) + "i"
				arround2 = __utils__.ft_round(num * __utils__.ft_sqrt(delta) / den, 15) + "i"
			print("\033[35m")
			if len(arround1[arround1.find('.') + 1:]) < 15 :
				print("<=>	" + var + "_1 = " + arround1)
				str1 = arround1
			else :
				print("<=>	" + var + "_1 ≈ " + arround1)
			print("	\33[33mor\033[35m")
			if len(arround2[arround2.find('.') + 1:]) < 15 :
				print("	" + var + "_2 = " + arround2)
				str2 = arround2
			else :
				print("	" + var + "_2 ≈ " + arround2)
			if den < 0 :
				return str2, str1
			return str1, str2
		str_num = ""
		str_den = __utils__.ft_round(a, 15)
		if a == -1 :
			a *= -1
			str_den = __utils__.ft_round(a, 15)
			print()
			print("<=>	" + var + "_1 = " + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = -" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den)
			str1 = str_num + "i√" + __utils__.ft_round(delta, 0)
			str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(__utils__.ft_sqrt(delta), 15) + "i"
			arround2 = __utils__.ft_round(-__utils__.ft_sqrt(delta), 15) + "i"
			print("\033[35m")
			if len(arround1[arround1.find('.') + 1:]) < 15 :
				print("<=>	" + var + "_1 = " + arround1)
				str1 = arround1
			else :
				print("<=>	" + var + "_1 ≈ " + arround1)
			print("	\33[33mor\033[35m")
			if len(arround2[arround2.find('.') + 1:]) < 15 :
				print("	" + var + "_2 = " + arround2)
				str2 = arround2
			else :
				print("	" + var + "_2 ≈ " + arround2)
			return str2, str1
		if a == 1 :
			str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0)
			str2 = str_num + "i√" + __utils__.ft_round(delta, 0)
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta), 15) + "i"
			arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta), 15) + "i"
			print("\033[35m")
			if len(arround1[arround1.find('.') + 1:]) < 15 :
				print("<=>	" + var + "_1 = " + arround1)
				str1 = arround1
			else :
				print("<=>	" + var + "_1 ≈ " + arround1)
			print("	\33[33mor\033[35m")
			if len(arround2[arround2.find('.') + 1:]) < 15 :
				print("	" + var + "_2 = " + arround2)
				str2 = arround2
			else :
				print("	" + var + "_2 ≈ " + arround2)
			return str1, str2
		if a < 0 :
			str_den = __utils__.ft_round(-a, 15)
			str1 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			str2 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			print()
			print("<=>	" + var + "_1 = " + str1)
			print("	\33[33mor\033[32m")
			print("	" + var + "_2 = " + str2)
			arround1 = __utils__.ft_round(__utils__.ft_sqrt(delta) / -a, 15) + "i"
			arround2 = __utils__.ft_round(-__utils__.ft_sqrt(delta) / -a, 15) + "i"
		else :
			str1 = "-" + str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			str2 = str_num + "i√" + __utils__.ft_round(delta, 0) + " / " + str_den
			arround1 = __utils__.ft_round(-__utils__.ft_sqrt(delta) / a, 15) + "i"
			arround2 = __utils__.ft_round(__utils__.ft_sqrt(delta) / a, 15) + "i"
		print("\033[35m")
		if len(arround1[arround1.find('.') + 1:]) < 15 :
			print("<=>	" + var + "_1 = " + arround1)
			str1 = arround1
		else :
			print("<=>	" + var + "_1 ≈ " + arround1)
		print("	\33[33mor\033[35m")
		if len(arround2[arround2.find('.') + 1:]) < 15 :
			print("	" + var + "_2 = " + arround2)
			str2 = arround2
		else :
			print("	" + var + "_2 ≈ " + arround2)
		if a < 0 :
			return str2, str1
		return str1, str2
	return delta_neg_notb_a_discriminant_float(var, a, delta, p)
