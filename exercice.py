#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	num = 0
	for char in text:
		if char.isalnum() == True:
			num += 1
		else:
			num += 0

	return num

def get_word_length_histogram(text):
	words_list = text.split()
	num_letters = []
	for words in words_list:
		num_letters.append(get_num_letters(words))

	num_letters = sorted(num_letters)

	len_list = max(num_letters)
	list = [0 for _ in range(len_list+1)]

	for num in num_letters:
		list[num] += 1

	return list

def format_histogram(histogram):
	ROW_CHAR = "*"
	histo = ""
	for i, n in enumerate(histogram[1:]):
		histo += f"{i+1} {ROW_CHAR * n} \n"

	return histo

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	histo = ""

	for n in histogram:
		if n >= 3:
			histo += BLOCK_CHAR
		elif n < 3:
			histo += " "

	histo += f"\n"

	for n in histogram:
		if n >= 2:
			histo += BLOCK_CHAR
		elif n < 2:
			histo += " "

	histo += f"\n"

	for n in histogram:
		if n >= 1:
			histo += BLOCK_CHAR
		elif n < 1:
			histo += " "

	histo += f"\n"

	histo += LINE_CHAR * len(histogram)




	return histo


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
