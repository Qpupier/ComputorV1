# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree_1.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/14 15:00:48 by qpupier           #+#    #+#              #
#    Updated: 2021/06/14 16:03:19 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import verbose as __verbose__
import utils as __utils__
import bonus.utils as __bonus_utils__

def	degree_1_bonus(equation, var, p) :
	print("Polynomial degree : 1")
	print("\033[32m")
	print("Steps :")
	part2 = []
	part2.append(equation[2])
	equation.pop(2)
	part2[0][0] *= -1
	__verbose__.print_step(equation, part2, True, p)
	result = __utils__.ft_round(part2[0][0], p)
	if equation[1][0] != 1 and equation[1][0] != -1 :
		print("<=>	" + var + " = " + __utils__.ft_round(part2[0][0], p) + " / " + __utils__.ft_round(equation[1][0], p))
		div = __utils__.ft_round(part2[0][0] / equation[1][0], 15)
		if div == int(float(div)) :
			result = str(int(div))
			result = str(int(div))
			print("<=>	" + var + " = " + result)
		else :
			num = part2[0][0]
			div = equation[1][0]
			if num == int(num) :
				num = int(num)
			if div == int(div) :
				div = int(div)
			mult = __bonus_utils__.irreducible_mult(num, div)
			if mult > 1 :
				print("<=>	" + var + " = " + str(num) + " * " + str(mult) + " / (" + str(div) + " * " + str(mult) + ")")
				num = int(__utils__.ft_round(int(num * mult), 0))
				div = int(__utils__.ft_round(int(div * mult), 0))
				print("<=>	" + var + " = " + str(num) + " / " + str(div))
			primes_num = __bonus_utils__.primes(num)
			primes_div = __bonus_utils__.primes(div)
			delete = []
			__bonus_utils__.reduce_fraction(primes_num, primes_div, delete)
			if delete :
				print("<=>	" + var + " = ", end="")
				__bonus_utils__.print_fraction(primes_num, primes_div, delete)
				print()
				__bonus_utils__.fraction_delete(primes_num, delete.copy())
				__bonus_utils__.fraction_delete(primes_div, delete.copy())
				print("<=>	" + var + " = ", end="")
				__bonus_utils__.print_fraction(primes_num, primes_div, None)
				print()
				if len(primes_num) > 1 or len(primes_div) > 1 :
					num, div = __bonus_utils__.irreducible(primes_num, primes_div)
					print("<=>	" + var + " = " + str(num) + " / " + str(div))
				else :
					num = 1 if not primes_num else primes_num[0]
					div = 1 if not primes_div else primes_div[0]
			if div < 0 :
				num *= -1
				div *= -1
				print("<=>	" + var + " = " + str(num) + " / " + str(div))
			round = __utils__.ft_round(num / div, 15)
			equal = " ≈ "
			result = str(num) + " / " + str(div)
			if len(round[round.find('.') + 1:]) < 15 :
				equal = " = "
				result = round
			print("\033[35m<=>	" + var + equal + __utils__.ft_round(num / div, 15) + "\033[0m")
	elif equation[1][0] == -1 :
		part2[0][0] *= -1
		result = __utils__.ft_round(part2[0][0], p)
		print("<=>	" + var + " = " + result)
	print("\033[33;1m")
	print("S = {" + result + "}\033[0m")
