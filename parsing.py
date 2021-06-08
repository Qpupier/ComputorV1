# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parsing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 11:39:44 by qpupier           #+#    #+#              #
#    Updated: 2021/06/08 19:33:28 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import error as __error__

def	verif_variables(equation, precision, solution) :
	variable = None
	first = False
	for each in equation :
		if each[1] :
			if not first :
				variable = each[1][0]
				first = True
			elif each[1][0] != variable :
				__error__.error_var(equation, precision, solution)
	return variable

def	verif_n_naturals(equation, precision, solution) :
	for each in equation :
		if each[1] and (each[1][1] != int(each[1][1]) or each[1][1] < 0) :
			__error__.error_n_naturals(equation, precision, solution)

def	verif_n_second(equation, precision, solution) :
	for each in equation :
		if each[1] and each[1][1] > 2 :
			__error__.error_n_second(equation, precision, solution)

def	verif_last(equation, precision, solution) :
	if len(equation) > 3 :
		__error__.error_parsing(equation, precision, solution)

def	parsing(equation, precision, solution) :
	global var
	var = verif_variables(equation, precision, solution)
	verif_n_naturals(equation, precision, solution)
	verif_n_second(equation, precision, solution)
	verif_last(equation, precision, solution)
	return equation
