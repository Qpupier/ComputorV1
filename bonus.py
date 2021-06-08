# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bonus.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 19:39:06 by qpupier           #+#    #+#              #
#    Updated: 2021/06/08 20:31:55 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import verbose as __verbose__
import utils as __utils__

def	primes(nb) :
	return

def	irreducible(num, div, p) :
	verif = False
	while not verif and p > 0 :
		try :
			if num != int(num) or div != int(div) :
				num *= 10
				div *= 10
			else :
				verif = True
		except :
			num *= 10
			div *= 10
		p -= 1
	num = int(__utils__.ft_round(num, 0))
	div = int(__utils__.ft_round(div, 0))
	print(num, div)
	first = primes(num)
	second = primes(div)

def	degree_1_bonus(equation, var, p) :
	print("Polynomial degree : 1")
	print("\033[32m")
	print("Steps :")
	part2 = []
	part2.append(equation[2])
	equation.pop(2)
	part2[0][0] *= -1
	__verbose__.print_step(equation, part2, True, p)
	if equation[1][0] != 1 :
		print("<=>	" + var + " = " + __utils__.ft_round(part2[0][0], p) + " / " + __utils__.ft_round(equation[1][0], p))
		div = __utils__.ft_round(part2[0][0] / equation[1][0], 15)
		irreducible(part2[0][0], equation[1][0], p)
		try :
			int(div)
			print("<=>	" + var + " = " + div)
		except :
			pass
	# 	print(var + " = " + s)
	# 	print()
	# print("\033[33;1mS = {", end="")
	# print(s, end="")
	# print("}\033[0m")
