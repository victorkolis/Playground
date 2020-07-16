#!/usr/bin/env python3

a = input('Please enter a sentence: ')

a = a.lower()

def replacer(sentence):
	sentence = sentence.replace('a', '4')
	sentence = sentence.replace('b', '8')
	sentence = sentence.replace('e', '3')
	sentence = sentence.replace('i', '1')
	sentence = sentence.replace('o', '0')
	sentence = sentence.replace('s', '5')
	sentence = sentence.replace('t', '7')
	sentence = sentence.replace('g', '9')
	print(sentence)

replacer(a)

