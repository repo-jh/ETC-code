"""
In this example, how to decrypt caesar cipher.

Author : Choi JaeHun
Last edited : 2017-08-28
"""

import sys

# cipher = "CSYEVIXIVQMREXIH"
# cipher = "VSRQJHEREVTXDUHSDQWV"
cipher = "IRXUVFRUHDQGVHYHQBHDUVDJR"

def decrypt(cipher, factor):
	convert_ascii(cipher, factor)

def convert_ascii(cipher, factor):
	ascii_list = []
	for i in cipher: ascii_list.append(ord(i))
	shift_ascii(ascii_list, factor)

def shift_ascii(ascii_list, factor):
	shift_list = [[] for i in range(25)]
	for i in range(1, 26):
		for j in ascii_list:
			if factor is 'r':
				if j+i > 90: 
					shift_list[i-1].append(64+((j+i)-90)) 
				else: 
					shift_list[i-1].append(j+i)
			elif factor is 'l':
				if j-i < 65:
					shift_list[i-1].append(91-(65-(j-i))) 
				else:
					shift_list[i-1].append(j-i)
			else: 
				print("factor is not vaild.")
				sys.exit()
	result(shift_list)

def result(shift_list):
	result_list = [[] for i in range(25)]
	for i in range(1, 26):
		for j in shift_list[i-1]:
			result_list[i-1].append(chr(j))
	for i in range(1, 26):
		str = ''.join(result_list[i-1])
		print("(round {})".format(i), str)

decrypt(cipher, 'l') # factor >>> l: left, r: Right
