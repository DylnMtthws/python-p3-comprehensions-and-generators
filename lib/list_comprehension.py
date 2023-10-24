#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


def make_exclamation(sentence_list):
    exclamations = []
    for phrase in sentence_list:
        exclamation = phrase + "!"
        exclamations.append(exclamation)
    return exclamations