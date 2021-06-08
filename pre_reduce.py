# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pre_reduce.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 10:34:50 by qpupier           #+#    #+#              #
#    Updated: 2021/06/08 19:19:15 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import computor as __computor__
import verbose as __verbose__

def	update_var(equation, var) :
	for i in range(len(equation)) :
		if equation[var][0] and i != var and equation[i][0] :
			if equation[i][1] == equation[var][1] :
				equation[var][0] += equation[i][0]
				equation[i][0] = 0
				if verbose :
					__verbose__.print_step(equation, None, False, precision)
	return equation

def	pre_reduce(equation, v, p) :
	global verbose, precision
	verbose = v
	precision = p
	for i in range(len(equation)) :
		equation = update_var(equation, i)
	equation = __computor__.clear_equation(equation, precision)
	return equation

def	print_reduce(equation, precision, solution) :
	if not solution :
		print("Reduced form : 				", end="")
		__verbose__.print_step(equation, None, True, precision)

def	reduce(equation) :
	new = [[0, [None, 2]], [0, [None, 1]], [0, None]]
	eq = [0, 0, 0, None]
	for each in equation :
		if not each[1] :
			new[2] = each
			eq[2] = each[0]
		elif each[1][1] == 1 :
			new[1] = each
			eq[1] = each[0]
			eq[3] = each[1][0]
		elif each[1][1] == 2 :
			new[0] = each
			eq[0] = each[0]
			eq[3] = each[1][0]
	return new, eq
