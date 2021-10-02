#!/usr/bin/env python3
from collections import namedtuple
import re

"""
Valid sentence checker . 

For use in consuming applications import the function then invoke the 'is_valid_sentence' function.

import sentence_checker

sentence_checker_result = sentence_checker.is_valid_sentence('The quick brown fox said hello Mr lazy dog.')

if sentence_checker_result.success:
     #do something
else:
    print (sentence_checker_result.error_message)

"""
Result = namedtuple('Result', 'success error_message')                      # NamedTuple to store result and the success states 

# Public method to be invoked by consuming applications
def is_valid_sentence(sentence):     
    success = True
    errors = []

    empty_string = _check_for_empty_string(sentence)
    if not empty_string.success:
        success = False
        errors.append(str(empty_string.error_message))

    capital_checker = _capital_checker(sentence)
    if not capital_checker.success:
        success = False
        errors.append(str(capital_checker.error_message))

    even_quotes = _even_quotes(sentence)
    if not even_quotes.success:
        success = False
        errors.append(str(even_quotes.error_message))
    
    end_char = _end_char(sentence)
    if not end_char.success:
        success = False
        errors.append(str(end_char.error_message))
    
    no_stray_period = _no_stray_period(sentence)
    if not no_stray_period.success:
        success = False
        errors.append(str(no_stray_period.error_message))
  
    number_under_13 = _number_under_13(sentence)
    if not number_under_13.success:
        success = False
        errors.append(str(number_under_13.error_message))
  
    return Result(success, '. '.join(errors))


# Check whether the sentence is empty
def _check_for_empty_string(sentence):
    if sentence:
        return Result(True, "")
    else:
        return Result(False, 'Sentences can not be empty')

# Check whether the first letter of the sentence passed to it is uppercase
def _capital_checker(sentence):
    if sentence:
        upper_error = 'This sentence is invalid as the first letter of your sentence is NOT uppercase!'
        alpha_error = 'Please start sentences with letters!'
        if not sentence[0].isalpha() and not sentence[0].isupper():       # check that the first character of the users input is a letter and first character of the users input is a letter
            return Result(False, alpha_error + ". " + upper_error)    
        elif not sentence[0].isalpha():                                    # check that the first character of the users input is a letter
            return Result(False, alpha_error)     
        elif not sentence[0].isupper():                                    # check that the first character of the users input is a letter
            return Result(False, upper_error)
        else:
            return Result(True, "")
    else:
        return Result(True, "")

# Check for an even number of quotes##
def _even_quotes(sentence):
    num_quotes = 0                                      # initialise a counter
    quote_chars = ['\"', '\'','“', '”']                 # list of characters considered quotes
    for char in sentence:                               # for loop iterates over all characters in user input
        if char in quote_chars:                         # check for quotes
            num_quotes += 1                             # quote counter updates
    if num_quotes%2 == 0:                               # check for even number of quotes
        return Result(True, "")
    else:
        return Result(False, 'This sentence is invalid as it contains an odd number of quotes!')

# Check that the last character in the user input is a suitable one
def _end_char(sentence):
    if sentence:
        termination_chars = ['.', '!', '?']
        if not sentence[-1] in termination_chars:               # index the last character and check it is in the list of acceptable characters
            return Result(False, 'The sentence is invalid, it does not contain any of the following termination characters: {},{},{}'.format('.','!','?'))
        else:
            return Result(True, "")
    else:
        return Result(True, "")

# Check that there are no periods apart from one at the end of the sentence
def _no_stray_period(sentence):
    if sentence.find('.',0, len(sentence)-1) != -1:     # looks for a period from the first character to the penultimate one
        return Result(False, 'This sentence is invalid as it contains a period at a position other than the end of the sentence!')
    else:
        return Result(True, "")


# Check the user input for numbers 0-12 and tells the user to rewrite these as words
def _number_under_13(sentence):
    if sentence:                                          # check sentence not null 
        
        numbers_in_sentence = re.findall(r"\d+",sentence) # find all digits in the sentence

        invalid_numbers = ['0','1','2','3','4','5','6','7','8','9','10','11','12']      

        invalid_numbers_exist =  any(item in invalid_numbers for item in numbers_in_sentence)     #returns True if any of the invalid numbers are found in the list of numbers contained in sentence
        
        if invalid_numbers_exist:
             return Result(False, 'This sentence is invalid, please write numbers 0-12 as words') 
        else:
            return Result(True, "")     
    else:
        return Result(True, "")        


# Main function that inititates user input and progresses through the sentence checker functions
def main():                                                                             
    sentence = input('Please enter your sentence here:\n') 
    
    sentence_checker_result = is_valid_sentence(sentence)                  # obtain the result of is_valid_sentence and store it in the variable sentence_checker_result
    if sentence_checker_result[0]:                                         # check whether the output is True (successful) 
        print('Sentence is valid')
    else:
        print('Sentence is invalid. ' + sentence_checker_result[1])        # if the output is False, access the second value in the namedtuple which is the string containing any error messages
   
if __name__ == '__main__':                                               
    main()




