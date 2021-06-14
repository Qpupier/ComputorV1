# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 11:07:54 by qpupier           #+#    #+#              #
#    Updated: 2021/06/14 17:00:40 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import re
import verbose as __verbose__
import pre_reduce as __pre_reduce__
import parsing as __parsing__
import algo as __algo__
import utils as __utils__

def	error(err):
	print(err)
	exit()

def	parse_pow(var) :
	lst = var.split('^')
	if len(lst) == 1 :
		lst.append("1")
	if len(lst) != 2 or lst[0] != lst[0].strip() or lst[1] != lst[1].strip() :
		error("Invalid syntax (Power)")
	if not re.findall(r"^[a-zA-Z]+$", lst[0]) or lst[0] == "i" :
		error("Invalid syntax (Variable)")
	try :
		lst[1] = float(lst[1])
	except :
		error("Invalid syntax (Power)")
	return lst

def	check_neg(var) :
	var = var.strip()
	if var[0] == '-' :
		var = var[1:]
	else :
		var = "-" + var
	if var != var.strip() :
		error("Invalid syntax")
	return var

def	parse_var(var) :
	nb = var.count(" * ")
	if nb > 1 :
		error("Too many multiplications")
	if not nb :
		tmp = re.findall(r"[a-zA-Z].*$", var)
		if not tmp or not tmp[0] :
			try :
				test = var.strip()[0] == '+'
				var = float(var.strip())
			except :
				error("Invalid syntax (Coefficient)")
			if test :
				error("Invalid syntax (Coefficient)")
			return [var, None]
		var = var.replace(tmp[0], " * " + tmp[0])
	new = var.split(" * ")
	if re.findall(r"[a-zA-Z]", new[0]) :
		tmp = new[0]
		new[0] = new[1]
		new[1] = tmp
		if new[1][0] == '-' :
			new[0] = check_neg(new[0])
			new[1] = new[1][1:]
	if len(new) != 2 :
		error("Invalid syntax (Multiplication)")
	if not new[0] :
		new[0] = "1"
	elif new[0] == "-" :
		new[0] = "-1"
	if new[0].strip()[0] == '+' :
		error("Invalid syntax (Coefficient)")
	try :
		new[0] = float(new[0].strip())
	except :
		error("Invalid syntax (Coefficient)")
	new[1] = parse_pow(new[1].strip())
	return new

def	parse_part(part) :
	lst = part.split(" - ")
	new = lst[0].strip()
	for i in range(1, len(lst)) :
		lst[i] = lst[i].strip()
		if not lst[i] :
			error("Invalid syntax")
		lst[i] = check_neg(lst[i])
		new += " + " + lst[i]
	new = new.split(" + ")
	for i in range(len(new)) :
		new[i] = parse_var(new[i])
	return new

def	neg(part) :
	for i in range(len(part)) :
		part[i][0] *= -1
	return part

def	join_parts(part1, part2) :
	for i in range(len(part2)) :
		part1.append(part2[i])
	return part1

def	clear_equation(eq, prec) :
	for i in range(len(eq) - 1, -1, -1) :
		if __utils__.ft_round(eq[i][0], prec) == "0" :
			eq[i][0] = 0
	for i in range(len(eq) - 1, -1, -1) :
		if not eq[i] or not eq[i][0] :
			eq.pop(i)
	for i in range(len(eq)) :
		if eq[i][1] and not eq[i][1][1] :
			eq[i][1] = None
	return eq

def	nb_prec(number) :
	prec = 0
	# try :
	while number != int(number) :
		prec += 1
		number *= 10
	# except OverflowError :
		# print("OK")
	return prec

def	check_precision(part) :
	precision = 0
	for each in part :
		nb = nb_prec(each[0])
		if nb > precision :
			precision = nb
		if each[1] :
			nb = nb_prec(each[1][1])
			if nb > precision :
				precision = nb
	return precision if precision <= 15 else 15

def	equation(entry, v, s) :
	global verbose, precision, solution
	verbose = v
	solution = s
	if entry.count('=') != 1 :
		error("Wrong number of equals")
	entry = entry.replace(',', '.')
	part = entry.split('=')
	part1 = parse_part(part[0])
	part2 = parse_part(part[1])
	precision = check_precision(part1)
	tmp = check_precision(part2)
	if tmp > precision :
		precision = tmp
	part1 = clear_equation(part1, precision)
	part2 = clear_equation(part2, precision)
	if verbose :
		print("\033[32mSteps :")
		__verbose__.print_step(part1, part2, True, precision)
	part = clear_equation(join_parts(part1, neg(part2)), precision)
	precision = check_precision(part)
	if verbose and part and part2 :
		__verbose__.print_step(part, None, False, precision)
	part = __pre_reduce__.pre_reduce(part, verbose, precision)
	if verbose :
		print("\033[0m")
	part = __parsing__.parsing(part, precision, solution)
	part, eq = __pre_reduce__.reduce(part)
	__pre_reduce__.print_reduce(part, precision, solution)
	__algo__.resolve(part, eq[3], eq[0], eq[1], eq[2], precision, verbose, solution)
	return part
