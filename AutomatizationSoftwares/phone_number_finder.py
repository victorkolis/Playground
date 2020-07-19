#!/usr/bin/env python3
# Victor deMatos
# Copyright (c) 2020 CODE FUTURE INVENT

# Description:
# This piece of software's goal is to satisfy a need to find patterns
# in a text (of any sort) to trim off phone number patterns
# such as americans and canadians are: xxx-xxx-xxxx

import re
import pprint

def phone_number_catcher(text_by_user):
    regex_compiler = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    list_of_numbers_found = regex_compiler.findall(text_by_user)
    if list_of_numbers_found == []:
        print('No number(s) found in the text!')
    else:
        pprint.pprint(list_of_numbers_found)
user_input = input('Enter/paste desired text: ')
phone_number_catcher(user_input)
