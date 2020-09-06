#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = """Darrell Purcell with help from Meagan Ramey on Regex
https://docs.python.org/3/library/re.html
https://www.w3schools.com/python/ref_string_strip.asp
https://www.geeksforgeeks.org/python-infinity/"""

from morse_dict import MORSE_2_ASCII


def decode_morse(morse):
    morse_group = ''
    phrase = ''
# strips leading or trailing whitespace and establishs length variable
    if morse.startswith(' ') or morse.endswith(' '):
        morse = morse.strip()
    length = len(morse)
# shortest possible morse length returns char E
    if length == 1:
        return 'E'
# iterates through morse string, creating morse groups and
# returns MORSE dictionary values for matching key patterns
    for i in range(length):
        if i == length - 1:
            morse_group += morse[-1]
            phrase += MORSE_2_ASCII[morse_group]
        elif morse[i] != ' ':
            word_space_found = False
            morse_group += morse[i]
        elif morse[i:(i + 3)] == '   ':
            phrase += MORSE_2_ASCII[morse_group] + " "
            morse_group = ''
            word_space_found = True
        elif not word_space_found:
            phrase += MORSE_2_ASCII[morse_group]
            morse_group = ''
    return phrase


def decode_bits(bits):
    # returns 'E' morse code in case of 1-only strings
    if len(bits) == 1 or '0' not in bits:
        return '.'
    # strip leading or trailing zeroes from bits
    if bits.startswith('0') or bits.endswith('0'):
        bits = bits.strip('0')
    # creates list of bits using zero as delimiter
    bit_list = re.split(r'([0]+)', bits)
    # sets time_unit to infinity
    time_unit = float('inf')
    # updates time_unit to smallest base frequency found
    for i in bit_list:
        if len(i) < time_unit:
            time_unit = len(i)
    # updates bit coding to conform with established time unit
    binary_word_space = '0000000' * time_unit
    binary_char_space = '000' * time_unit
    binary_nospace = '0' * time_unit
    binary_dash = '111' * time_unit
    binary_dot = '1' * time_unit
    morse_code = ''
    # establishes stop indexes for string slicing
    word_space_index = len(binary_word_space)
    char_space_index = len(binary_char_space)
    nospace_index = len(binary_nospace)
    dash_index = len(binary_dash)
    dot_index = len(binary_dot)
    # swaps matching bit patterns for corresponding morse code
    while len(bits) > 0:
        if bits[0:word_space_index] == binary_word_space:
            bits = bits.replace(bits[0:word_space_index], '', 1)
            morse_code += '   '
        elif bits[0:char_space_index] == binary_char_space:
            bits = bits.replace(bits[0:char_space_index], '', 1)
            morse_code += ' '
        elif bits[0:nospace_index] == binary_nospace:
            bits = bits.replace(bits[0:nospace_index], '', 1)
            morse_code += ''
        elif bits[0:dash_index] == binary_dash:
            bits = bits.replace(bits[0:dash_index], '', 1)
            morse_code += '-'
        else:
            bits = bits.replace(bits[0:dot_index], '', 1)
            morse_code += '.'
    return morse_code


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
