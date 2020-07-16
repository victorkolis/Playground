#!/usr/bin/env python3

# AUTHOR: Victor Kolis 

# Understanding the game:
''' 
Enter any text at all into the prompt when you run this game
And it will convert your text into a readable numtext type of file.
'''

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

